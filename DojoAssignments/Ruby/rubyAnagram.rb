class Words
  def yurb word
    puts "\n\nYour original word is #{word}"
    puts "Crushed into fine anagram dust.."
    # array = Array.new
    puts "The word is now #{word.split('').collect! {|n| n}}"
  end

  def initialize
    puts "Please, type in a word so I may turn it into magical anagram dust"
    word = gets
    result = yurb word
    return result
  end
end
word_obj = Words.new
# puts word_obj.yurb "Gold"
