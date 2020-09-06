"use strict"

function addData(rank, name, institute, studies, points) {
    let output = "";

    output += `<td> ${rank} </td>`;
    output += `<td> ${name} </td>`;
    output += `<td> ${institute} </td>`;
    output += `<td> ${studies} </td>`;
    output += `<td> ${points} </td>`;

    return output;
};

let data = [];

data.push(
    {
        name: "The One Who Knocks",
        institute: "IISER Pune",
        studies: "2" + "nd".sup() + " Year (UG)",
        points: 36
    },
    {
        name: "Hydrogen",
        institute: "IISER Pune",
        studies: "2" + "nd".sup() + " Year (UG)",
        points: 35
    },
    {
        name: "Mandita Dutta",
        institute: "IISER Kolkata",
        studies: "2" + "nd".sup() + " Year (UG)",
        points: 13
    },
    {
        name: "Shyreyasri Sain",
        institute: "Visvabharati university",
        studies: "2" + "nd".sup() + " Year (UG)",
        points: 31
    },
    {
        name: "Sayan Goswani",
        institute: "Visvabharati university",
        studies: "2" + "nd".sup() + " Year (UG)",
        points: 24
    },
    {
        name: "Garga Mondal",
        institute: "Visvabharati university",
        studies: "2" + "nd".sup() + " Year (UG)",
        points: 23
    },
    {
        name: "Tobo",
        institute: "Presidency University",
        studies: "2" + "nd".sup() + " Year (UG)",
        points: 12
    },
    {
        name: "Meghana V",
        institute: "Christ university",
        studies: "2" + "nd".sup() + " Year (UG)",
        points: 21
    },
    {
        name: "Prithu",
        institute: "Dolna Day school",
        studies: "12" + "th".sup() + " Std",
        points: 17
    },
    {
        name: "Nayan Banerjee",
        institute: "IACS Kolkata",
        studies: "2" + "nd".sup() + " Year (UG)",
        points: 15
    },
    {
        name: "Soumili Biswas",
        institute: "Salt Lake school",
        studies: "12" + "th".sup() + " Std",
        points: 16
    },
    {
        name: "Sarthak",
        institute: "Baranagar Narendranath Vidyamandir",
        studies: "12" + "th".sup() + " Std",
        points: 16
    }
)

data = data.sort((a, b) => b.points - a.points);

let leaderboard = document.getElementById("leaderboard");
let num_display = 10;

for(let rank = 0; rank < num_display; rank++) {
    leaderboard.innerHTML += "<tr>" + addData(rank + 1, data[rank].name, data[rank].institute, data[rank].studies, data[rank].points) + "</tr>";
}


    

