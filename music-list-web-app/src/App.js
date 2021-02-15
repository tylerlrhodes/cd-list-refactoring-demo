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
    this.state = {cds: [], 
                  totalPages: 0, 
                  perPage: 10, 
                  currentPage: 1,
                  sortColumn: "artist",
                  sortDirection: 1}
    this.getCds = this.getCds.bind(this);
    this.sortOrderChange = this.sortOrderChange.bind(this);
  }
  async componentDidMount() {
    await this.getCds();
  }
  async sortOrderChange(name, direction) {
    console.log("App::sortOrderChange name = " + name + " direction = " + direction)
    await this.getCds(this.state.currentPage, name, direction)
  }
  async getCds(page, sortColumn, sortDirection) {
    if (page === undefined || isNaN(page))
      page = 1 
    if (sortColumn === undefined || sortColumn === "")
      sortColumn = this.state.sortColumn
    if(sortDirection === undefined)
      sortDirection = this.state.sortDirection
    var response = await fetch(GetCDsURL + "/" + (page - 1) + "/" + sortColumn + "/" + sortDirection)
    var results = await response.json()
    //var results = JSON.parse(json)
    this.setState({cds: results.cd_list, 
      currentPage: page,
      totalPages: results.total_pages,
      perPage: results.per_page,
      sortColumn: results.sort_column,
      sortDirection: results.sort_direction})
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
         sortColumn={this.state.sortColumn}
         sortDirection={this.state.sortDirection}     
         totalPages={this.state.totalPages}
         perPage={this.state.perPage}
         currentPage={this.state.currentPage}
         onSortChange={this.sortOrderChange}
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
