// This function should return a user object. Does it?
var axios = require('axios');
module.exports.getUser = function(){
  var user = {
    firstName: "Dave",
    lastName: "Bowman",
    occupation: "Astronaut",
    admin: false
  }
  return user;
}

module.exports.getData= function(){
  axios('https://dog.ceo/api/breeds/list/all').then(function(response){
    return(response);
  })
}
