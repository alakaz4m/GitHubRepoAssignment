// let students = [
//     {name: 'Remy', cohort: 'Jan'},
//     {name: 'Genevieve', cohort: 'March'},
//     {name: 'Chuck', cohort: 'Jan'},
//     {name: 'Osmund', cohort: 'June'},
//     {name: 'Nikki', cohort: 'June'},
//     {name: 'Boris', cohort: 'June'}
// ];

// for(let student in students){
//   console.log("Name: " + students[student]['name'] + ", Cohort: " + students[student]['cohort'])
// }

let users = {
    employees: [
        {'first_name':  'Miguel', 'last_name' : 'Jones'},
        {'first_name' : 'Ernie', 'last_name' : 'Bertson'},
        {'first_name' : 'Nora', 'last_name' : 'Lu'},
        {'first_name' : 'Sally', 'last_name' : 'Barkyoumb'}
    ],
    managers: [
       {'first_name' : 'Lillian', 'last_name' : 'Chambers'},
       {'first_name' : 'Gordon', 'last_name' : 'Poe'}
    ]
}

for(let val in users){
  console.log(val.toUpperCase())
  for(var i = 0; i < users[val].length; i++){
    let total = users[val][i]['last_name'].length + users[val][i]['first_name'].length;
    console.log(users[val].indexOf(users[val][i])+1 + " - " + users[val][i]['last_name'].toUpperCase() +", "+ users[val][i]['first_name'].toUpperCase() + " - " + total);
  }
