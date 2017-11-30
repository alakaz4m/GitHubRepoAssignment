person1 = {:first_name => "Michael", :last_name => "Kravitz", :age => 19}
person2 = {:first_name => "Henry", :last_name => "Ford", :age => 28}
person1.delete(:age)
person2.empty?
person3 = {}
puts "Has key? " + person3.has_key?(:first_name).to_s
puts "Has value? " + person2.has_value?("Henry").to_s
