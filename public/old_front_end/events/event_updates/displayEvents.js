"use strict";
let months = ["January", "Febraury", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

function displayLink(update) {
    let output = "";

    if (update.category == "Science") {
        return "../science_eve/" + update.link;
    }
    else if (update.category == "Cultural") {
        return "../cultural_eve/" + update.link;
    }
}

function displayDate(update) {

    if ('date_custom' in update) {
        return update.date_custom;
    }
    else {
        let output = update.date_meta;

        let date = update.date.getDate();
        output += ` ${date}`;

        if (date == 1 || date == 21 || date == 31)
            output += "st".sup();
        else if (date == 2 || date == 22)
            output += "nd".sup();
        else if (date == 3 || date == 23)
            output += "rd".sup();
        else
            output += "th".sup();

        output += " ";

        output += months[update.date.getMonth()];

        return output;
    }
}

let updates = [];
updates.push(
    {
        name: "BioBlitz",
        image: "bioblitz-update.jpeg",
        date: new Date(2020, 7, 15),
        date_meta: "Starts from",
        category: "Science",
        link: "bioblitz.html",
        permanent: true,
        show: true,
    },
    {
        name: "Shutters",
        image: "shutters-update.png",
        date: new Date(2020, 7, 16),
        date_meta: "Starts from",
        category: "Cultural",
        link: "shutters.html",
        permanent: true,
    },
    {
        name: "Elementary",
        image: "elementary-update.jpeg",
        date: new Date(2020, 7, 17),
        date_meta: "Starts from",
        category: "Science",
        link: "elementary.html",
        permanent: true,
    },
    {
        name: "Triviathon",
        image: "triviathon-update.png",
        date: new Date(2020, 7, 23),
        date_meta: "Starts from",
        category: "Cultural",
        link: "triviathon.html",
        permanent: true,
        show: true,
    },
    {
        name: "Spooky Quizzes",
        image: "spooky-quizzes-update.jpeg",
        date: new Date(2020, 7, 30),
        date_meta: "Starts from",
        category: "Science",
        link: "spooky.html",
        permanent: true,
        show: true,
    },
    {
        name: "Alekhya",
        image: "alekhya-update.png",
        date: new Date(2020, 8, 1),
        date_meta: "Starts from",
        category: "Cultural",
        link: "alekhya.html",
        permanent: true,
        show: true,
    },
    {
        name: "Cosplay",
        image: "cosplay-update.png",
        date: new Date(2020, 8, 16),
        date_meta: "Ends on",
        category: "Cultural",
        link: "cosplay.html",
        permanent: true,
        show: true,
    },
    {
        name: "Naturally Creative",
        image: "naturally-creative.jpeg",
        date: new Date(2020, 8, 19),
        date_custom: "19" + "th".sup() + " and 20" + "th".sup() + " September",
        category: "Cultural",
        link: "naturally_creative.html",
        permanent: true,
        show: true,
    },
    {
        name: "Astral Felony",
        image: "astral-update.jpeg",
        date: new Date(2020, 8, 24),
        date_custom: "Last week of September",
        category: "Science",
        link: "astral_felony.html",
        permanent: true,
        show: true,
    },
);
updates = updates.sort((a, b) => (b.date - a.date));

let updates_month = document.getElementById("updates-month");
let updates_category = document.getElementById("updates-category");
let updates_display = document.getElementById("updates-display");

displayEvents();

function displayEvents() {

    let month_selected = updates_month.value;
    let category_selected = updates_category.value;

    for (let update of updates) {
        update.show = true;
        if (month_selected == "august" && update.date.getMonth() != 7)
            update.show = false;
        if (month_selected == "september" && update.date.getMonth() != 8)
            update.show = false;
        if (category_selected == "science" && update.category != "Science")
            update.show = false;
        if (category_selected == "cultural" && update.category != "Cultural")
            update.show = false;
    }

    updates_display.innerHTML = ""

    for (let update of updates) {
        if (update.show) {
            updates_display.innerHTML += `<div class="m-bot-100">
                                            <div class="col-md-6">
                                                <div class="full-width">
                                                    <img src="${update.image}" alt="">
                                                </div>
                                            </div>
                                            <div class="col-md-6">
                                                <div class="heading-title-side-border text-left">
                                                    <h1 class="text-uppercase">${update.name}</h1>
                                                    <div class="title-border-container">
                                                        <div class="title-border"></div>
                                                    </div>
                                                </div>
                                                <ul class="portfolio-meta m-bot-30">
                                                    <li><span>Date</span> ${displayDate(update)}</li>
                                                    <li><span> Category </span> ${update.category}</li>
                                                    <li><span> Website link</span> <a href="${displayLink(update)}">${update.name}
                                                            website</a></li>
                                                </ul>
                                            </div>
                                        </div>`
        }
    }

    for(let update of updates) {
        update.show = true;
    }
}