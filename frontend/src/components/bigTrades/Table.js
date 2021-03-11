import React from 'react';
import DataTable from 'react-data-table-component';

const columns = [
	{
		name: 'Ticker',
		selector: 'ticker',
		sortable: true
	},
	{
		name: 'Underlying Price', 
		selector: 'underlying_price'
	},
	{
		name: 'Prices',
		selector: 'prices',
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
		name: 'Exp Dates',
		selector: 'exp_dates'
	},
];
function checkEarnings(ticker, earnings) {
	let newTicker = ticker 
	let foundTickers = []
	earnings.forEach( earning => {
		if (earning.ticker == ticker) {
			console.log(earning.ticker)
			console.log('found earnings')
			newTicker = `${earning.ticker} (ER: ${earning.date})` 
			foundTickers.push(ticker)
		} 
	})	
	return newTicker
}
export default function Table(props) {
	const data = props.api;
	console.log(data);
	
	const api = props.api;
	let rows;
	if (Array.isArray(api)) {
		rows = api.map((row) => ({
			ticker: checkEarnings(row.ticker, props.earnings),
			exp_dates: row.exp_dates.join(' / \t'),
			strikes: row.strikes.join(' / \t'),
			volume_oi_ratio: row.volume_oi_ratio.join(' / \t'),
			prices: row.prices.join(' / \t'),
			underlying_price: row.underlying_price
		}));
	}
	console.log(rows);
	return (
		<div>
			<DataTable columns={columns} data={rows} responsive={true} highlightOnHover={true} />
		</div>
	);
}
