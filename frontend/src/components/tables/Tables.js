import React from 'react';

export default function Tables(props) {
	const api = props.api;
	let rows;
	if (Array.isArray(api)) {
		rows = api.map((row) => (
			<tr>
				<th scope="row">{row.ticker}</th>
				<th scope="row">{row.underlyingPrice}</th>
				<td>{row.dates.join(' / \t')}</td>
				<td>{row.strikes.join(' / \t')}</td>
				<td>{row.goldenRatio.join(' / \t')}</td>
				<td>{row.prices.join(' / \t')}</td>
			</tr>
		));
	}
	return (
		<React.Fragment>
			<table class="table">
				<thead>
					<tr>
						<th scope="col">ticker</th>
						<th scope="col">underlyingPrice</th>
						<th scope="col">dates</th>
						<th scope="col">strikes</th>
						<th scope="col">golden ratio</th>
						<th scope="col">prices</th>
					</tr>
				</thead>
				<tbody>{rows}</tbody>
			</table>
		</React.Fragment>
	);
}
