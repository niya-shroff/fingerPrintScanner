import axios from 'axios'

const SendFormData = (data) => {
    axios({
        method: "post",
        url: "localhost:3000",
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