var mongoose = require('mongoose');

// CF registrations
var cfregSchema = new mongoose.Schema({
  ticketId: {
    type: String,
    required: true
  },
  ticket: mongoose.Schema.Types.Mixed
});

var cfreg = module.exports = mongoose.model("CollegeFeverRegistrations", cfregSchema);