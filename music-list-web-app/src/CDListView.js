import React, { Component } from 'react'
import Glyphicon from '@strongdm/glyphicon'
import uuid from 'react-uuid'


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
    pages.push(<li key={uuid()} className={"page-item" + active}>
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

const SortHeader = ({name, arrowStatus, sortChangeFn}) => {

  function sortChange() {
    //console.log("sortChangeFn... huh?")
    let newArrowDirection = 
      arrowStatus === 1 ? 2 : 
      arrowStatus === 2 ? 1 : 1

    sortChangeFn(name, newArrowDirection)
  }
  const showArrow = arrowStatus > 0
  const arrow = arrowStatus === 1 ? "arrow-up" : "arrow-down"
  return <span
    className="btn btn-link"
    onClick={() => sortChange()}>
      {name}
    {showArrow && <Glyphicon glyph={arrow} />}
  </span>
}

class CDListView extends Component {

  constructor(props) {
    super(props)
    this.pageChange = this.pageChange.bind(this)
    this.sortChange = this.sortChange.bind(this)
  }

  sortChange(name, arrowStatus) {
    //console.log("CDListView sortChange")
    this.props.onSortChange(name, arrowStatus)
  }

  pageChange(page) {
    this.props.onPageChange(page)
  }

  getArrowStatus(name) {
    //console.log("columnName = " + name + " sortDirection = " + this.props.sortDirection)
    if (this.props.sortColumn.toUpperCase() === name.toUpperCase()) {
      return this.props.sortDirection
    }
    return 0
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
                <th>
                  <SortHeader name="Artist" 
                   arrowStatus={this.getArrowStatus("Artist")}
                   sortChangeFn={this.sortChange}/>
                </th>
                <th>
                  <SortHeader name="Title" 
                   arrowStatus={this.getArrowStatus("title")}
                   sortChangeFn={this.sortChange}/>
                </th>
                <th>
                  <SortHeader name="Year" 
                   arrowStatus={this.getArrowStatus("year")}
                   sortChangeFn={this.sortChange}/>
                </th>
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