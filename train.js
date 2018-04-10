var http = require('http')
var server = http.createServer(function(request, response ){
  response.writeHead(200, {"content-Type" : "text/html" })
  response.write("hello sylke")
  response.end ();

});

server.listen(3000);
console.log("server is listening")
;
