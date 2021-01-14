import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import Navbar from './components/navbar/Navbar';
import Home from './components/home/Home';
import CallieSpreads from './components/callieSpreads/ApiCallieSpreads';
import BigTrades from './components/bigTrades/ApiBigTrades'

function App() {
	return (
		<Router>
			<React.Fragment>
				<Navbar />
				<Switch>
					<Route exact path="/bigTrades" component={BigTrades} />
					<Route exact path="/" component={CallieSpreads} />
				</Switch>
			</React.Fragment>
		</Router>
	);
}
export default App;
