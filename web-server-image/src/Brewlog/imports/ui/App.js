import React from 'react';
import PropTypes from 'prop-types'

import TitleBar from './TitleBar'
import BrewChart from './BrewChart'


export default class App extends React.Component {
  render() {
    return(
      <div>
        <TitleBar title={this.props.title} subtitle={this.props.subtitle}/>
        <BrewChart chartData={this.props.chartData}/>
      </div>
    );
  }
}

App.propTypes = {
  title: PropTypes.string.isRequired,
  subtitle: PropTypes.string.isRequired
}
