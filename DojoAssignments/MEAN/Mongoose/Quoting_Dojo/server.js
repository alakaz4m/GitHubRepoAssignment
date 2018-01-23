// Require the Express Module
var express = require('express');
// Create an Express App
var app = express();
// Require body-parser (to receive post data from clients)
var bodyParser = require('body-parser');
// Require Mongoose (to store post data from clients)
var mongoose = require('mongoose');
// Connect to the db
mongoose.connect('mongodb://localhost/quote_db');
mongoose.Promise = global.Promise;
// Integrate body-parser with our App
app.use(bodyParser.urlencoded({ extended: true }));
// Require path
var path = require('path');
// Setting our Static Folder Directory
app.use(express.static(path.join(__dirname, './static')));
// Setting our Views Folder Directory
app.set('views', path.join(__dirname, './views'));
// Setting our View Engine set to EJS

//Creating Quote model
var QuoteSchema = new mongoose.Schema({
 name: {type: String},
 quote: {type: String}
}, {timestamps: true})
// Store the Schema under the name 'Quote'
mongoose.model('Quote', QuoteSchema);
// Retrieve the Schema called 'Quote' and store it to the variable Quote
var quote = mongoose.model('Quote');
app.set('view engine', 'ejs');

// Routes
// Root Request
app.get('/', function(req, res) {
    // This is where we will retrieve the users from the database and include them in the view page we will be rendering.
    res.render('index');
})
// Post Request to /quotes for storing into Quote Model
app.post('/quotes', function(req, res) {
  // Creating new Quote document from the post request
  var newQuote = new quote({name: req.body.name, quote: req.body.quote});
  // Saving newQuote into Quote DB
  newQuote.save(function(err) {
    // Checking for error
    if(err) {
      console.log(err);
    }
    else {
      res.redirect('/quotes');
    }
  });
})
// Get Request to /quotes for reading from Quote Model
app.get('/quotes', function(req, res) {
  quote.find({}, function(err, quotes) {
    res.render('quotes', {content: quotes});
  })
})


// // Add User Request
// app.post('/users', function(req, res) {
//     console.log("POST DATA", req.body);
//     // This is where we would add the user from req.body to the database.
//     res.redirect('/');
// })
// Setting our Server to Listen on Port: 8000
app.listen(8000, function() {
    console.log("listening on port 8000");
})
