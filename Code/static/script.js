document.addEventListener("DOMContentLoaded",function() {

var counter = 1

const start = document.getElementById("submit1");
start.addEventListener('click', card);

function card(){
    console.log("clicked")
    var paragraphEl = document.createElement('p');
    paragraphEl.textContent = 'You clicked the button!'
    paragraphEl.setAttribute("id","element");
    document.body.appendChild(paragraphEl);
};

});


/*
var counter = 1
var dictInputs={}

let submitCounter = "submit".concat(counter.toString());
submit = document.getElementById(submitCounter);
submit.addEventListener('click', next, addToDict);
console.log(submitCounter)

function next(){
    counter ++
    getElementById(counter-1).style.visibility = "hidden";
    getElementById(counter).style.visibility = "visible";
};

function back(){
    counter --
    getElementById(counter+1).style.visibility = "hidden";
    getElementById(counter).style.visibility = "visible";

};

function addToDict(){
    var input = document.getElementById(counter);  
    dictInputs[input_key] = input.value;
*/