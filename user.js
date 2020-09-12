module.exports = (app) => {
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

}

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
