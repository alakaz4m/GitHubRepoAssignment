var express = require('express');
var app = express();
var session = require('express-session')
var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }));
app.use(session({secret: 'imsleepy123'}));
app.use(express.static(__dirname + "/static"));
app.set("views", __dirname + "/views");
app.set("view engine", "ejs");

app.get('/', function(req, res){
  res.render('form');
});

app.post("/submit", function(req, res){
  req.session.name = req.body.name;
  req.session.location = req.body.location;
  req.session.language = req.body.language;
  req.session.comment = req.body.comment;
  res.redirect('/result');
});

app.get("/result", function(req, res){
  console.log(req.session.name);
  var content = {
    name: req.session.name,
    location: req.session.location,
    language: req.session.language,
    comment: req.session.comment
  }
  res.render('result' , content);
});

app.listen(8000, function(){
  console.log('listening 8000');
})
