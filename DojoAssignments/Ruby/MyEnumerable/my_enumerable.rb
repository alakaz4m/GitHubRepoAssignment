module MyEnumerable
  def my_each
    for n in 0..self.length
      puts self[n] #value of n index self
    end
  end
end
