import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import Table from './components/tables/ApiTables';
import Navbar from './components/navbar/Navbar';
import Home from './components/home/Home';

function App() {
	return (
		<Router>
			<React.Fragment>
				<Navbar />
				<h1 className="display-6 text-center">Quickly find calendar ratios!</h1>
				<h1 className="display-6 text-center">The golden ratio is calculated by short / long leg</h1>
				<Switch>
					<Route exact path="/tables" component={Table} />
					<Route exact path="/" component={Table} />
				</Switch>
			</React.Fragment>
		</Router>
	);
}
export default App;
