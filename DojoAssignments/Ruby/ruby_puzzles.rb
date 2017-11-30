# array = [3,5,1,2,7,9,8,13,25,32]
# sum = 0
# array.each do |i|
#   sum += i
# end
# puts sum
# puts array.find_all {|num| num > 10}
#
# array_name = ["John", "KB", "Oliver", "Cory", "Matthew","Christopher"]
# puts array_name.shuffle.find_all {|word| word.length > 5}
# array_alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y"]
# array_beta = ["y","z"]
# array_whole = (array_alpha << array_beta).flatten.shuffle
# puts "first letter is #{array_whole.first} and last letter is #{array_whole.last}"
# puts (55).upto(100).to_a.shuffle.take(10).sort
# letter = Array.new
# 5.times {letter << (65+rand(26)).chr}
# print letter
# print "\n"
# words_arr = Array.new
# 10.times do
#   string = ""
#   5.times {string << (rand(65..90)).chr}
#   words_arr << string
# end
# print words_arr
# print "\n"
