document.addEventListener("DOMContentLoaded",function() {

    let counter = 0
    var dictInputs= {"name": "", "vorname":"", "strasse":""}
    
    const start = document.querySelector(".start");
    start.addEventListener('click', createParagraph);
    
    
    
    function createParagraph() {
        if (counter === 0){
            start.parentNode.removeChild(start)
        }
        var form = document.createElement('form');
        var input = document.createElement("INPUT");
        var submit = document.createElement("button");
        input.setAttribute("type", "text");
        input.setAttribute("id", "input");
        input.setAttribute("placeholder", "Name");
        submit.setAttribute("class", "button");
        submit.setAttribute("value", "submit");
        submit.addEventListener('click', addToDict);
        form.appendChild(input);
        form.appendChild(submit);
        document.body.appendChild(form);
    };

    function addToDict(){
        let input_key = Object.keys(dictInputs)[counter];
        console.log(input_key)
        var input = document.getElementById("input");  
        dictInputs[input_key] = input.value;
        var paragraphEl = document.createElement('p');
        paragraphEl.textContent = dictInputs[input_key];
        document.body.appendChild(paragraphEl);
        counter += 1
        createParagraph();
        //console.log(input_key)
    };
    });
    
    
    /*
    1. move through list of inputs_names with submit of createParagraph
    2. Safe input as variable
    3. submit variables to backend
    4. create back button
    5. create cards and visuable feedback
    6. create info button
    7. create progress bar*/