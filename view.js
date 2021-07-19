// This is for routing all the front end  folders and the data required to bind them.

module.exports = (app) => {
  app.get("/api/event", (req, res) => {
    console.log(req.query.name);
    event.findOne({ name: req.query.name }, (e, d) => {
      if (e) throw e;
      if (!d) {
        res.status(404).send("No event like that bois");
      } else {
        res.send(d);
      }
    });
  });

  app.post("/api/event", (req, res) => {
    console.log(req.body);
    event.updateOne({ _id: req.body._id }, req.body, (err, data) => {
      if (err) throw err;
      console.log(data.nModified);
      res.send(data);
    });
  });

  // Gameface Front End Serving System
  app.get("/events/*/:event", (req, res) => {
    res.sendFile(__dirname+'/Front End/event.html')
  });

  // Data for gameface
  app.get('/api/event/data', (req, res)=>{
    console.log(req.query);
    res.sendFile(__dirname + '/event data/' + decodeURI(req.query.name) + '.json');
  })

  // About Us and Contact (Plus Legal)
  app.get('/contact', (req,res)=>{
    res.sendFile(__dirname+'/Front End/contact.html');
  })
    
};
