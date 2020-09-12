var mongoose = require('mongoose');

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
module.exports = user = mongoose.model("user", userSchema);