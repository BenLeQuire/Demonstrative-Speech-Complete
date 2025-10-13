const button =document.getElementById("submit-button");

function submit () {
    let cont = false
    let name = document.getElementById("name").value;
    let question = document.getElementById("question").value;
    if(name.length < 1 && question.length < 1) {
        alert("Please enter a name and message");
    }
    else if (name.length < 1) {
        alert("Please enter a name");
    }
    else if (question.length < 1) {
        alert("Please enter a question");
    }
    else{
        //alert("hello, your name is " + name +" and your question is " + question);
        cont = true;
    }
    if (cont) {
        let randNum = Math.floor(Math.random() * 5)
        let output=""

        switch (randNum) {
            case 0:
                output="yes"
                break;
            case 1:
                output="no"
                break;
            case 2:
                output="yuh-huh"
                break;
            case 3:
                output="nuh-uh"
                break;
            case 4:
                output="idfk"
        }
        alert(output);
    }

    //console.log("y");
    //window.open("https://www.example.com")
}

button.addEventListener("click", submit);