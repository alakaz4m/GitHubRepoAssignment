var express = require('express');
var app = express();
var session = require('express-session');
var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }));
app.use(session({secret: 'imsleepy123'}));
app.use(express.static(__dirname + "/static"));
app.set("views" ,__dirname + "/views");
app.set("view engine", "ejs");

app.get('/', function (req, res){
    if(req.session.counter == null){
        req.session.counter = 1;
    }
    else{
      req.session.counter += 1;
    }
    res.render('session', {content: req.session.counter});
});

app.post('/add', function(req, res){
  console.log(req.session.counter)
  req.session.counter += 2;
  res.redirect('/');
});

app.post('/reset', function(req, res){
  console.log('resetting')
  req.session.counter = null;
  res.redirect('/')
})

app.listen(8000, function(){
  console.log("listening port 8000")
})
