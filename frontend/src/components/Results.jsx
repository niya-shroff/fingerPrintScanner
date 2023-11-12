import './Results.css';
import {BiSolidUserRectangle} from 'react-icons/bi'
import QueryMongo from './QueryMongo'

const Results = () => {

  let name = "Niya Shroff"
  let email = "shroffniya@gmail.com"
  let spire = "3848329932"
  let lastVisited = "Worcestor Dining Hall"

  // const results = QueryMongo()
  // console.log(results)
  // if (results.data != undefined) {
  //   name = results.data.firstName + " " + results.data.lastName
  //   email = results.data.email + " "
  //   spire = results.data.spire + " "
  // }

  return (
    <div>
      <header>
        <h1> UScan Results</h1>
          <BiSolidUserRectangle className='image'/>
      </header>
      <main>
        <div>
          <h3 className='right' > Name: {name} </h3>
          <br/>
          <h3 className='right' > Email Address: {email} </h3>
          <br/>
          <h3 className='right'> SPIRE ID: {spire} </h3>
          <br/>
          <h3 className='right'> Last Visited: {lastVisited} </h3>
        </div>
      </main>
      <body>
      </body>
    </div>
  )
}

export default Results