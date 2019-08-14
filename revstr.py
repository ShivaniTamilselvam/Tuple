def reverseWords(input): 
    inputWords = input.split(" ") 
    inputWords=inputWords[-1::-1] 
    output = ' '.join(inputWords) 
    return output 
if __name__ == "__main__": 
    input = 'geeks quiz practice code'
    print reverseWords(input) 
