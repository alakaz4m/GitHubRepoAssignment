function Deck(){
    //seperated symbols from numbers for ease of use
  var deck = [];
  var shuffled_deck = [];
  var d = [];
  var cards = {
    suites: ["Diamonds", "Hearts", "Spades", "Clubs"],
    values: ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
    };

  this.start = function(){
    console.log("Creating deck...");
    //going through the array and creating suites and deck_of_cards combinations until there are 52 cards total
    for(var i = 0; i < cards.suites.length; i++){
      for(var j = 0; j < cards.values.length; j++){
          deck.push(cards.values[j] + " of " + cards.suites[i])
      }
    }
    return deck;
  }
  this.shuffle = function(){
    for (let s = deck.length - 1; s > 0; s--) {
      var t = Math.floor(Math.random() * (s + 1));
      [deck[s], deck[t]] = [deck[t], deck[s]];
      shuffled_deck.push(deck[s]);
     }
     return shuffled_deck;
   }

  this.deal = function(){
    d.push(shuffled_deck[shuffled_deck.length - 1])
    shuffled_deck.pop();
    return d;
  };
}

function Player(name, Deck){
  var playerName = name;
  var hand = [];
  this.deal = function(){
    if(Deck){
      hand.push(Deck.deal());
    }
  }
}

var newDeck = new Deck();
newDeck.start();
