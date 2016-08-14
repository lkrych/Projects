
def LetterChanges(str)

  # we will replace every letter in the string with the letter following it
  # by first getting the number representation of the letter, adding 1 to it,
  # then converting this new number to a letter using the chr function
  # we also check to see if the character is z and if so we simply convert the z to an a
  converted = str.gsub(/[a-zA-Z]/) do |c|
      if c == 'z' or c == 'Z'
        'a'
      else
        (c.ord + 1).chr
      end
  end

  # we have now successfully converted each letter to the letter following it
  # in the alphabet, and all we need to do now is capitalize the vowels
  return converted.tr!('aeiou', 'AEIOU')

end
