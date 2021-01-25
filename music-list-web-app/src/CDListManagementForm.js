import React, { Component } from 'react'
import 'bootstrap/dist/css/bootstrap.css'
import { UploadCSVFile, DownloadCSVFile, AddCD } from './global'

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
      await fetch(AddCD, {
        method: 'POST',
        cache: 'no-cache',
        headers: {
            'Content-Type':'application/json'
        },
        body: JSON.stringify(this.state)
      });
      this.props.onUpload();
    }
    async downloadFile(event) {
        let res = await fetch(DownloadCSVFile, {
            method: 'GET'
        });
        let blob = await res.blob();
        let file = window.URL.createObjectURL(blob);
        var fileLink = document.createElement('a');
        fileLink.href = file;
        fileLink.download = 'cd_list.csv';
        fileLink.click();
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
                  <input type="button" value="Download list as CSV" 
                         className=""
                         onClick={this.downloadFile}></input>
                </div>
              </div>
              <hr />
              <div className="form-row">
                <div className="form-group col-md-12">
                  <label>Artist</label>
                  <input type="text" value={this.state.artist} className="form-control" 
                         name="artist" onChange={this.handleInputChange} />
                </div>
              </div>
              <div className="form-row">
                <div className="form-group col-md-12">
                  <label>Title</label>
                  <input type="text" value={this.state.title} className="form-control" 
                         name="title" onChange={this.handleInputChange} />
                </div>
              </div>
              <div className="form-row">
                <div className="form-group col-md-3">
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
  
  export default CDListManagementForm;