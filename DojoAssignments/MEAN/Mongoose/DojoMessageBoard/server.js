var path= require('path');
var express = require('express');
var app = express();
var mongoose = require('mongoose');
var Schema = mongoose.Schema;
var bodyParser = require('body-parser');

app.use(bodyParser.urlencoded());
app.set('view engine', 'ejs')
app.set('views', path.join(__dirname, 'views'));
mongoose.connect('mongodb://localhost/messageBoard');
mongoose.Promise = global.Promise;

const PostSchema = new mongoose.Schema({
  name: {type: String, required: true, minlength: 4},
  message: {type: String, required: true},
  comments: [{type: Schema.Types.ObjectId, ref: 'Comment'}]
}, {timestamps: true});

mongoose.model('Post', PostSchema);
const Post = mongoose.model('Post');

const CommentSchema = new mongoose.Schema({
  _post: {type: Schema.Types.ObjectId, ref: 'Post'},
  name: {type: String, required: true, minlength: 4},
  text: {type: String, required: true},
}, {timestamps: true, usePushEach: true});

mongoose.model('Comment', CommentSchema);
const Comment = mongoose.model('Comment');

app.get('/', function(req, res){
  Post.find({}, function(err, posts){
    if(err){
      console.log('uhoh');
      res.render('index', {errors: err.errors, allPosts: posts})
    }
    else{
      res.render('index', {errors: {}, allPosts: posts})
    }
  })
});

app.post('/create', function(req, res){
  var postInstance = new Post(req.body);
  postInstance.save(function(err){
    if(err){
      res.render('index', {errors: err.errors, allPosts: []});
    }
    else{
      console.log('saved post')
      res.redirect('/');
    }
  })
});

app.post('/create/:id/comment', function(req, res){
  var commentInstance = new Comment(req.body)
  commentInstance._post = req.params.id;
  Post.findOne({_id:})
  commentInstance.save(function(err){
    if(err){
      res.render('index', {errors: err.errors, allPosts: []});
    }
  })
})

app.listen(3000, function(){
      console.log("Listening on port 3000..\n\n\n\n");
})
