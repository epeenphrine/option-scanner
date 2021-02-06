import React from 'react';
import { BrowserRouter, Route, Link } from 'react-router-dom';

export default function Navbar() {
	return (
		<div>
			<nav className="navbar navbar-expand-lg navbar-light bg-light">
				<div className="container-fluid">
					<Link className="navbar-brand" href="/">
						NEETsignals
					</Link>
					<button
						className="navbar-toggler"
						type="button"
						data-toggle="collapse"
						dta-target="#navbarNavAltMarkup"
						aria-controls="navbarNavAltMarkup"
						aria-expanded="false"
						aria-label="Toggle navigation"
					>
						<span className="navbar-toggler-icon" />
					</button>
					<div className="collapse navbar-collapse" id="navbarNavAltMarkup">
						<div className="navbar-nav">
							<Link className="nav-item nav-link active" to="/">
								Callie Spreads<span className="sr-only" />
							</Link>
							<Link className="nav-item nav-link" to="bigTrades">
								Big Trades
							</Link>
						</div>
					</div>
				</div>
			</nav>
		</div>
	);
}
