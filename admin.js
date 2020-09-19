const mongoose = require('mongoose');

async function displayUsernames(results) {
  for (const key in results) {
    var entry = results[key];
    var person = await user.findOne({ _id: entry.user });
    console.log(person.name);
  }
}

module.exports = (app) => {

  console.log('Started admin service...');

  // JSON answer key
  var answers = {
    "aone": {
      "marks": 2,
      "correct": [
        "CARBOHYDRATE"
      ]
    },
    "atwo": {
      "marks": 2,
      "correct": [
        "ARCHAEOPTERYX"
      ]
    },
    "athree": {
      "marks": 1,
      "correct": [
        "Na(I) / K(I) - ATPASE PUMP",
        "Na(I) / K(I) - ATPase PUMP",
        "SODIUM(I) / POTASSIUM(I) - ATPASE PUMP",
        "SODIUM(I) / POTASSIUM(I) - ATPase PUMP",
        "Na(I) / K(I) - ATPASE",
        "Na(I) / K(I) - ATPase",
        "SODIUM(I) / POTASSIUM(I) - ATPASE",
        "SODIUM(I) / POTASSIUM(I) - ATPase"
      ]
    },
    "afour": {
      "marks": 1,
      "correct": [
        "Escherichia coli"
      ]
    },
    "afive": {
      "marks": 1,
      "correct": [
        "ANTON VAN LEEUWENHOEK",
        "ANTONI VAN LEEUWENHOEK",
        "ANTONIE VAN LEEUWENHOEK"
      ]
    },
    "asix": {
      "marks": 1,
      "correct": [
        "HOMOGENISATION",
        "HOMOGENIZATION"
      ]
    },
    "aseven": {
      "marks": 1,
      "correct": [
        "ELEPHANT",
        "ELEPHANTS",
        "Elephas maximus"
      ]
    },
    "aeight": {
      "marks": 1,
      "correct": [
        "HIV"
      ]
    },
    "anine": {
      "marks": 1,
      "correct": [
        "THEOPHRASTUS"
      ]
    },
    "aten": {
      "marks": 1,
      "correct": [
        "AMENSALISM",
        "ALLELOPATHY",
        "ANTIBIOSIS"
      ]
    },
    "bone": {
      "marks": 1,
      "correct": [
        "MITOCHONDRIA"
      ]
    },
    "btwo": {
      "marks": 1,
      "correct": [
        "PHAGE"
      ]
    },
    "bthree": {
      "marks": 1,
      "correct": [
        "DEHYDROGENASE"
      ]
    },
    "bfour": {
      "marks": 1,
      "correct": [
        "SYNAPSIS"
      ]
    },
    "bfive": {
      "marks": 1,
      "correct": [
        "SCID"
      ]
    },
    "bsix": {
      "marks": 1,
      "correct": [
        "LYSOSOME",
        "MEMBRANE"
      ]
    },
    "bseven": {
      "marks": 1,
      "correct": [
        "INTERFERON"
      ]
    },
    "beight": {
      "marks": 1,
      "correct": [
        "RNA POLYMERASE",
        "R.N.A.POLYMERASE",
        "R.N.A POLYMERASE"
      ]
    },
    "bnine": {
      "marks": 2,
      "correct": [
        "EPISOME"
      ]
    },
    "bten": {
      "marks": 1,
      "correct": [
        "PLASMOLYSIS"
      ]
    },
    "beleven": {
      "marks": 2,
      "correct": [
        "AMBER"
      ]
    },
    "btwelve": {
      "marks": 1,
      "correct": [
        "CAPSID"
      ]
    },
    "bthirteen": {
      "marks": 2,
      "correct": [
        "DIPLOTENE"
      ]
    },
    "bfourteen": {
      "marks": 2,
      "correct": [
        "LIPOPROTEIN"
      ]
    },
    "bfifteen": {
      "marks": 2,
      "correct": [
        "PLASMODESMATA"
      ]
    },
    "cone": {
      "marks": 2,
      "correct": [
        "cone_2"
      ]
    },
    "ctwo": {
      "marks": 2,
      "correct": [
        "ctwo_1"
      ]
    },
    "cthree": {
      "marks": 2,
      "correct": [
        "cthree_2"
      ]
    },
    "cfour": {
      "marks": 2,
      "correct": [
        "cfour_2"
      ]
    },
    "cfive": {
      "marks": 2,
      "correct": [
        "cfive_1"
      ]
    },
    "csix": {
      "marks": 4,
      "correct": [
        "csix_2"
      ]
    },
    "cseven": {
      "marks": 6,
      "correct": [
        "cseven_1"
      ]
    },
    "ceight": {
      "marks": 4,
      "correct": [
        "ceight_3"
      ]
    },
    "cnine": {
      "marks": 4,
      "correct": [
        "cnine_6"
      ]
    }
  };

  // array of questions
  let questions = [];
  for (let [key, value] of Object.entries(answers)) {
    questions.push(key);
  }

  // contains score, validity of responses and 
  let results = [];

  // Getting users responses

  var qresSchema = new mongoose.Schema({
    'user': { type: mongoose.Schema.Types.ObjectId },
    'start': { type: Date, default: new Date() },
    'end': { type: Date },
    'response': { type: mongoose.Schema.Types.Mixed }
  })

  var bbres = mongoose.model("BioBlitz Responses", qresSchema);

  var user = require(__dirname + '/models/user.js')
  console.log(user);





  bbres.find((e, entries) => {
    if (e) throw e;

    // console.log(mongoose.Schema.Types.ObjectId(entries[0]._id));
    
    // Users responses

    // Hey, Chandan!
    // There are two kinds of data in the db, this is to ensure this is for security reasons.
    /**
     * The first kind is with only start time and no answers.
     * The second kind is with all answers and start and end date.
     * 
     * Evaluate only the second kind (obvio)
     * Ensure that end - start <= 2 hours ( be a lil flexible there to allow for network latency)
     * Then see if user answer belongs to array of acceptable answers.
     * 
     * Verify with the coords if we can evaluate case insensitively. ( in which case convert to upper caps or lower before comparision ) 
     * If your script works... Tell me to send the next part which is to update the server with the correct answers.
     * 
     * Ciao and thanks.
     * 
     * So to summarise.
     * 
     * 1) Ensure your data has end and answers.
     * 2) Evaluate
     * 3) Party
     */

    var test1_responses = []

    // Put the script here
    for (let index = 0; index < entries.length; index++) {
      var response = entries[index];
      if (response.response) {
        if (!('test' in response.response)) {
          //console.log(response._id);
          test1_responses.push(response);
          // console.log(response._id)
        }
      }
    }
    // displayUsernames(test1_responses);

    // evaluation loop
    for (let entry of test1_responses) {

      let display_response = "";

      let result = {
        user_name: entry.user,
        score: 0,
        duration: 0, // in hours
      }

      // checks validity of response; if valid, then evaluates the score.
      for (let question of questions) {
        if (question in entry.response) {

          if (question == "athree") {
            if ((entry.response[question].toUpperCase().includes("SODIUM") && entry.response[question].toUpperCase().includes("POTASSIUM") && entry.response[question].toUpperCase().includes("ATPASE")) || (entry.response[question].toUpperCase().includes("NA") && entry.response[question].toUpperCase().includes("K") && entry.response[question].toUpperCase().includes("ATPASE"))) {
              result.score += answers[question].marks;
            }
          }
          else if (question == "aeight") {
            if (entry.response[question].includes("HIV")) {
              result.score += answers[question].marks;
            }
          }
          else if (answers[question].correct.includes(entry.response[question])) {
            result.score += answers[question].marks;
          }

          if (question == "athree" || question == "aeight") {
            display_response += "custom";
          }
          else {
            display_response += entry.response[question];
          }
        }
        else {
          display_response += "No Ans";
        }
        display_response += '^';

        if (question == "aten" || question == "bfifteen" || question == "cnine") {
          display_response += (result.score + '^');
        }
      }

      // checks duration
      let duration = entry.end - entry.start;
      if (Number.isNaN(duration)) {
        result.duration = -1;
      }
      else {
        result.duration = duration / (3600 * 1000);
      }

      console.log(display_response);
      results.push(result);
    }
    // end of evaluation loop 

    //results = results.sort((a, b) => b.score - a.score);

    // console.log("USER ID | Score | Validity of responses | Duration (in hours)");
    for (let result of results) {
      // OUTPUT given to BioBlitz coords in form of a spreadsheet
      // console.log(result.user_name, result.score, result.duration.toFixed(2));
    }

  });


  

}


async function namakarana(results = Array){
  for (const key in results) {
    var entry = results[key];
    var person = await user.findOne({_id:entry.user_id}); 
    console.log(person.name);
  }
}