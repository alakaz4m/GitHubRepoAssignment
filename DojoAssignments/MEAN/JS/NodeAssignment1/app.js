var fs = require('fs');
var http = require('http');
var server = http.createServer(function(request, response){
  if(request.url === "/"){
    fs.readFile('pages/index.html', 'utf-8', function (errors, content){
      response.writeHead(200, {'Content-Type': 'text/html'});
      response.write(content);
      response.end();
    })
  }

  else if(request.url === "/ninjas"){
    fs.readFile('pages/ninjas.html', 'utf-8', function(errors, content){
      response.writeHead(200, {'Content-Type': 'text/html'});
      response.write(content);
      response.end();
    })
  }

  else if(request.url === "/dojos/new"){
    fs.readFile('pages/dojos.html', 'utf-8', function(errors, content){
      response.writeHead(200, {'Content-Type': 'text/html'});
      response.write(content);
      response.end();
    })
  }

  else {
    response.writeHead(404);
    response.end('File not found!!!');
  }

}); // end of createServer function

server.listen(1337);
console.log("Running in localhost at port 1337");
