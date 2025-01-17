function loging(event) {
    event.preventDefault();  // Prevent the default form submission behavior

    let strName = document.getElementById('fname').value;
    //let strLastName = document.getElementById('lname').value;
    let usrPass = document.getElementById('userPass').value;
    //let avatarName = document.getElementById('userAvatarName').value;

    fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: strName,
            password: usrPass,
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => console.log("Response:", data))
    .catch(error => console.error("Error:", error));
};

function singup(){
    let strName = document.getElementById('fname').value;
    let strLastName = document.getElementById('lname').value;
    let usrPass = document.getElementById('userPass').value;
    let avatarName = document.getElementById('userAvatarName').value;

    fetch("http://127.0.0.1:5000/singup", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: strName,
            lastname: strLastName,
            password: usrPass,
            avatar_name : avatarName
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => console.log("Response:", data))
    .catch(error => console.error("Error:", error));
};

function selectBed(event){
    event.preventDefault(); 
    var selectedBed = document.getElementById('selectBed').value
    var selectedRoom = document.getElementById('selectRoom').value
    console.log(selectedRoom, selectedBed)

    fetch("http://127.0.0.1:5000/room", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            bed: selectedBed,
            room: selectedRoom,
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => console.log("Response:", data))
    .catch(error => console.error("Error:", error));
}

function uploadPhoto(event){
    event.preventDefault(); 
 
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];  // Access the first file selected
    
    // Create a FormData object and append the file
    const formData = new FormData();
    formData.append('fileInput', file);

    // Send the file using fetch to a server endpoint
    fetch('http://127.0.0.1:5000/uploadimage', {
        method: 'POST',
        body: formData,
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('File upload failed!');
        }
        return response.json();
    })
    .then(data => {
        alert('File uploaded successfully!');
        console.log('Server Response:', data);
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while uploading the file.');
    });
}

function displayImage(event){
    event.preventDefault(); 

    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];  // Access the first file selected

    if (!file) {
        alert('Please select a file first!');
        return;
    }

    const div2img = document.getElementById('avatarDisplay');
    div2img.innerHTML = ''; // Clear previous image

    var objImage = document.createElement('img');
    objImage.alt = 'Uploaded Image';
    objImage.style.width = '75px';
    objImage.style.height = '75px';
    div2img.appendChild(objImage);

    const fileReader = new FileReader();
    fileReader.onload = function(event) {
        objImage.src = event.target.result; // Correctly set the image source
    };

    fileReader.readAsDataURL(file);

    console.log(file);
}

function uploadPoem(event){
    event.preventDefault();
    
    user_poem = document.getElementById('poemSpace').value
    c_user_id = 1 // Fake user id 
 
    fetch("http://127.0.0.1:5000/updatepoem", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            poem: user_poem,
            user_id: c_user_id
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => console.log("Response:", data))
    .catch(error => console.error("Error:", error));
    
    console.log(user_poem)
}