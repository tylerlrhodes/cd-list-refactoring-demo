// import logo from './logo.svg';
import React, { Component } from 'react'
import './App.css';
import 'bootstrap/dist/css/bootstrap.css'

const CDListEndpoint = process.env.REACT_APP_CDLISTURL;
const GetCDs = CDListEndpoint + "/GetCDS"
const UploadCSVFile = CDListEndpoint + "/UploadCSV"

export class CDListView extends Component {
  constructor(props) {
    super(props)
    this.state = {cds: props.cds || []};
  }
  render() {
    return (
      <div className="row">
        <div className="col-12">
          <table className="table table-bordered">
            <thead className="thead-dark">
              <tr>
                <th>Artist</th>
                <th>Title</th>
                <th>Year</th>
              </tr>
            </thead>
            <tbody>
              {this.props.cds.map((val, idx) => {
                return <tr key={idx}>
                  <td>{val[0]}</td>
                  <td>{val[1]}</td>
                  <td>{val[2]}</td>
                </tr>
              })}
            </tbody>
          </table>
        </div>
      </div>
    )
  };
}

class CDListManagementForm extends Component {
  constructor(props){
    super(props);
    this.state = {artist: '',
                  title: '',
                  year: 0};
    this.handleSubmit = this.handleSubmit.bind(this);
    this.uploadFile = this.uploadFile.bind(this);
    this.handleInputChange = this.handleInputChange.bind(this);
  }
  handleInputChange(event) {
    const target = event.target;
    switch (target.name) {
      case "artist":
        this.setState({artist: target.value});
        break;
      case "title":
        this.setState({title: target.value});
        break;
      case "year":
        this.setState({year: target.value})
        break;
      default:
        break;
    }
  }
  async handleSubmit(event) {
    event.preventDefault();
    console.log(this.state.artist);
    console.log(this.state.title);
    console.log(this.state.year);
  }
  async uploadFile(event) {
    let upload = document.getElementById("uploadFile");
    if (upload === undefined || upload === null ||
        upload.files.length === 0) {
      console.error("No file selected!");
      return;
    }
    var formData = new FormData();
    formData.append('csvfile', upload.files[0]);

    await fetch(UploadCSVFile, {
      method: 'POST',
      header: {
        "Content-Type": "text/csv"
      },
      body: formData
    })
    this.props.onUpload();
  }
  render() {
    return (
      <div className="row">
        <div className="col-md-6">
          <hr />
          <form className="form-horizontal" onSubmit={this.handleSubmit}>
            <div className="form-row mb-3">
              <div className="input-group">
                  <input type="file" className="" id="uploadFile" />
              </div>
            </div>
            <div className="form-row mb-3">
              <div className = "input-group">
                  <input type="button" 
                         value="Upload selected file (replaces list on server)..." 
                         className=""
                         onClick={this.uploadFile}></input>
              </div>
            </div>
            <div className="form-row">
              <div className="input-group mb-3">
                <input type="button" value="Download list as CSV" className=""></input>
              </div>
            </div>
            <hr />
            <div className="form-row">
              <div className="form-group col-md-6">
                <label>Artist</label>
                <input type="text" value={this.state.artist} className="form-control" 
                       name="artist" onChange={this.handleInputChange} />
              </div>
            </div>
            <div className="form-row">
              <div className="form-group col-md-5">
                <label>Title</label>
                <input type="text" value={this.state.title} className="form-control" 
                       name="title" onChange={this.handleInputChange} />
              </div>
            </div>
            <div className="form-row">
              <div className="form-group col-md-2">
                <label>Year</label>
                <input type="text" value={this.state.year} className="form-control" 
                       name="year" onChange={this.handleInputChange} />
              </div>
            </div>
            <div className="form-row">
              <div className="form-group col-md-4">
                <button type="submit" className="btn btn-primary">Add CD</button>
              </div>
            </div>       
          </form> 
        </div>
      </div>
    )
  }
}

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
    var response = await fetch(GetCDs)
    var json = await response.json()
    this.setState({cds: json})
    console.log(this.state)
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
