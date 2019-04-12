document.addEventListener("DOMContentLoaded",function() {

let counter = 0
var dictInputs= {"name": "", "vorname":"", "strasse":""}

const start = document.querySelector(".start");
start.addEventListener('click', createParagraph,);



function createParagraph() {
    let input_key = Object.keys(dictInputs)[counter];
    if (counter === 0){
        start.parentNode.removeChild(start);
    }
    var card = document.createElement('div');
    var input = document.createElement("INPUT");
    var submit = document.createElement("button");
    input.setAttribute("type", "text");
    input.setAttribute("id", "input");
    input.setAttribute("placeholder", input_key);
    submit.setAttribute("value", "test")
    submit.setAttribute("class", "button")
    submit.addEventListener('click', addToDict);
    card.appendChild(input);
    card.appendChild(submit);
    card.setAttribute("id", input_key)
    document.body.appendChild(card);
};

/*function createButton(){
    const submitAll = document.createElement("button");
    submitAll.setAttribute("name", "helloButton");
    submitAll.setAttribute("class", "button")
    submitAll.addEventListener('click', safeToDb);
    document.body.appendChild(submitAll);
};

function safeToDb() {
};
*/

function addToDict(){
    let input_key = Object.keys(dictInputs)[counter];
    var input = document.getElementById("input");  
    dictInputs[input_key] = input.value;
    var paragraphEl = document.createElement('p');
    paragraphEl.textContent = dictInputs[input_key];
    document.body.appendChild(paragraphEl);
    //destroy or hide previous card
    counter += 1
    createParagraph();
};
});


/*
1. move through list of inputs_names with submit of createParagraph
2. Safe input as variable
3. submit variables to backend
4. create back button
5. create cards and visuable feedback
6. create info button
7. create progress bar
*/