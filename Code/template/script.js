document.addEventListener("DOMContentLoaded",function() {


var inputDict= {"name": "", "vorname":"", "strasse":""}

const start = document.querySelector(".start");
start.addEventListener('click', createParagraph);



function createParagraph() {
    start.parentNode.removeChild(start)
    var form = document.createElement('form');
    var input = document.createElement("INPUT");
    var submit = document.createElement("INPUT")
    input.setAttribute("type", "text");
    input.setAttribute("placeholder", "Name");
    submit.setAttribute("type", "submit");
    form.appendChild(input);
    form.appendChild(submit);
    form.setAttribute("id", "id_1");
    document.getElementById("formSpace").appendChild(form);
    const submitAll = document.createElement("button");
    submitAll.setAttribute("name", "helloButton");
    submitAll.addEventListener('click', safeToDb);
    document.getElementById("submitAllSpace").appendChild(submitAll);
}

function safeToDb() {
}
});


/*
1. move through list of inputs_names with submit of createParagraph
2. Safe input as variable
3. submit variables to backend
4. create back button
5. create cards and visuable feedback
6. create info button
7. create progress bar*/