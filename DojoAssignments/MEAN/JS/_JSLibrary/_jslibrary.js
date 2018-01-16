var _ = {
  map: function(list, iteratee){
    for(var i = 0; i < list.length; i++){
      list[i] *= iteratee;
    }
    return list;
  },
  reduce: function(list, iteratee,memo){
    //memo is set to 0 if no memo exists
    memo = memo || 0;
    iteratee = iteratee || 0;
    for(var i = 0; i < list.length; i++){
      memo += list[i] + iteratee;
      console.log(i);
      _.reduce(list[i], iteratee, memo);
    }
    return memo;
  },
  find: function(list, predicate){
    predicate = predicate || 2;
    for(var i = 0; i < list.length; i++){
      if(list[i] > predicate){
        return list[i] + " is greater than " + predicate;
      }
      else if(list[i] === predicate){
        return list[i] + " is equal to " + predicate;
      }
    }
    return "No index is greater than " + predicate;
  },
  filter: function(list, predicate){
    predicate = predicate || 2;
    var passed = []
    for(var i = 0; i < list.length; i++){
      if(list[i] > predicate){
        passed.push(list[i]);
      }
    }
    return passed;
  },
  reject: function(list, predicate){
    predicate = predicate || 2;
    var failed = []
    for(var i = 0; i < list.length; i++){
      if(list[i] < predicate){
        failed.push(list[i]);
      }
    }
    return failed;
  }
};
