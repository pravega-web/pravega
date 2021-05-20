  // Events
  var mongoose = require('mongoose')

  var regsSchema = new mongoose.Schema({
    'name':{
      type:String,
      default:'Name'
    },
    'email':{
        type:String,
        default:'pravega.website@gmail.com'
    },
    'date':{
        type:Date,
        default: new Date()
    },
    'event':{
        type:String,
        default: 'Event Name'
    },
    'rpay':{
        type: mongoose.Schema.Types.Mixed,
        default:{}
    },
    'meta':mongoose.Schema.Types.Mixed
  })

  module.exports = regs = mongoose.model('Registrations',regsSchema)