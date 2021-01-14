import React from 'react';
import DataTable from 'react-data-table-component';

// const data = [ { id: 1, title: 'Conan the Barbarian', year: '1982' } ];
const columns = [
	{
		name: 'Ticker',
		selector: 'ticker',
		sortable: true
	},
	{
		name: 'Underlying Price',
		selector: 'underlyingPrice',
		sortable: true
	},
	{
		name: 'Golden Ratio',
		selector: 'goldenRatio',
		sortable: true
	},
	{
		name: 'Strikes',
		selector: 'strikes',
		sortable: true
	},
	{
		name: 'Prices',
		selector: 'prices',
		sortable: true
	},
	{
		name: 'Dates',
		selector: 'dates'
	}
];

export default function Table2(props) {
	const data = props.api;
	console.log(data);

	const api = props.api;
	let rows;
	if (Array.isArray(api)) {
		rows = api.map((row) => ({
			ticker: row.ticker,
			underlyingPrice: row.underlyingPrice,
			dates: row.dates.join(' / \t'),
			strikes: row.strikes.join(' / \t'),
			goldenRatio: row.goldenRatio.join(' / \t'),
			prices: row.prices.join(' / \t')
		}));
	}
	console.log(rows);
	return (
		<React.Fragment>
			<div className="">
				<DataTable title="calendar spreads" columns={columns} data={rows} responsive={true} highlightOnHover={true} />
			</div>
		</React.Fragment>
	);
}
