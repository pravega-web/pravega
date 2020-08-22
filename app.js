//SCSCSCSCSCSCSCSCSCSCSCSCSCSCSCSCSCSCSCSCSCSCSCSC
//Pravega Central Server

const express = require("express");
const app = express();

// Libraries which we need
const bodyParser = require("body-parser");
const mongoose = require("mongoose");
var cors = require("cors");
var cowsay = require("cowsay");
const pug = require("pug");
const http = require("http");
var compression = require("compression")
app.locals.moment = require("moment");

app.use(express.static(__dirname + "/public"));
app.use('/face',express.static(__dirname + "/public/face"))
app.use(bodyParser.json());
app.use(function (req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header(
    "Access-Control-Allow-Headers",
    "Origin, X-Requested-With, Content-Type, Accept"
  );
  res.header('Accept-Encoding: gzip')
  next();
});
app.use(compression())

// GLobal variables

const caCreditMultiplier = 0.05;
const min_val = 0;
const max_val = 50;

var uri =
  "mongodb+srv://pravega_developer:123qwerty@pravega-qebux.mongodb.net/test?retryWrites=true&w=majority";

mongoose.connect(uri, { useNewUrlParser: true });
var db = mongoose.connection;

// Check if connection was successful
db.on("error", e => {
  console.log("Mongoose connection error: No Mongo Instance running ");
});

// Run the rest of the program only if db connection is succesful
db.once("open", e => {
  server();
});

