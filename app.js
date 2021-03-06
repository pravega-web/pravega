//SCSCSCSCSCSCSCSCSCSCSCSCSCSCSCSCSCSCSCSCSCSCSCSC
// Pravega Central Server

const express = require("express");
const app = express();

// Libraries which we need
const mongoose = require("mongoose");
var cors = require("cors");
var compression = require("compression");
app.locals.moment = require("moment");

// Load ENV variables
require("dotenv").config();

// AWS for mailing
var AWS = require("aws-sdk");

// Static folders to serve
app.use(express.static(__dirname + "/public/"));

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(function (req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header(
    "Access-Control-Allow-Headers",
    "Origin, X-Requested-With, Content-Type, Accept"
  );
  res.header("Accept-Encoding: gzip");
  next();
});
app.use(compression());

// File serving routes
require(__dirname + "/file_routes.js")(app);

// Webinar routes
require(__dirname + "/webinar.js")(app);

// DB handling
// require(__dirname+'/admin.js')(app);

// Helper Functions here
var helper = require(__dirname + "/helper.js")();
var logit = helper.logit; // Need to pull this out just in case...

// Global variables
const caCreditMultiplier = 0.05;
const min_val = 0;
const max_val = 50;

// MongoDB Connection string
var uri =
  "mongodb+srv://pravega_developer:123qwerty@pravega-qebux.mongodb.net/test?retryWrites=true&w=majority";

// Mongoose connection
mongoose.connect(uri, { useNewUrlParser: true, useUnifiedTopology: true });
var db = mongoose.connection;

// Run the rest of the program only if db connection is succesful
db.once("open", (e) => {
  server();
});

function server() {
  // Mongoose models
  var event = require(__dirname + "/models/event.js");
  var webinar = require(__dirname + "/models/webinar.js");
  var logs = require(__dirname + "/models/logs.js");
  var user = require(__dirname + "/models/user.js");
  var cfreg = require(__dirname + "/models/cfreg.js");
  var regs = require(__dirname + "/models/regs.js");

  // Front End
  app.use("/", express.static(__dirname + "/Front End"));

  // Testing new Website
  // app.use('/', express.static('GameFace'))

  // General Purpouse

  // User
  require(__dirname + "/user.js")(app);

  // CA System
  require(__dirname + "/credit.js")(app);

  // Front end viewing data
  require(__dirname + "/view.js")(app);

  // Razorpay Integration
  // require(__dirname + '/rpay.js')(app, AWS);

  // Check if connection was successful
  db.on("error", (e) => {
    console.log("Mongoose connection error: No Mongo Instance running ");
  });

  console.log(
    "Server started at ",
    app.locals.moment(new Date()).format("hh : mm : s")
  );

  const listener = app.listen(process.env.PORT || 3000, () => {
    console.log("Your app is listening on port " + listener.address().port);
  });
}
