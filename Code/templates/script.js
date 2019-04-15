document.addEventListener("DOMContentLoaded",function() {

let counter = 0
//get dict-keys from database
var dictInputs= {"name": "", "vorname":"", "strasse":""}


const start = document.querySelector(".start");
start.addEventListener('click', createCard);

const submitAllButton = document.getElementById("submitAll")
submitAllButton.style.visibility = "hidden";

function createCard() {
    counter ++;
    //Destroy previous card
    let input_key = Object.keys(dictInputs)[counter];
    if (counter === 1){
        start.parentNode.removeChild(start);
        submitAllButton.style.visibility = "visible";
        submitAllButton.addEventListener('click', safeToDb);
    }
    //Create new card
    var card = document.createElement('div');
    var input = document.createElement("INPUT");
    var submitButton = document.createElement("button");
    input.setAttribute("type", "text");
    input.setAttribute("id", "input");
    input.setAttribute("placeholder", input_key);
    input.setAttribute("class", "input")
    submitButton.setAttribute("class", "button")
    submitButton.addEventListener('click', addToDict);
    submitButton.innerHTML = counter;
    //Create Back Button if not first card
    if (counter > 1){
        let previousCard = document.getElementById(counter-1)
        previousCard.parentNode.removeChild(previousCard)
        var backButton = document.createElement("button")
        backButton.setAttribute("class", "button");
        backButton.addEventListener('click', lastCard);
        backButton.innerHTML = "back";
        card.appendChild(backButton)

    }
    card.appendChild(input);
    card.appendChild(submitButton);
    card.setAttribute("id", counter);
    card.setAttribute("class", "card");
    document.body.appendChild(card);
};

function safeToDb() {
    submitAllButton.innerHTML = "submit"
    var submitForm = document.getElementById("form") //createElement("form")
    submitForm.setAttribute("id", "submitForm")
    submitForm.setAttribute("name", "submitForm")
    for (var x in dictInputs) {
        var submitInput = document.createElement("input")
        submitInput.setAttribute("name", x)
        submitInput.setAttribute("value",dictInputs[x]);
        //submitInput.setAttribute("hidden");
        submitForm.appendChild(submitInput)
    }
   // document.body.appendChild(submitForm)
    //var inputsJson = JSON.stringify(dictInputs);
    // send to server
    alert("Your Data is safe now");
};


//View last Card
function lastCard(){
    counter --;
    //Destroy previous card
    if (counter > 0){
        let previousCard = document.getElementById(counter+1)
        previousCard.parentNode.removeChild(previousCard)
    }
    //Create old card
    let input_key = Object.keys(dictInputs)[counter];
    var card = document.createElement('div');
    var input = document.createElement("INPUT");
    var submitButton = document.createElement("button");
    input.setAttribute("type", "text");
    input.setAttribute("id", "input");
    input.setAttribute("placeholder", input_key);
    input.setAttribute("value",dictInputs[input_key]);
    submitButton.setAttribute("class", "button")
    submitButton.addEventListener('click', addToDict);
    submitButton.innerHTML = counter;
    //Create Back Button if not first card
    if (counter > 1){
        var backButton = document.createElement("button")
        backButton.setAttribute("class", "button");
        backButton.addEventListener('click', lastCard);
        backButton.innerHTML = "back";
        card.appendChild(backButton)
    }
    card.appendChild(input);
    card.appendChild(submitButton);
    card.setAttribute("id", counter);
    card.className = "card";
    document.body.appendChild(card);
};

//Add Value to Object
function addToDict(){
    let input_key = Object.keys(dictInputs)[counter];
    var input = document.getElementById("input");  
    dictInputs[input_key] = input.value;
    var form = document.getElementById("form")
    var safeInput = document.createElement("INPUT");
    safeInput.setAttribute("type", "text")
    createCard();

};
});


/*
!!!dictInputs - "name" - not in form!!!
3. submit variables to backend
5. create cards and visuable feedback
6. create info button
7. create progress bar
*/