var app = require('./app.js');
var mocha = require('mocha');
var chai = require('chai');

//Our first unit test
describe("fetch user", function(){
  var user = app.getUser();
  const getdata = axious.require();

  it("should return an object", function(){
    chai.should();
    user.should.be.a('object')
  })
  it("should return a string", function(){
    chai.should();
    user.lastName.should.be.a('string')
  })

})



describe("Retrieve some JSon", function(){
  let response = app.getData();
  chai.should();
  it("should return valid JSon", function(){
    let valid = validate(response);
    valid.should.be('true')
  })
})
