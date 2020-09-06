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

function displayLink(links) {
    let output = "";

    if(links.ms_platform) {
        if(links.ms_link == false) {
            output += '<li><span>Meeting link</span> <a href="#"> Will be updated soon </a></li>';
        }
        else {
            output += '<li><span>Meeting link</span> <a href="' + links.ms_link +'"> Will be updated soon </a></li>';
        }
    }
    if(links.youtube_platform) {
        if(links.youtube_link == false) {
            output += '<li><span>Youtube link</span> <a href="#"> Will be updated soon </a></li>';
        }
        else {
            output += '<li><span>Youtube link</span> <a href="' + links.youtube_link + '"> Click here </a></li>';
        }
    }
    return output;
}

let pre_image = '<div class="m-bot-100"> <div class="col-md-6"><div class="full-width"><img src="elementary/'
let post_image = '" alt="">';
let pre_title = '</div></div><div class="col-md-6"><div class="heading-title-side-border text-left"><h2 class="text-uppercase">';
let post_title = '</h2>';
let pre_prof = '<h4>By Prof. ';
let post_prof = '</h4>';
let pre_date = '<ul class="portfolio-meta m-bot-30"><li><span>Date and time</span> ';
let post_date = '</li>';
let pre_abstract = '</ul><p><b>Abstract:</b> ';
let post_abstract = '</p>';
let pre_bio = '<p><b>Bio:</b> ';
let post_bio = '</p></div></div><hr><br><br>'

let lectures = [];

lectures.push(
    {
        image: "DrPSM.png",
        number: 1,
        title: "Chemistry in Molecular Vessel",
        prof: "Partha Sarathi Mukherjee",
        date: {
            day: 29,
            month: "August",
            time: "6 PM",
        },
        links: {
            ms_platform: false,
            youtube_platform: true,
            youtube_link: "https://www.youtube.com/watch?v=HWT78BciE0Q",
        },
        abstract: "Properties of chemical entities in confined nanospace are expected to be different from their bulk properties due to restricted rotational and vibrational motions. Such restricted motions along with other interaction(s) may allow to stabilize unusual conformations of compounds in confined space of molecular cavities. Moreover, reactivity and reaction pathways in confined space may become different from traditional bulk reactions leading to the formation of unusual product(s). In this regard, chemists have been trying to design artificial molecular vessels to perform chemical reactions in their confined nanospace. Design of 3D molecular architectures having hydrophobic confined space including their use for catalytic organic transformations will be discussed. The lecture will also focus on the interior decoration of nanocages with urea moieties for new generation discrete heterogeneous catalysts for Michael addition. It is also planned to focus on our recent work on the use of confined space of discrete organic cages for the nucleation of tiny palladium nanoparticles and their successful use in photocatalytic transformation of nitroaromatics to corresponding azo-compounds. Our recent work on the design of enantiopure coordination cages for enantioselective recognition will also be presented in brief. ",
        bio: "Prof. Partha Sarathi Mukherjee is a Professor at the Inorganic and Physical Chemistry department of the Indian Institute of Science, Bangalore. He is a fellow of the Royal Society of Chemistry, a fellow of the Indian Academy of Sciences and has received the Shanti Swarup Bhatnagar Prize for science and technology awarded by the CSIR. He is renowned for his studies on organic nanostructures, molecular sensors and catalysis in nanocages. ",
    },
    {
        image: "DrJemmis.png",
        number: 2,
        title: "Elementary Questions",
        prof: "E.D. Jemmis",
        date: {
            day: 2,
            month: "September",
            time: "5:30 PM",
        },
        links: {
            ms_platform: true,
            ms_link: false,
            youtube_platform: false,
        },
        abstract: "No question is elementary; yet in some ways all questions are. Often general questions are asked in the early stages of one’s education, just as it happened in the beginning of human civilization before different disciplines evolved. A question asked in my UG days that took thirty years even to get a partial answer will be presented. This involved the search for an equivalent of structural and electronic structural relationships of compounds of carbon and its allotropes, in the chemistry of boron. This has led to development of interrelationships amongst polyhedral boranes, beta-rhombohedral boron, borophenes and borospherenes, in many ways related to fullerenes and graphene. ",
        bio: "Prof. Eluvathingal D. Jemmis holds the Year of Science Chair Professorship (SERB) at the Department of Inorganic and Physical Chemistry Department of Indian Institute of Science, and studies structure and reactivity problems of chemistry computationally. He received the Shanti Swarup Bhatnagar Prize (CSIR), and Padma Shri from Govt of India, and was the founding Director of IISER Thiruvananthapuram. ",
    },
)

lectures = lectures.sort((a,b) => (b.number - a.number));

let lectures_display = document.getElementById("lectures-display");

for (let lecture of lectures) {
    lectures_display.innerHTML += pre_image + lecture.image + post_image
    + pre_title + `Talk ${lecture.number}: ` + lecture.title + post_title
    + pre_prof + lecture.prof + post_prof 
    + pre_date + displayDate(lecture.date) + post_date
    + displayLink(lecture.links)
    + pre_abstract + lecture.abstract + post_abstract
    + pre_bio + lecture.bio + post_bio;
}