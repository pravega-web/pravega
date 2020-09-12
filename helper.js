// Helpers for Server

// Libraries for helpers

const pug = require('pug');
const moment = require('moment');

class Helpers {
  constructor() {
    this.sendLogs = async (res) => {
      var logSet = await logs.find({});
      logSet.reverse();
      res.send(
        pug.compileFile(__dirname + "/public/front_end/views/dev/logs.pug")({
          date: new Date(),
          logs: logSet,
          moment: moment
        })
      );
    }
    this.logit = async function(head, body) {
      await logs.create({ log: { head: head, body: body } }).then(
        res => {
          console.log("Logged to DB");
        },
        err => {
          console.log("Unsuccessfull Log!");
        }
      );
    }
  
  }
}

module.exports = () => {
  return new Helpers();
};

