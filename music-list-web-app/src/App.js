// import logo from './logo.svg';
import React, { Component } from 'react'
import './App.css';

const CDListEndpoint = process.env.REACT_APP_CDLISTURL;
const GetCDs = CDListEndpoint + "/GetCDS"

export class CDListView extends Component {
  constructor(props) {
    super(props)
    this.state = {cds: []}
  }
  async componentDidMount() {
    var response = await fetch(GetCDs)
    var json = await response.json()
    this.setState({cds: json})
    console.log(this.state)
    this.state.cds.map((val, idx) => {
      console.log(idx + " " + val)
    })
  }
  render() {
    return (
      <table>
        <thead>
          <tr>
            <th>Artist</th>
            <th>Title</th>
            <th>Year</th>
          </tr>
        </thead>
        <tbody>
          {this.state.cds.map((val, idx) => {
            return <tr key={idx}>
              <td>{val[0]}</td>
              <td>{val[1]}</td>
              <td>{val[2]}</td>
            </tr>
          })}
        </tbody>
      </table>
    )
  };
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
          Music CD List 1.0
        </p>
      </header>
      <CDListView>

      </CDListView>
    </div>
  );
}

export default App;
