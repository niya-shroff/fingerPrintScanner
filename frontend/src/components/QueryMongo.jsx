import axios from 'axios'

const QueryMongo = () => {
    axios({
        method: "get",
        url: "http://127.0.0.1:5000/api/results",
      })
    .then(function (response) {
        console.log(response);
        return response
    })
    .catch(function (response) {
        console.log(response);
        return response
    });

}

export default QueryMongo