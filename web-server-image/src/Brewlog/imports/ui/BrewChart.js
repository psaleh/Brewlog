import React from 'react';
import PropTypes from 'prop-types'
import {LineChart, Line, XAxis, YAxis, Tooltip, Legend} from 'recharts';



export default class BrewChart extends React.Component {

  render() {
    console.log('Chart data', this.props.chartData);
    return (

    	<LineChart width={600} height={300} data={this.props.chartData}
            margin={{top: 5, right: 30, left: 20, bottom: 5}}>
       <XAxis dataKey="time"/>
       <YAxis/>
       <Tooltip/>
       <Legend />
       <Line type="monotone" dataKey="SG" stroke="#8884d8" activeDot={{r: 8}}/>
       <Line type="monotone" dataKey="Temp" stroke="#82ca9d" />
      </LineChart>
    );
  }
}
