import React from 'react';
import DataTable from 'react-data-table-component';

const columns = [
	{
		name: 'Ticker',
		selector: 'ticker',
		sortable: true
	},
	{
		name: 'Volume Oi Ratio',
		selector: 'volume_oi_ratio',
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
		name: 'Exp Dates',
		selector: 'exp_dates'
	}
];
export default function Table(props) {
	const data = props.api;
	console.log(data);

	const api = props.api;
	let rows;
	if (Array.isArray(api)) {
		rows = api.map((row) => ({
			ticker: row.ticker,
			exp_dates: row.exp_dates.join(' / \t'),
			strikes: row.strikes.join(' / \t'),
			volume_oi_ratio: row.volume_oi_ratio.join(' / \t'),
			prices: row.prices.join(' / \t')
		}));
	}
	console.log(rows);
	return (
		<div>
			<DataTable columns={columns} data={rows} responsive={true} highlightOnHover={true} />
		</div>
	);
}