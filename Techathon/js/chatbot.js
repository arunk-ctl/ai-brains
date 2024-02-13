
const chatbot = document.getElementById('chatbot');
const conversation = document.getElementById('conversation');
const inputForm = document.getElementById('input-form');
const inputField = document.getElementById('input-field');
let count=0

inputForm.addEventListener('submit', function(event) {
  event.preventDefault();
  const input = inputField.value;
  if(input!== ""){
  inputField.value = '';
  const currentTime = new Date().toLocaleTimeString([], { hour: '2-digit', minute: "2-digit" });

  // Adding user input to conversation
  let message = document.createElement('div');
  message.classList.add('chatbot-message', 'user-message');
  message.innerHTML = `<p class="chatbot-text" sentTime="${currentTime}">${input}</p>`;
  conversation.appendChild(message);

  // Generate chatbot response
  if(count<4)
  {
   process(input, function (error, response) {
  if (error) {
    console.error(error);
  } else {
    console.log(response);
    let response1 = response;
    count+=1;
  // Add chatbot response to conversation
  message = document.createElement('div');
  message.classList.add('chatbot-message','chatbot');
  message.innerHTML = `<p class="chatbot-text" sentTime="${currentTime}">${response1}</p>`;
  conversation.appendChild(message);
    }
});
  }
  else
  {
  const timeout="Hope the issue is not resolved. I will create a ticket for assistance from our executive."
  message = document.createElement('div');
  message.classList.add('chatbot-message','chatbot');
  message.innerHTML = `<p class="chatbot-text" sentTime="${currentTime}">${timeout}</p>`;
  conversation.appendChild(message);

  //Calling ServiceNow API

  getINC(function (error, response) {
  if (error) {
    console.error(error);
  } else {
    console.log(response);
    let response1 = "Your ticket number is:"+response;
  // Add chatbot response to conversation
  message = document.createElement('div');
  message.classList.add('chatbot-message','chatbot');
  message.innerHTML = `<p class="chatbot-text" sentTime="${currentTime}">${response1}</p>`;
  conversation.appendChild(message);
    }
});
  }

  }

  function process(input,callback) {
        if (input !== "") {
            var xhr = new XMLHttpRequest();
            try
            {
            xhr.open("POST", "http://127.0.0.1:5000/api/data", true);
            xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
            xhr.setRequestHeader("Access-Control-Allow-Origin", "http://localhost:63343");
            xhr.onload = function () {
                if (xhr.status === 200) {
                   response= xhr.responseText;
                   callback(null, response);
                } else {
                   callback(new Error('Request failed with status: ' + xhr.status));
                }
            }
            xhr.send(JSON.stringify({ data: input }));
            }
        catch(err){
        alert("Error in server!");
        }

        }
    }

    function getINC(callback){
     var xhr = new XMLHttpRequest();
     xhr.open("POST", "http://127.0.0.1:5000/api/inc", true);
            xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
            xhr.setRequestHeader("Access-Control-Allow-Origin", "http://localhost:63343");
            xhr.onload = function () {
                if (xhr.status === 200) {
                   response= xhr.responseText;
                   callback(null, response);
                } else {
                   callback(new Error('Request failed with status: ' + xhr.status));
                }
            }
            xhr.send();
    }
  });
