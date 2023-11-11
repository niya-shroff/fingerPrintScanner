import axios from 'axios'

const SendFormData = (data) => {
    axios({
        method: "POST",
        url: "http://127.0.0.1:5000",
        data: data,
        withCredentials: false,
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": '*',
          "Access-Control-Allow-Methods": 'PUT, GET, POST, DELETE, OPTIONS',
          "Access-Control-Allow-Headers": 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
          }
      })
        .then(function (response) {
          console.log(response);
        })
        .catch(function (response) {
          console.log(response);
        });
}

export default SendFormData