function server() {

  // Schema for user object
  var userSchema = new mongoose.Schema({
    edu: String,
    name: String,
    phone: mongoose.Schema.Types.Mixed,
    email: mongoose.Schema.Types.Mixed,
    meta: {
      type: mongoose.Schema.Types.Mixed,
      default: {
        credit: 0,
        trId: Math.floor(Math.random() * 10000)
      }
    },
    pword: mongoose.Schema.Types.Mixed,
    ca: {
      required: false,
      is: {
        type: mongoose.Schema.Types.Boolean,
        required: false
      },
      credit: {
        type: Number,
        required: false,
        default: 0
      }
    },
    refId: {
      type: Number,
      required: true
    }
  });

  // Construct team as mongoose object
  var user = mongoose.model("user", userSchema);

  var webinarSchema = new mongoose.Schema({
    name: String,
    start: Date,
    end: Date,
    description: {
      info: String,
      speaker: String,
      speakerInfo: String,
      talkInfo: String
    },
    link: String
  });

  var webinar = mongoose.model("Webinars", webinarSchema);

  // CF registrations
  var cfregSchema = new mongoose.Schema({
    ticketId: {
      type: String,
      required: true
    },
    ticket: mongoose.Schema.Types.Mixed
  });

  var cfreg = mongoose.model("CollegeFeverRegistrations", cfregSchema);

  // Logs

  var logSchema = new mongoose.Schema({
    timeStamp: {
      type: Date,
      default: new Date()
    },
    log: {
      head: { type: mongoose.Schema.Types.Mixed },
      body: { type: mongoose.Schema.Types.Mixed }
    }
  });

  var logs = mongoose.model("Logs", logSchema);

  async function logit(head, body) {
    await logs.create({ log: { head: head, body: body } }).then(
      res => {
        console.log("Logged to DB");
      },
      err => {
        console.log("Unsuccessfull Log!");
      }
    );
  }

  // logit("INFO", "Server loaded...");

  // Routing

  // app.get("/", (req, res) => {
  //   console.log("Homepage");
  //   res.sendFile(__dirname + "/public/front_end/views/index.html");
  // });

  app.use('/', express.static('public/old_front_end'))

  app.get("/template", (req, res) => {
    console.log("Template");
    res.sendFile(__dirname + "/public/front_end/views/template.html");
  });

  app.get("/login", (req, res) => {
    res.sendFile(__dirname + "/public/front_end/views/login.html");
  });

  app.get("/userhome", (req, res) => {
    res.sendFile(__dirname + "/public/front_end/views/user_home.html");
  });

  app.get("/ca/home", (req, res) => {
    res.sendFile(__dirname + "/public/front_end/views/ca_home.html");
  });

  app.get("/vendor", (req, res) => {
    res.sendFile(__dirname + "/public/front_end/views/vendor.html");
  });

  app.get("/ca/signup", (req, res) => {
    res.sendFile(__dirname + "/public/front_end/views/ca_register.html");
  });

  app.get('/form', (req, res) => {
    res.sendFile(__dirname + "/public/front_end/views/form.html")
  })

  app.get("/paradigms", (req, res) => {
    webinar.find((err, data) => {
      var live = {
        is: true,
        live: false,
        wbnr: data[0]
      };
      if (err) throw err;

      data.forEach(wbnr => {
        wbnr.start = new Date(wbnr.start.getTime() + 5.5 * 3600 * 1000);
        wbnr.end = new Date(wbnr.end.getTime() + 5.5 * 3600 * 1000);
        // console.log(app.locals.moment(wbnr.start).format('DD / MM / YYYY hh : mm a'))
        idanim = new Date(new Date().getTime() + 5.5 * 3600 * 1000);
        // console.log(app.locals.moment(idanim).format('DD / MM / YYYY hh : mm a'))

        wbnr.icon = "keyboard_arrow_down";
        if (idanim < wbnr.end && idanim > wbnr.start) {
          console.log("Live event");
          live.is = true;
          live.wbnr = wbnr;
          live.live = true;
        } else {
          // console.log('No event live');
        }
      });

      data.sort(function (a, b) {
        var keyA = new Date(a.start),
          keyB = new Date(b.start);
        // Compare the 2 dates
        if (keyA < keyB) return -1;
        if (keyA > keyB) return 1;
        return 0;
      });

      res.send(
        pug.compileFile(
          __dirname + "/public/front_end/views/webinar/masterlink.pug"
        )({
          moment: app.locals.moment,
          future: data,
          live: live
        })
      );
    });
  });





  // Webinars 

  app.get("/api/edit/webinars", (req, res) => {
    res.sendFile(
      __dirname + "/public/front_end/views/webinar/edit-webinar.html"
    );
  });

  // Webinar Creation
  app.post("/api/webinar", (req, res) => {
    webinar.create(req.body, (err, data) => {
      if (err) throw err;
      res.send(data);
    });
  });

  // Webinar Updation
  app.post("/api/update/webinar", (req, res) => {
    webinar.updateOne({ _id: req.body._id }, req.body, (e, d) => {
      if (e) throw e;
      res.send(d.nModified + "");
    });
  });

  // Webinar Retrieval
  app.get("/api/webinar", (req, res) => {
    webinar.find((err, data) => {
      if (err) throw err;
      res.send(data);
    });
  });

  // Webinar Deletion
  app.put("/api/webinar", (req, res) => {
    console.log(req.body);
    webinar.deleteOne({ _id: req.body._id }, (e, d) => {
      if (e) throw e;
      res.send(d);
    });
  });


  // General Purpouse 

  // Login
  app.post("/api/login", (req, res) => {
    user.find(
      { email: req.body.username, pword: req.body.password },
      (err, data) => {
        if (err) {
          throw err;
        }
        if (!data[0]) {
          res.status(401).send("Auth failed: Wrong creds");
        } else {
          res.send(data);
        }
      }
    );
  });




  // User


  // Create user
  app.post("/api/create/user", (req, res) => {
    // Add all preprocessing to data here
    var newUser = req.body;
    genRefId(newUser, res);
  });

  // Find user
  app.post("/api/find/user", (req, res) => {
    user.find(req.body, (err, data) => {
      if (err) throw err;
      res.send(data);
    });
  });

  // Updating user
  app.post("/api/update/user", (req, res) => {
    console.log(req.body);
    user.updateOne({ _id: req.body._id }, req.body, (err, data) => {
      if (err) {
        throw err;
      }
      console.log("Updated: ", data.nModified == 1);
      res.send(data);
    });
  });

  // pword update
  app.post("/api/update/user/pword", (req, res) => {
    res.send("OK");
  });




  // CA System 



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



  // Logs
  app.get("/logs", (req, res) => {
    sendLogs(res);
  });




  // Helper functions
  function genRefId(newUser, res) {
    rand = Math.floor(Math.random() * 100000);
    user.findOne({ refId: rand }, (err, data) => {
      if (err) {
        throw err;
      }
      //Check unique
      if (data) {
        genRefId(newUser);
      } else {
        newUser.refId = rand;
        user.create(newUser, (err1, data) => {
          if (err1) {
            throw err1;
          }
          res.send(data);
        });
      }
    });
  }

  // Credit CA
  // TODO: MOST Important Function as of now
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

  // TODO: Logger
  async function sendLogs(res) {
    var logSet = await logs.find({});

    logSet.reverse();
    res.send(
      pug.compileFile(__dirname + "/public/front_end/views/dev/logs.pug")({
        date: new Date(),
        logs: logSet,
        moment: app.locals.moment
      })
    );
  }

  app.get("/stayinalive", (req, res) => {
    console.log("Just pinged from external.");
    res.send("OK");
    setTimeout(e => {
      callHeroku();
    }, 10 * 60 * 2);
  });

  console.log('Server started at ', new Date());

  const listener = app.listen(process.env.PORT || 3000, () => {
    console.log("Your app is listening on port " + listener.address().port);
  });
}
