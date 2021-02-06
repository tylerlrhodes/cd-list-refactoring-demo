// import logo from './logo.svg';
import React, { Component } from 'react'
import './App.css';
import 'bootstrap/dist/css/bootstrap.css'
import CDListManagementForm from './CDListManagementForm'
import CDListView from './CDListView'
import { GetCDsURL } from './global'

class App extends Component {
  constructor(props){
    super(props);
    this.state = {cds: []}
    this.getCds = this.getCds.bind(this);
  }
  async componentDidMount() {
    await this.getCds();
  }
  async getCds() {
    var response = await fetch(GetCDsURL)
    var json = await response.json()
    this.setState({cds: json})
  }
  render() {
    return (
      <div className="App container">
        <header className="App-header">
          <h1>
            Music CD List 1.0
          </h1> 
        </header>
        <CDListView cds={this.state.cds}>
        </CDListView>
        <h3>Add a CD/Upload or Download list:</h3>
        <CDListManagementForm onUpload={ async () => { await this.getCds() }}
                              onAddCD={async () => { await this.getCds() }}>

        </CDListManagementForm>
      </div>
    );
  }
}

export default App;
