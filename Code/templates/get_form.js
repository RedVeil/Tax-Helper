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