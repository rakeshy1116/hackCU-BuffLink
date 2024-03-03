document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('myForm');
    const textInput = document.getElementById('text');

    var myItems = JSON.parse(localStorage.getItem('checkedItems')) || [];
    loadLocalStorage();
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the form from submitting
        //   var myItems = localStorage.getItem('checkedItems') == null ? [] : localStorage.getItem('checkedItems');
    
        const inputValue = textInput.value;
        if (inputValue === "") {
            alert("Text box cannot be empty!");
            return;
        }
        var emailBox = document.getElementById('exampleInputEmail1');
        var nameBox = document.getElementById('name')
        if(emailBox === ""){
            alert("Email box cannot be empty!");
            return;
        }
        if(nameBox === ""){
            alert("Name box cannot be empty!");
            return;
        }
        localStorage.setItem('email', emailBox.value)
        localStorage.setItem('name', nameBox.value)
        myItems.push(inputValue)
        localStorage.setItem('checkedItems', JSON.stringify(myItems));
        var extractedData = extractCheckBoxData(myItems);
        extractedData.push(inputValue)
        localStorage.setItem('checkedItems', JSON.stringify(extractedData));
        let formData = {
            name: nameBox.value,
            email: emailBox.value,
            text: JSON.stringify(extractedData)
        };
        //document.getElementById('output').textContent = JSON.stringify(formData);

        fetch('http://127.0.0.1:5003/', {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch((error) => {
            console.error('Error:', error);
        });

        var submitButton = document.getElementById('submit-button');
        var originalButtonHTML = submitButton.outerHTML;
      
        // Replace the submit button with the image
        submitButton.outerHTML = '<img id="progress-image" src="buff.png" />';
      
        // Start the animation
        var progressBar = document.getElementById('progress-image');
        progressBar.style.position = 'relative';
        progressBar.style.animation = 'progress 2s linear forwards';
      
        // After 2 seconds, replace the image with the original button
        setTimeout(function() {
          progressBar.outerHTML = originalButtonHTML;
          window.close();
        }, 2000);
    });
});

function extractCheckBoxData(myItems){

    console.log(document.getElementById("chkBox"))
    console.log(myItems)
    var data =[] 
    myItems.forEach(element => {
        if(document.getElementById(element)){
            if(document.getElementById(element).checked)
                data.push(element)
        }
    });
    return data;

    // data = []
    // myItems.forEach(element => {
    //     if(document.getElementById(element).checked)
    //         data.push(element)
    // });

    // return data;
}

function loadLocalStorage(){

    if(localStorage.getItem('email') != null){
        var email = localStorage.getItem('email');
        var emailBox = document.getElementById('exampleInputEmail1')
        emailBox.defaultValue = email;
    }
    if(localStorage.getItem('name') != null){
        var name = localStorage.getItem('name');
        var nameBox = document.getElementById('name')
        nameBox.defaultValue = name;
    }
    var printData = JSON.parse(localStorage.getItem('checkedItems')) || [];
    //document.getElementById('output').textContent = printData;
    printData.forEach(element => {
        createCheckBox(element)
    });
}

function createCheckBox(item){
    const checkboxContainer = document.getElementById("outercheckbox");
    const chkboxDiv = document.createElement("div");
    chkboxDiv.className = "chkbox"; // Assig
    var newCheckbox = document.createElement("input");
    
    // Set attributes for the new checkbox
    newCheckbox.type = "checkbox";
    newCheckbox.id = item;
    newCheckbox.name = item;
    newCheckbox.checked = true;
    
    // Create a label for the checkbox
    var label = document.createElement("label");
    label.htmlFor = item;
    label.appendChild(document.createTextNode(item));

    // Append the new checkbox and label to an existing element in the DOM
    var container = document.getElementById("chkBox");
    chkboxDiv.appendChild(newCheckbox);
    chkboxDiv.appendChild(label);
    checkboxContainer.appendChild(chkboxDiv)
}