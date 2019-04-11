document.addEventListener("DOMContentLoaded",function() {


var dictInputs = {"name":"test"};

const start = document.querySelector(".start");
start.addEventListener('click', createParagraph);

const submit = document.querySelector(".submit");
submit.addEventListener('click', addToDict);



function test(){
    var iban = document.getElementById("iban")
    var message = iban.value;
    var paragraphEl = document.createElement('p');
    paragraphEl.textContent = iban.value;
    document.body.appendChild(paragraphEl);
};


function addToDict(){
    var iban = document.getElementById("iban")
    dictInputs.push({
        key:   "iban",
        value: iban.value,
    });
    var paragraphEl = document.createElement('p');
    paragraphEl.textContent = dictInputs["iban"];
    document.body.appendChild(paragraphEl);
};


function createParagraph(){
    var paragraphEl = document.createElement('p');
    paragraphEl.textContent = dictInputs["name"];
    document.body.appendChild(paragraphEl);
};
});