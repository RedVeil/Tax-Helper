document.addEventListener("DOMContentLoaded",function() {

    let counter = -1
    //get dict-keys from database
    var dictInputs= {"name": "", "vorname":"", "strasse":"","deutsch?":"", "verheiratetGewesen":"","five":"","six":"","seven":""}
    
    
    const start = document.querySelector(".start");
    start.addEventListener('click', createRadio);


    function safeToDb() {
        submitAllButton.innerHTML = "submit"
        var submitForm = document.createElement("form")
        submitForm.setAttribute("id", "submitForm")
        submitForm.setAttribute("name", "submitForm")
        for (var x in dictInputs) {
            var submitInput = document.createElement("input")
            submitInput.setAttribute("name", x)
            submitInput.setAttribute("value",dictInputs[x]);
            //submitInput.setAttribute("hidden");
            submitForm.appendChild(submitInput)
        }
        var userNameInput = document.createElement("input")
        userNameInput.setAttribute("type", "text");
        userNameInput.setAttribute("id", "nameInput");
        var userInputButton = document.createElement("input")
        userInputButton.setAttribute("type", "submit")
        submitForm.appendChild(userNameInput)
        submitForm.appendChild(userInputButton)
        document.body.appendChild(submitForm)
    };




    var request = new XMLHttpRequest();
    request.open('POST', '/my/url', true);
    request.setRequestHeader('Content-Type', '/test; charset=UTF-8');
    request.send(data);



    if(counter===1){
        start.parentNode.removeChild(start);
        submitAllButton.style.visibility = "visible";
        submitAllButton.addEventListener('click', safeToDb);
    }
    else if(counter===4){
        alert("test");
    }



    function createRadio(){
        //Create new card
        var card = document.createElement('div');
        var yesButton = document.createElement("button");
        var noButton = document.createElement("button");
        yesButton.setAttribute("class", "button")
        yesButton.setAttribute("id","input")
        yesButton.innerHTML = "Yes";
        noButton.setAttribute("class", "button")
        noButton.setAttribute("id","input")
        noButton.innerHTML = "No";
        //Create Back Button if not first card
        card.appendChild(yesButton);
        card.appendChild(noButton);
        card.setAttribute("id", counter);
        card.setAttribute("class", "card");
        document.body.appendChild(card);   
    };
});