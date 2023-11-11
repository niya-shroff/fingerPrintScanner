import axios from 'axios'

const SendFormData = (data) => {
    axios({
        method: "post",
        url: "http://127.0.0.1:5000",
        data: data,
      })
        .then(function (response) {
          console.log(response);
        })
        .catch(function (response) {
          console.log(response);
        });
}

export default SendFormData