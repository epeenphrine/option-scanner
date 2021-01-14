import React, { useState, useEffect } from "react";
import CheckBox from "./CheckBox";
import Tables from "./Tables"
import Table2 from "./Table2"
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
      {/* <Tables api={api}/> */}
      <Table2 api={api} />
    </React.Fragment>
  );
}
