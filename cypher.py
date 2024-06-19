# This Python Program deciphers a hidden message 
# from a text.
# @author Gradi Kayamba
# @version 06/19/2024

# This function creates a pyramid.
# @value array (array): the array to create a pyramid.
# @return (bool or array): an array of last numbers if it's a pyramid othewise False and exits.
def create_pyramid(array):
  step = 1
  result = []
  while len(array) != 0:
    if len(array) >= step:
      result.append(array[0:step])
      array = array[step:]
      step += 1
    else:
      return False    
  return result
  
# This function finds the number at the end
# of the pyramid line.
# @value fullArray (array): the full array containing the last numbers and strings of the pyramid.
# @return (array): an array containing the last numbers of the pyramid.
def getLastNumbers(array):
  result = []
  for x in array:
    result.append(x[-1])
  return result
  
  
# This function deciphers the message. 
# @value endPyramidArray (array): the array containing the last 
# numbers of the pyramid.
# @value fullArray (array): the full array containing the last 
# numbers and strings of the pyramid.
# @return (str): the deciphered message as a string.
def decipher(array1, array):
  result = ""    
  for y in array1:
      for x in array:
        if(int(x[0]) == y):
          result += x[1]+  " "
            
  return result
  
# This function takes a file and breaks it down to a 2 dimensional
# array of numbers and strings per array.
# @value message_file (file): the file containing the secret message.
# @return (str or bool): the secret message if its a pyramid, otherwise False.
def unpackMessage(message_file):  
  file = open(message_file, "r")
  lines = file.readlines()
  fullArray = []
  numbersOnlyArray = []
  for line in lines:
    newLine = line.strip()
    splitLines = newLine.split()
    fullArray.append(splitLines) # return ["string", "string"]
  for i in fullArray:
    numbersOnlyArray.append(int(i[0])) # return the numbers
    numbersOnlyArray.sort() # sort the numbers
    
  result = create_pyramid(numbersOnlyArray) 
  return [result, fullArray]
  
# This function checks if the file has a hidden message 
# @value message_file (file): the file containing the secret message.
# @return (str): the secret message.  
def decode_message(file):
  unpackedMessage = unpackMessage(file)
  if(unpackedMessage[0] == False):
    return "Not a pyramid"
    
  lastPyramidNumbersArray = getLastNumbers(unpackedMessage[0])
  message = decipher(lastPyramidNumbersArray, unpackedMessage[1])
  
  return message
    
print(decode_message("file.txt"))    
