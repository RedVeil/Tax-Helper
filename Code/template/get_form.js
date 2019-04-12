document.addEventListener("DOMContentLoaded",function() {

    let counter = 0
    
    const start = document.querySelector(".start");
    start.addEventListener('click', createButton);

    function createButton(){
        counter ++;
        if (counter === 1){
            start.parentNode.removeChild(start);
        }
        else if (counter > 1){
            let previousButton = document.getElementById(counter-1)
            previousButton.parentNode.removeChild(previousButton)
        }
        var submit = document.createElement("button");
        submit.setAttribute("class", "button");
        submit.setAttribute("id", counter);
        submit.addEventListener('click', createButton);
        submit.innerHTML = counter;
        document.body.appendChild(submit);
        
    };

    /*function printCounter(){
        var paragraphEl = document.createElement('p');
        paragraphEl.textContent = counter;
        document.body.appendChild(paragraphEl);
    }*/

});