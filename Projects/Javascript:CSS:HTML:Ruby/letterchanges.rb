def LetterChanges(str)
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    vowels = "aeiou"
    newString = []
    stringarray = str.chars
    stringarray.each do |letter|
      if letter.match(/^[[:alpha:]]$/)
        index = lower.index(letter)
        if vowels.include?(letter)
            newString << (upper[index+1])
        else
            newString << (lower[index + 1])
        end
      else
        newString << letter
      end
    end
    newString.join
    return newString

end

LetterChanges("Argument goes here")
