module.exports = function (app) {

  app.get('/talks', (req, res) => {
    res.sendFile(__dirname + '/public/front_end/views/webinar/masterlink.html')
  })

  app.get('/paradigms',(req, res) => {
    res.sendFile(__dirname + '/public/front_end/views/webinar/gotopage.html')
  })

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
      res.send(data.sort(function(a, b){
        return (new Date(a.start) - new Date(b.start))
      }));
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


}