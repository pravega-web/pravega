var mongoose = require('mongoose');

var webinarSchema = new mongoose.Schema({
  name: String,
  start: Date,
  end: Date,
  description: {
    info: String,
    speaker: String,
    speakerInfo: String,
    talkInfo: String,
    event:{
      type: String,
      default: "Paradigms"
    }
  },
  link: String
});

module.exports =  webinar = mongoose.model("Webinars", webinarSchema);

