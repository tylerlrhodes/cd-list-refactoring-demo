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
    this.state = {cds: [], totalPages: 0, perPage: 10, currentPage: 1}
    this.getCds = this.getCds.bind(this);
  }
  async componentDidMount() {
    await this.getCds();
  }
  async getCds(page) {
    if (page === undefined || isNaN(page))
      page = 1 
    var response = await fetch(GetCDsURL + "/" + (page - 1))
    var results = await response.json()
    //var results = JSON.parse(json)
    this.setState({cds: results.cd_list, 
      currentPage: page,
      totalPages: results.total_pages,
      perPage: results.per_page})
  }
  render() {
    return (
      <div className="App container">
        <header className="App-header">
          <h1>
            Music CD List 1.0
          </h1> 
        </header>
        <CDListView cds={this.state.cds}
         totalPages={this.state.totalPages}
         perPage={this.state.perPage}
         currentPage={this.state.currentPage}
         onPageChange={(p) => this.getCds(p)}>
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
