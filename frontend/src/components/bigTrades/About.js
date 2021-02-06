import React from 'react'

export default function About() {
    return (
        <React.Fragment>
			<h1 className="display-6 text-center">Big Trades only looks at volume and open interest in call contracts</h1>
			<h1 className="display-6 text-center">It shows only contracts with  ( volume : open interest ) ratio of 4 or higher </h1>
        </React.Fragment>
    )
}
