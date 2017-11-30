# (1..255).each {|i| puts i}
# (1..255).each { |i| puts i if i % 3 == 0}
# sum = 0 #used for ln 4
# puts (0..255).each {|i| puts "New number: #{i.to_s} " + "Sum: #{sum+=i}"}
# x = [1,3,5,7,9,13]
# x.each do |i|
#   puts i
# end
# puts (1..255).max
# x = [1,2,3,4,5,6]
# sum = 0
# x.each do |i|
#   sum += i
# end
# puts average = sum / x.length
# y = []
# (1..255).each {|i| y.push(i) if i % 3 == 0 }
# print y
# def greater_than y
#   array1 = [1,2,3,4,5,6,7]
#   count = 0
#   array1.each {|i| count+= 1 if i > y}
#     return count
# end
# result = greater_than 3
# puts result
# def multiply_array arr
#   array = arr.to_a
#   array.each { |i| array[array.index(i)] = i*i } #<--- I love this algo!!
#   return array
# end
# result = multiply_array [1,3,4,6]
# puts result
# def no_negative arr
#   arr.each{ |i| arr[arr.index(i)] = 0 if i < 0}
#   return arr
# end
# result = no_negative [0,-2,-1,1,2,5,-2]
# print result.to_s + "\n"
# def max_min_avg arr
#   puts "min is #{arr.min}"
#   puts "max is #{arr.max}"
#   sum = 0
#   arr.each do |i|
#   sum += i
# end
#   avg = sum/arr.length
#   puts "average is #{avg}"
# end
# max_min_avg [2,6,3,2,5,-1,4]
