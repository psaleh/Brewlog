import { Meteor } from 'meteor/meteor';
import {BrewData} from '../imports/api/brewdata';

Meteor.startup(() => {
  // code to run on server at startup


  //  Meteor.publish('brewdata.public', function(){
  //    return Brewdata.find();
  //  });
  let data = BrewData.find().fetch();
  console.log(data);

});
