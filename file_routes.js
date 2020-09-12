var helper = require(__dirname+'/helper')();

module.exports = function(app){

  app.get("/userhome", (req, res) => {
    res.sendFile(__dirname + "/public/front_end/views/user_home.html");
  });
  

  app.get("/template", (req, res) => {
    console.log("Template");
    res.sendFile(__dirname + "/public/front_end/views/template.html");
  });

  app.get("/login", (req, res) => {
    res.sendFile(__dirname + "/public/front_end/views/login.html");
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

  // Logs
  app.get("/logs", (req, res) => {
    console.log(helper);
    helper.sendLogs(res);
  });
  
}
