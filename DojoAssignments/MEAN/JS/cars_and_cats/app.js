var fs = require('fs');
var http = require('http');
var server = http.createServer(function(request, response){
  if(request.url === "/cars"){
    fs.readFile('./views/cars.html', 'utf-8', function(errors, content){
      response.writeHead(200, {'Content-Type': 'text/html'});
      response.write(content);
      response.end();
    });
  }

  else if(request.url === "/images/CommonsBlue.jpg"){
    fs.readFile('./images/CommonsBlue.jpg', function(errors, content){
      response.writeHead(200, {'Content-Type': 'image/jpg'});
      response.write(content);
      response.end();
    });
  }


  else if(request.url === "/images/LexusSC.jpg"){
    fs.readFile('./images/LexusSC.jpg', function(errors, content){
      response.writeHead(200, {'Content-Type': 'image/jpg'});
      response.write(content);
      response.end();
    });
  }

  else if(request.url === "/images/cooliocar.png"){
    fs.readFile('./images/cooliocar.png', function(errors, content){
      response.writeHead(200, {'Content-Type': 'image/png'});
      response.write(content);
      response.end();
    });
  }

  else if(request.url === "/images/redcar.png"){
    fs.readFile('./images/redcar.png', function(errors, content){
      response.writeHead(200, {'Content-Type': 'image/png'});
      response.write(content);
      response.end();
    });
  }

  else if(request.url === "/stylesheets/style.css"){
    fs.readFile('./stylesheets/style.css', 'utf-8', function(errors, content){
      response.writeHead(200, {'Content-Type': 'text/css'});
      response.write(content);
      response.end();
    })
  }

  else if(request.url === "/cats"){
    fs.readFile('./views/cats.html', 'utf-8', function(errors, content){
      response.writeHead(200, {'Content-Type': 'text/html'});
      response.write(content);
      response.end();
    });
  }

  else {
    response.writeHead(404);
    response.end('File not found!!!');
  }

}); // end of createServer function

server.listen(1337);
console.log("Running in localhost at port 1337");
