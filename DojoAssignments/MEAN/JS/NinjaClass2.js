function Ninja(name){
  if(this.health <= 0){
    console.log(this.name + " died!");
  };
  this.name = name;
  this.health = 100;
  var speed = 3;
  var strength = 3;

  var kick = function(target){
    if(target instanceof Ninja){
      console.log(strength);
      target.health -= 15 * strength;
    };
  };

  this.sayName = function(){
    console.log("My ninja name is " + this.name + "!");
  };

  this.showStats = function(){
    console.log("Name: " + this.name + ", Health: " + this.health + ", Speed: " + speed + ", Strength: " + strength);
  };

  this.drinkSake = function(){
    console.log("Kanpai! *sip sip sip*");
    this.health += 10;
  };

  this.punch = function(target){
    if(target instanceof Ninja){
      target.health -= 5;
      console.log(target.name + " was punched by " + this.name + " and lost 5 hp!");
    };
  };
  this.kick = function(target){
    console.log(target.name + " was punched by " + this.name + " and lost " + 15 * strength + " hp");
    kick(target);
  };
};

blueNinja = new Ninja("Kevin");
redNinja = new Ninja("Drew");

redNinja.kick(blueNinja);
blueNinja.showStats();
