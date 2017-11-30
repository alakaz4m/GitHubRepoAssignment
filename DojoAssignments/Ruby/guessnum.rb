def guess_num guess
  num = 25
  puts 'you were right!' if guess == num
  puts 'your guess was high' if guess > num
  puts 'your guess was low' if guess < num
end

guess_num 25
