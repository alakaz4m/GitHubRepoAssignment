def test
  puts "You are in the method"
  yield
  puts "You are again back to the method"
  yield
end
test { puts 1+1 }

def chocolate
  puts "This is cool"
  yield
  puts "Way cooler"
end
