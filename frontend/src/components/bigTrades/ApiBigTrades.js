import React, {useState, useEffect} from 'react';
import Table from './Table'
import About from './About'
export default function ApiBigTrades() {
	const [ api, setApi ] = useState([]);
	const [ ratio, setRatio] = useState(0.6);
	const [ volume, setVolume ] = useState(500);
	const [ oi, setOi ] = useState(1000);
	const [ table, setTable ] = useState('react-table');
	const [earnings, setEarnings] = useState([])

	// call api on page load
	useEffect(async () => {
		const res = await fetch('https://api.neetcode.com/bigTrades');
		const data = await res.json();

		const res2 = await fetch('https://api.neetcode.com/earningsThisWeek')
		const earningss = await res2.json()
		setApi(data);
		setEarnings(earningss)
	}, []);

	// call api using function based on events
	async function makeReq() {
		const url = `https://api.neetcode.com/bigTrades?ratio=${ratio}&volume=${volume}&openInterest=${oi}`;
		const res = await fetch(url);
		const data = await res.json();
		console.log('make req ran ');
		console.log(url);
		setApi(data);
	}

    return (
        <React.Fragment>
			<About />
            <Table api={api} earnings = {earnings}/>
        </React.Fragment>
    )
}
