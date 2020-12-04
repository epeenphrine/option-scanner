import React from "react";
import { BrowserRouter, Route, Link } from "react-router-dom"
 
export default function Navbar() {
  return (
    <div>
      <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <div className="container-fluid">
          <a className="navbar-brand" href="/">
            NEETsignals 
          </a>
        </div>
      </nav>
    </div>
  );
}
