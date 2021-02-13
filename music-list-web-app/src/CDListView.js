import React, { Component } from 'react'




const PaginateComponent = (props) => {
  const {total, perPage, currentPage, onPageChange} = props;
  const totalPages = total / perPage;

  function* startPageGenerator() {
    let begin = 1;
    yield begin;
    while (true) {
      yield begin += perPage;
    }
  }

  var gen = startPageGenerator();

  let potential = gen.next().value;
  while (potential + (perPage - 1) < currentPage) {
    potential = gen.next().value;
  }

  const pages = [];
  for (let i = potential; 
       i < potential + perPage &&
       i <= totalPages + 1; 
       i++) {
    pages.push(<li className="page-item">
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
      <span>{currentPage}</span><br />
      <ul class="pagination">
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
    this.state = { curPage: 1 }
    this.pageChange = this.pageChange.bind(this)
  }

  pageChange(page) {
    this.setState({ curPage: page})
  }

  render() {
    return (
      <div className="row">
        <div className="col-12">
          <PaginateComponent total={this.props.cds.length} perPage={10} currentPage={this.state.curPage}
           onPageChange={this.pageChange} />
          <table className="table table-bordered">
            <thead className="thead-dark">
              <tr>
                <th>Artist</th>
                <th>Title</th>
                <th>Year</th>
              </tr>
            </thead>
            <tbody>
              {this.props.cds
                .slice((this.state.curPage - 1) * 10, (this.state.curPage - 1) * 10 + 10)
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