import React, { Component } from 'react'

class CDListView extends Component {
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

  export default CDListView;