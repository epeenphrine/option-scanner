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
function checkEarnings(ticker, earnings) {
	let newTicker = ticker 
	let foundTickers = []
	earnings.forEach( earning => {
		if (earning.ticker == ticker) {
			console.log(earning.ticker)
			console.log('found earnings')
			newTicker = `${earning.ticker} (ER: ${earning.date})` 
			foundTickers.push(ticker)
			console.log(newTicker)
		} 
	})	
	return newTicker
}
export default function Table2(props) {
	const data = props.api;

	const api = props.api;
	const earnings = props.earnings
	console.log(data)
	console.log(earnings)
	let rows;
	if (Array.isArray(api)) {
		rows = api.map((row) => (
		{
			ticker: checkEarnings(row.ticker, earnings),
			underlyingPrice: row.underlyingPrice,
			dates: row.dates.join(' / \t'),
			strikes: row.strikes.join(' / \t'),
			goldenRatio: row.goldenRatio.join(' / \t'),
			prices: row.prices.join(' / \t')
		}));

	}
	// let test;
	// if (Array.isArray(earnings)) {
	// 	data.forEach(row => {
	// 		checkEarnings(row.ticker, earnings)
	// 	})

	// }
	console.log(rows);
	return (
		<React.Fragment>
			<div className="">
				<DataTable columns={columns} data={rows} responsive={true} highlightOnHover={true} />
			</div>
		</React.Fragment>
	);
}
