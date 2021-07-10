  // Events
  var mongoose = require('mongoose')

  var eventSchema = new mongoose.Schema({
    'name':{
      type:String,
      default:'eventName'
    },
    'orgs':{
      type : Array,
      default:[]
    },
    'genre':{
      type:String
    },
    'tagline':{
      type: String,
      default: "This event's tagline."
    },
    'description':{
      type: String,
      default: "This event's description."
    },
    'updates':{
      type:Array,
      default: [
        {
          'date':"",
          'updates':[]
        }
      ]
    },
    'subevents':{
      type:Array,
      default:[]
    },
    'phone':{
      type: String,
      default:""
    },
    'email':{
      type: String,
      default:""
    },
    'meta':mongoose.Schema.Types.Mixed
  })

  module.exports = event = mongoose.model('Events',eventSchema)