const mongoose = require('mongoose');

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
      "marks": 4,
      "correct": [
        "cone_2"
      ]
    },
    "ctwo": {
      "marks": 4,
      "correct": [
        "ctwo_1"
      ]
    },
    "cthree": {
      "marks": 4,
      "correct": [
        "cthree_2"
      ]
    },
    "cfour": {
      "marks": 6,
      "correct": [
        "cfour_1"
      ]
    },
    "cfive": {
      "marks": 2,
      "correct": [
        "cfive_2"
      ]
    },
    "csix": {
      "marks": 2,
      "correct": [
        "csix_1"
      ]
    },
    "cseven": {
      "marks": 2,
      "correct": [
        "cseven_2"
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
  }


  // Getting users responses

  
  var qresSchema = new mongoose.Schema({
    'user': { type: mongoose.Schema.Types.ObjectId },
    'start': { type: Date, default: new Date() },
    'end': { type: Date },
    'response': { type: mongoose.Schema.Types.Mixed }
  })

  var bbres = mongoose.model("BioBlitz Responses", qresSchema);

  bbres.find((e, responses) => {
    if (e) throw e;

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
     * So t summarise.
     * 
     * 1) Ensure your data has end and answers.
     * 2) Evaluate
     * 3) Party
     */

    // Put the script here
    console.log(responses);

  // Update script goes here.

  // I'll put this part in when you're done.
  });

}