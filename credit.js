const cors = require('cors');

module.exports = function (app) {

  // v1 - Accepting CA code only
  app.post("/api/cf/register", cors(), (req, res) => {
    // Call an async function so main thread can continue.
    creditCa(req.body);
    // Does it matter what you send them ?
    res.send("OK");
  });

  // Crediting CA
  app.post("/api/ca/credit", (req, res) => {
    user.findOne({ refId: req.body.refId }, (err, data) => {
      if (err) throw { err };
      if (data) {
        data.ca.credit += req.body.credit;
        user.update({ _id: data._id }, (err1, updata) => {
          if (err) throw err;
          res.send(data);
        });
      } else {
        res.send("Invalid reference id");
      }
    });
  });

  // Vendor
  app.post("/api/credit", (req, res) => {
    if (mongoose.Types.ObjectId.isValid(req.body._id)) {
      user.find({ _id: req.body._id }, (err, data) => {
        if (err) throw err;
        if (data[0].meta.trId == req.body.trId) {
          if (data[0].meta.credit > req.body.credit) {
            var upd = data[0];
            upd.meta.credit = data[0].meta.credit - req.body.credit;
            upd.meta.trId = Math.floor(Math.random() * 10000);
            user.findOneAndUpdate(
              { _id: data[0]._id },
              upd,
              (err1, updated) => {
                if (err1) throw err1;
                res.send("Success");
              }
            );
          } else {
            res.send("Insufficient credits");
          }
        } else {
          res.send("Transaction ID incorrect!");
        }
      });
    } else {
      console.log(req.body._id);
      res.send("Invalid ID");
    }
  });

}

// Credit CA
// MOST Important Function as of now
async function creditCa(receipt) {
  var oldRegistration = await cfreg.findOne({ ticketId: receipt.ticketId });

  if (oldRegistration) {
    // Yell at CF
    console.log("Dupes Error. TCF get it fixed");
    logit("DUPES ERROR", "TCF GET IT FIXED");
  } else {
    var newCfReg = await cfreg.create({
      ticketId: receipt.ticketId,
      ticket: receipt
    });

    // Iterate through the list of tickets
    for (const ticket of receipt.ticketItems) {
      // Find CA based on refernce code
      refId = parseInt(ticket.attendee.customTField0);

      logit("INFO", "Incoming Registration : " + receipt.ticketId);

      if (typeof refId == "number" && !isNaN(refId)) {
        var ca = await user.findOne({ refId: refId });
        console.log("CA :", ticket.attendee.customTField0);

        // If found ( valid reference ID )
        if (ca) {
          // Credit
          credit = Math.min(
            max_val,
            Math.max(min_val, Math.round(caCreditMultiplier * ticket.fare))
          );

          console.log(
            "CA: ",
            ticket.attendee.customTField0,
            " | credited : ",
            credit
          );

          // Math.min(50, Math.round(caCreditMultiplier * ticket.fare))

          // Increase the credit and update the CA's account
          ca.ca.credit += credit;
          ca.meta.credit += credit;

          record = {
            name: ticket.attendee.name,
            event: ticket.programName,
            credit: credit,
            timeStamp: new Date()
          };

          if (!ca.meta.refs) {
            ca.meta.refs = [];
            ca.meta.refs.push(record);
          } else {
            ca.meta.refs.push(record);
          }

          var upd = await user.updateOne({ _id: ca._id }, ca);
          console.log(upd.nModified);

          if (upd.nModified == 1) {
            logit(
              "INFO",
              "CA :" + ticket.attendee.customTField0 + " CREDITED : " + credit
            );
          } else {
            logit(
              "ERROR - 2",
              "CA :" +
              ticket.attendee.customTField0 +
              " NOT CREDITED : " +
              credit
            );
          }

          // 1 - Success, 0 - Failure

          ca = {};
        } else {
          // Send to server ?
          console.log("CA CODE: NoT FounD");
          logit(
            "INFO",
            "CA Code Invalid (Referred and Wrong) :" +
            ticket.attendee.customTField0
          );
        }
      } else {
        console.log("INVALID CA CODE");
        logit(
          "INFO",
          "CA Code Invalid (Not referred) :" + ticket.attendee.customTField0
        );
      }
    }

    // Verify async is actually async
    // console.log('Done!')
    // var lol = await user.findOne({ 'refId': ticket.attendee.refId });
    // lol.ca.credit += caCreditMultiplier * 100
    // user.updateOne({_id:lol._id},lol, (err,updRes)=>{
    //   if(err) throw(err);
    //   console.log(updRes.nModified)
    // })
  }
}
