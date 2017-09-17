import React from 'react';
import ReactDOM from 'react-dom';
import {Meteor} from 'meteor/meteor';
import {Tracker} from 'meteor/tracker';

import App from '../imports/ui/App'
import {BrewData} from '../imports/api/brewdata'

Meteor.startup(() => {
   Tracker.autorun(() => {
    let data = BrewData.find().fetch();
    let title = 'Brew Log';
    let subtitle = 'Created by Paul Saleh';
  ReactDOM.render(<App title={title} subtitle={subtitle} chartData={data}/>, document.getElementById('app'));
  });
});
