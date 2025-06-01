function printData() {
    var resohed;

    function sendDataToBackend(data) {
        fetch('/process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
            .then(response => response.json())
            .then(result => {

                // console.log('Backend Response:', result);
                // alert('Received from backend: ' + JSON.stringify(result));
                 console.log(result.result);
                 resohed = result.result;
                 document.getElementsByTagName('h4')[0].innerHTML = resohed;
            }) 
            .catch(error => {
                console.error('Error:', error);
                alert('Error sending data to backend.');
            });

        
    }

    function sendSelectedData() {
        const pregnancies = document.getElementById('pregnancies').value;
        const glucose = document.getElementById('glucose').value;
        const bloodPressure = document.getElementById('bloodPressure').value;
        const skinThickness = document.getElementById('skinThickness').value;
        const insulin = document.getElementById('insulin').value;
        const bmi = document.getElementById('bmi').value;
        const diabetesPedigreeFunction = document.getElementById('diabetesPedigreeFunction').value;
        const age = document.getElementById('age').value;

        if (!pregnancies || !glucose || !bloodPressure || !skinThickness || !insulin || !bmi || !diabetesPedigreeFunction || !age) {
            alert("All fields are required!");
            return;
        }
    

        console.log(pregnancies, glucose, bloodPressure, skinThickness, bmi, diabetesPedigreeFunction, age)
        sendDataToBackend({pregnancies, glucose,bloodPressure,skinThickness, insulin, bmi, diabetesPedigreeFunction, age });
    }
    sendSelectedData()

    // document.getElementsByTagName('h4').innerHMTL = resohed;
}

// function revier1(data) {
//     var storeq1 = data;
//     console.log(storeq1);
// }


function clearData() {
    document.getElementById('pregnancies').value = '';
    document.getElementById('glucose').value = '';
    document.getElementById('bloodPressure').value = '';
    document.getElementById('skinThickness').value = '';
    document.getElementById('insulin').value = '';
    document.getElementById('bmi').value = '';
    document.getElementById('diabetesPedigreeFunction').value = '';
}

