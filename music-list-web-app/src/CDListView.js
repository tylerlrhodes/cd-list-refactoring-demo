import React, { Component } from 'react'




const PaginateComponent = (props) => {
  const {totalPages, currentPage, onPageChange} = props;

  let start = 1
  if (currentPage < 4) {
    start = 1
  }
  else if (currentPage % 3 === 0) {
    start = currentPage - 2
  }
  else {
    start = currentPage - (currentPage % 3) + 1
  }
  //console.log("start: " + start + " total pages: " + totalPages)
  const pages = [];
  for (let i = start; 
       i < start + 3 &&
       i <= totalPages; 
       i++) {
    let active = i === currentPage ? " active" : ""
    pages.push(<li className={"page-item" + active}>
      <button className="page-link" href="/GetCDs"
       onClick={() => { onPageChange(i) }}>{i}</button></li>)
  }
  // 
  // need total items
  // items per page
  // current page
  // calc if previous or next should be active
  // calculate what numbers to show
  const nextDisabled = (currentPage < totalPages ? false : true)
  const prevDisabled = (currentPage - 1 === 0 ? true : false)
  return <div>
    <nav aria-label="Page navigation example">
      {/* <span>{currentPage}</span><br /> */}
      <ul className="pagination">
        <li className={"page-item" + (prevDisabled ? " disabled" : "")}>
          <button disabled={prevDisabled} className="page-link" 
           onClick={() => onPageChange(currentPage - 1)}>Previous</button></li>
        {pages}
        <li className={"page-item " + (nextDisabled ? "disabled" : "")}>
          <button disabled={nextDisabled} className="page-link" 
           onClick={() => onPageChange(currentPage + 1)}>Next</button></li>
      </ul>
    </nav>
  </div>
}

class CDListView extends Component {

  constructor(props) {
    super(props)
    this.pageChange = this.pageChange.bind(this)
  }

  pageChange(page) {
    this.props.onPageChange(page)
  }

  render() {
    return (
      <div className="row">
        <div className="col-12">
          <PaginateComponent totalPages={this.props.totalPages} 
           perPage={this.props.perPage} 
           currentPage={this.props.currentPage}
           onPageChange={(p) => this.pageChange(p)} />
          <table className="table table-bordered">
            <thead className="thead-light">
              <tr>
                <th><span className="btn btn-link">Artist</span></th>
                <th><span className="btn btn-link">Title</span></th>
                <th><span className="btn btn-link">Year</span></th>
              </tr>
            </thead>
            <tbody>
              {this.props.cds
                // .slice((this.state.curPage - 1) * 10, (this.state.curPage - 1) * 10 + 10)
                .map((val, idx) => {
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