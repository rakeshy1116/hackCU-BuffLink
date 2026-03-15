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

        var submitButton = document.getElementById('submit-button');
        submitButton.disabled = true;
        submitButton.textContent = 'Sending…';

        var banner = document.getElementById('status-banner');
        banner.style.display = 'none';

        var apiBase = localStorage.getItem('apiBase') || 'http://127.0.0.1:5007';

        fetch(apiBase + '/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        })
        .then(function(response) {
            return response.json().then(function(body) {
                return { ok: response.ok, body: body };
            });
        })
        .then(function(result) {
            if (result.ok) {
                banner.style.background = '#d4edda';
                banner.style.color = '#155724';
                banner.style.border = '1px solid #c3e6cb';
                banner.textContent = '✓ Preferences saved! Matching events will be emailed to you.';
                banner.style.display = 'block';
                setTimeout(function() { window.close(); }, 3000);
            } else {
                var msg = (result.body && result.body.error) ? result.body.error : 'Something went wrong. Please try again.';
                showError(banner, submitButton, msg);
            }
        })
        .catch(function(error) {
            console.error('Error:', error);
            showError(banner, submitButton, 'Could not reach the server. Make sure BuffLink backend is running.');
        });
    });
});

function showError(banner, submitButton, message) {
    banner.style.background = '#f8d7da';
    banner.style.color = '#721c24';
    banner.style.border = '1px solid #f5c6cb';
    banner.textContent = '✗ ' + message;
    banner.style.display = 'block';
    submitButton.disabled = false;
    submitButton.textContent = 'Submit';
}

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