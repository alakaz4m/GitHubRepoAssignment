var path= require('path');
var express = require('express');
var app = express();
var mongoose = require('mongoose');
var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded());
app.set('view engine', 'ejs')
app.set('views', path.join(__dirname, 'views'));
mongoose.connect('mongodb://localhost/owl_db');
var OwlSchema = new mongoose.Schema({
  name: {type: String},
  color: {type: String},
  type: {type: String}
}, {timestamps:true});
mongoose.model('Owl', OwlSchema);
var Owl = mongoose.model('Owl');
app.get('/', function(req, res){
  res.redirect('/owls')
})
app.get('/owls', function(req,res){
  Owl.find({}, function(err, owl) {
    if(err){
      console.log(err);
    }
    else{
      res.render('index', {content: owl});
    }
  })
})
app.get('/owls/:id', function(req, res) {
  Owl.find({id: req.params.id}, function(err, owl) {
    if(err){
      res.redirect('/owls')
    }
    else{
      res.render('read', {content: owl});
    }
  })
})
app.get('/owls/new', function(req, res){
  res.render('new');
})
app.post('/owls', function(req, res){
  var newOwl = new Owl({name: req.body.name, color: req.body.color, type: req.body.type});
  newOwl.save(function(err, newOwl){
    if(err){
      console.log(err);
    }
    else{
      res.redirect('/owls')
    }
  });
})
// app.get('/ninjas', function(req,res){
//   		Ninja.find({}, function(err, ninja){
//   		res.render('<ejs filename>', {<key value>: <object name>});
//   		})
// })
// app.post('/quotes', function(req,res){
//   		var new<Document> = new <Document>({name: req.body.<key value>, content: req.body.<key value>});
//   		new<Document>.save(function(err){
//       		if(err){
//           			console.log("something went wrong")
//           			console.log(err);
//           			res.redirect('/');
//       		}else{
//           			console.log('<something relevent');
//           			res.redirect('/<ejs filename>');
//       		}
//   		})
// })
app.listen(8000, function(){
  console.log("listening on port 8000");
})
