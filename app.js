// A function which returns an object after one second
var getData = function(cb){
  setTimeout(function(){
    var data = {
      data: "Some data",
      moreData: "And more data",
      lastData: true
    }
    cb(data)
  }, 1000)
}




getData(function(data){
  console.log(data)
})
