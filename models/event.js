  // Events
  var mongoose = require('mongoose')

  var eventSchema = new mongoose.Schema({
    'name':{
      type:String,
      default:'eventName'
    },
    'coordinators':{
      type : Array,
      default:[]
    },
    'password':{
      type: String
    },
    'genre':{
      type:String
    },
    'content':{
      'intoduction':String,
      'events':[
        { 
          'heading':String,
          'description':String
        }
      ],
      'tagline':String
    },
    'meta':mongoose.Schema.Types.Mixed
  })

  module.exports = event = mongoose.model('Events',eventSchema)