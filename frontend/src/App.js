import React from "react"
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

import Table from "./components/table/ApiTables";
import Navbar from "./components/navbar/Navbar";
import Home from "./components/home/Home"

function App() {
  return (
    <Router>
      <React.Fragment>
        <div className="App">
          <Navbar />
          <Switch>
            <Route exact path="/tables" component={Table} />
            <Route exact path="/" component={Table} />
          </Switch>
        </div>
      </React.Fragment>
    </Router>
  );
}

export default App;
