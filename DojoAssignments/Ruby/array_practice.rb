array1 = ["shoes", "tofu", 3, 1, 10, "bacon"]
array2 = ['a','c','d','f','e','b','z']

puts array1
puts '---'
puts array1.at(5)
puts '---'
array1.delete('tofu') #deletes tofu
puts array1.reverse #returns the array in reverse order
puts '---'
puts "length of array is #{array1.length}"
puts '---'
puts array2
puts '---'
puts 'array sorted is'
puts array2.sort
puts '---'
puts array2[0,3]
puts '---'
puts array2.shuffle
puts '---'
puts array1.join(" and ")
puts '---'
puts array1.insert(array1.length,'chocolate')
puts '---'
puts array1.values_at(0,1,2)
