import React, { useState, useEffect } from "react";
import CheckBox from "./CheckBox";

export default function ApiTables() {
  const [api, setApi] = useState([]);
  const [days, setDays] = useState(15);
  const [goldenRatio, setGoldenRatio] = useState(0.6);
  const [volume, setVolume] = useState(500);
  const [oi, setOi] = useState(1000);

  // call api on page load
  useEffect(async () => {
    const res = await fetch(
      "https://api.neetcode.com/callieSpreadsLong?days=14"
    );
    const data = await res.json();
    setApi(data);
  }, []);

  // call api using function based on events
  async function makeReq() {
    const url = `https://api.neetcode.com/callieSpreadsLong?days=${days}&goldenRatio=${goldenRatio}&totalVolume=${volume}&openInterest=${oi}`;
    const res = await fetch(url);
    const data = await res.json();
    console.log("make req ran ");
    console.log(url);
    setApi(data);
  }

  // const tickers = api.map((something) => <li>{something.ticker}</li>);
  let rows;
  if (Array.isArray(api)){
    rows = api.map((row) => (
      <tr>
        <th scope="row">{row.ticker}</th>
        <th scope="row">{row.underlyingPrice}</th>
        <td>{row.dates.join(" / \t")}</td>
        <td>{row.strikes.join(" / \t")}</td>
        <td>{row.goldenRatio.join(" / \t")}</td>
        <td>{row.prices.join(" / \t")}</td>
      </tr>
    ));
  }
  // const rows = api.map((row) => (
  //   <tr>
  //     <th scope="row">{row.ticker}</th>
  //     <th scope="row">{row.underlyingPrice}</th>
  //     <td>{row.dates.join(" / \t")}</td>
  //     <td>{row.strikes.join(" / \t")}</td>
  //     <td>{row.goldenRatio.join(" / \t")}</td>
  //     <td>{row.prices.join(" / \t")}</td>
  //   </tr>
  // ));
  // console.log(goldenRatio)
  // console.log(volume)
  // console.log(oi)
  return (
    <React.Fragment>
      <CheckBox
        makeReq={makeReq}
        setDays={setDays}
        days={days}
        setGoldenRatio={setGoldenRatio}
        setVolume={setVolume}
        setOi={setOi}
      />
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
