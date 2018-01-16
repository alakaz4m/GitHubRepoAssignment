// function zero_negativity(array){
//   for(var i = 0; i < array.length -1; i++){
//     if(array[i] < 0){
//       return false;
//     }
//   }
//   return true;
// }

// let math1 = zero_negativity([1,2,6,3]);
// console.log(math1);

// function is_even(num){
//   if(num % 2 == 0){
//     return true;
//   }
//   else{
//     return false;
//   }
// }

// let math2 = is_even(15);
// console.log(math2);

// function how_many_even(array){
//   var count = 0;
//   for(var i = 0; i < array.length; i++){
//     if(is_even(array[i])){ // if is_even is true, it adds 1 to count
//       count += 1;
//     }
//   }
//   return count;
// }

// let math3 = how_many_even([1,2,3,4,5,6]);
// console.log(math3);

// function create_dummy_array(n){
//   var array = [];
//   for(var i = 0; i < n; i++){
//     var newNum = Math.floor((Math.random() * 100) + 1);
//     array.push(newNum);
//   }
//   return array;
// }

// let math4 = create_dummy_array(10);
// console.log(math4);

// function random_choice(array){
//   var newNum = Math.floor((Math.random() * array.length));
//   var myPick = array[newNum];
//   return myPick;
// }

// let math5 = random_choice([1,2,3,4,5,6,7])
// console.log(math5);
