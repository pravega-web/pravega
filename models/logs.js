var mongoose = require('mongoose');


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

module.exports =  logs = mongoose.model("Logs", logSchema);
