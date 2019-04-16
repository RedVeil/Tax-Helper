document.addEventListener("DOMContentLoaded",function() {

    let counter = -1
    //get dict-keys from database
    var dictInputs= {"name": "", "vorname":"", "strasse":"","deutsch?":"", "verheiratetGewesen":"","five":"","six":"","seven":"","eight":"","nine":""}
    
    
    const start = document.querySelector(".start");
    start.addEventListener('click', specialEvents);
    
    const submitAllButton = document.getElementById("submitAll")
    submitAllButton.style.visibility = "hidden";
    
    
    
    
    function createCard(x=1) {
        let input_key = Object.keys(dictInputs)[counter];
        //Create new card
        var card = document.createElement('div');
        var input = document.createElement("INPUT");
        var submitButton = document.createElement("button");
        input.setAttribute("type", "text");
        input.setAttribute("id", "input");
        input.setAttribute("placeholder", input_key);
        input.setAttribute("class", "input")
        if (dictInputs[input_key]!== ""){
            input.setAttribute("value", dictInputs[input_key] )
        }
        submitButton.setAttribute("class", "button")
        submitButton.addEventListener('click', addToDict);
        submitButton.innerHTML = counter;
        //Create Back Button if not first card
        if (counter > 0){
            let previousCard = document.getElementById(counter-x)
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
    
    function saveToDb() {
        $.ajax({
            type: "POST",
            url: "{{ url_for("save") }}",
            contentType: "application/json",
            data: JSON.stringify(dictInputs),
            dataType: "json",
            success: function(response) {
                console.log(response);
            },
            error: function(err) {
                console.log(err);
            }
        });
    };
    
    
    //View last Card
    function lastCard(){
        counter --;
        //Destroy previous card
        if (counter > -1){
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
        if (counter > 0){
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
        specialEvents();
    
    };
    
    
    function specialEvents(){
        counter ++;
        if (counter === 0){
            start.parentNode.removeChild(start);
            submitAllButton.style.visibility = "visible";
            submitAllButton.addEventListener('click', saveToDb);
            createCard()
        }
        else if (counter ===12){
            createRadio() //Deutscher? --- safe value in db
        }
        else if (counter ===13){
            createRadio() //Hast du einen Ehepartner?
        }
        else if (counter ===14){
            createRadio() //Hattest du einen Ehepartner davor?
        }
        else if (counter ===49){
            createRadio3() //Steuerberater? - add copyInfo to last next button of Steuerberater
        }
        else if (counter ===62){
            createRadio() //empfängt jemand anderes die dokumente (nur wenn nicht steuerberater)
        }
        else if (counter ===62){ 
            createRadio() //empfängt jemand anderes die dokumente (nur wenn nicht steuerberater)
        }
        /*else if (if deutscher){
            createRadio() empfängt jemand anderes die dokumente (nur wenn nicht steuerberater)
        }*/
        else if (counter ===84){ 
            createRadio() //Hast du ein Atelier/Büro/Werkstatt für deinen Beruf welches nicht in deiner eigenen Wohnung ist?
        }
        /*else if (if not atelier){
            createRadio2() copy adresse
        }*/
        else if (counter ===124){ 
            createRadio() //vorheriges unternehmen besessen?
        }
        /*else if (if not deutscher){
            jump()
        }*/
        /*else if (if not verheiratet){ --- 400 und danach !!!! CHANGE u-beträge/p_beträge reihenfolge!!!!
            jump()
        }*/
        else if (counter ===62){ 
            createRadio() //empfängt jemand anderes die dokumente (nur wenn nicht steuerberater)
        }
        else {
            createCard()
        };
    };
    
    function createRadio(){
        //Create new card
        var card = document.createElement('div');
        var yesButton = document.createElement("button");
        var noButton = document.createElement("button");
        yesButton.setAttribute("class", "button")
        yesButton.setAttribute("id","input")
        yesButton.addEventListener('click', jump);
        yesButton.innerHTML = "Yes";
        noButton.setAttribute("class", "button")
        noButton.setAttribute("id","input")
        noButton.addEventListener('click', specialEvents);
        noButton.innerHTML = "No";
        //Create Back Button if not first card
        if (counter > 0){
            let previousCard = document.getElementById(counter-1)
            previousCard.parentNode.removeChild(previousCard)
        }
        card.appendChild(yesButton);
        card.appendChild(noButton);
        card.setAttribute("id", counter);
        card.setAttribute("class", "card");
        document.body.appendChild(card);   
    };
    
    function createRadio2(){
        //Create new card
        var card = document.createElement('div');
        var yesButton = document.createElement("button");
        var noButton = document.createElement("button");
        yesButton.setAttribute("class", "button")
        yesButton.setAttribute("id","input")
        yesButton.addEventListener('click', copyInfo);
        yesButton.innerHTML = "Yes";
        noButton.setAttribute("class", "button")
        noButton.setAttribute("id","input")
        noButton.addEventListener('click', specialEvents);
        noButton.innerHTML = "No";
        //Create Back Button if not first card
        if (counter > 0){
            let previousCard = document.getElementById(counter-1)
            previousCard.parentNode.removeChild(previousCard)
        }
        card.appendChild(yesButton);
        card.appendChild(noButton);
        card.setAttribute("id", counter);
        card.setAttribute("class", "card");
        document.body.appendChild(card);   
    };
    
    function copyInfo(){
        let nameValue = dictInputs["name"];
        dictInputs["six"] = nameValue;
        console.log(dictInputs["six"])
        specialEvents()
    };
    
    
    function jump(){
        counter += 2;
        createCard(2); 
    };
    /*
    !!!dictInputs - "name" - not in form!!!
    3. submit variables to backend
    5. create cards and visuable feedback
    6. create info button
    7. create progress bar
    */
    });