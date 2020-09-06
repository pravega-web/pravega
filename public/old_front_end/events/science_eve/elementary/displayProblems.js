"use strict"

function displayDate(date) {
    let output = `${date.day}`;

    if(date.day == 1 || date.day == 21 || date.day == 31) {
        output += "st".sup();
    }
    else if(date.day == 2 || date.day == 22) {
        output += "nd".sup();
    }
    else if(date.day == 3 || date.day == 23) {
        output += "rd".sup();
    }
    else {
        output += "th".sup();
    }
    output += ` ${date.month} at ` + date.time;

    return output;
}

function displayDetails(problem) {
    let output = "";

    output += "<li><span>Uploaded on</span> " + displayDate(problem.uploaded)
    + "</li><li><span>Deadline</span> " + displayDate(problem.deadline)
    + "</li><li><span>Points</span> " + `${problem.points}` 
    + '</li><li><span>Link</span> <a href="elementary/' + `problem_${problem.num}`
    + '.pdf"> Download problem</a> </li>';

    if(problem.has_solution) {
        output += '<li><span>Solution</span> <a href="elementary/' + `solution_${problem.num}`
        + '.pdf"> View solution</a> </li>';
    }
    return output;
}

let problems = [];
problems.push(
    {
        num: 1,
        title: "How to be a good Host?",
        uploaded: {
            day: 17,
            month: "August",
            time: "9 PM",
        },
        deadline: {
            day: 19,
            month: "August",
            time: "9 PM",
        },
        points: 10,
        has_solution: true, 
    },
    {
        num: 2,
        title: "Not a Bed of Roses",
        uploaded: {
            day: 21,
            month: "August",
            time: "1:30 PM",
        },
        deadline: {
            day: 19,
            month: "August",
            time: "8:30 PM",
        },
        points: 10,
        has_solution: true, 
    },
    {
        num: 3,
        title: "A Case of Catalysis",
        uploaded: {
            day: 24,
            month: "August",
            time: "1:30 PM",
        },
        deadline: {
            day: 24,
            month: "August",
            time: "8:30 PM",
        },
        points: 10,
        has_solution: true, 
    },
    {
        num: 4,
        title: "It's in Your Blood!",
        uploaded: {
            day: 27,
            month: "August",
            time: "1:30 PM",
        },
        deadline: {
            day: 27,
            month: "August",
            time: "8:30 PM",
        },
        points: 10,
        has_solution: true, 
    },
    {
        num: 5,
        title: "A Race to Racemize",
        uploaded: {
            day: 31,
            month: "August",
            time: "1:30 PM",
        },
        deadline: {
            day: 31,
            month: "August",
            time: "8:30 PM",
        },
        points: 10,
        has_solution: true, 
    },
);

problems = problems.sort((a,b) => b.num - a.num);

let pre_image = '<div class="m-bot-100"><div class="col-md-6"><div class="full-width"><img src="elementary/';
let post_image = '.jpg" alt=""></div></div>';
let pre_title = '<div class="col-md-6"><div class="heading-title-side-border text-left"><h2 class="text-uppercase">';
let post_title = '</h2><div class="title-border-container"><div class="title-border"></div></div></div>';
let pre_details = '<ul class="portfolio-meta m-bot-30">';
let post_details = '</ul></div></div><hr>';

let problems_display = document.getElementById("problems-display");

for(let problem of problems) {
    problems_display.innerHTML += pre_image + `problem_${problem.num}` + post_image
    + pre_title + `Problem ${problem.num}: ${problem.title}` + post_title
    + pre_details + displayDetails(problem) + post_details;
}