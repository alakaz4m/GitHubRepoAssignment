require_relative 'printer_module' #This line is used to call the printer_modle.rb made previously
class Array #creates a class named Array
  include Printer # adds the method Printer to this instance of class
end #ends class
class String #creates a class named String
  include Printer #adds the method Printer to this instance of class
end #ends class
[1,2,3].print_each_element #[1,2,3] is an Array Class
puts [1,2,3].class # => Array
"Hello".print_each_element # => "H" "e" "l" "l" "o"
