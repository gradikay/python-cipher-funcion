# This function creates a pyramid
# return true if the array is a pyramid
def create_pyramid(array):
  step = 1
  subsets = []
  while len(array) != 0:
    if len(array) >= step:
      subsets.append(array[0:step])
      array = array[step:]
      step += 1
    else:
      return False    
  return subsets
  
# This function finds the number at the end
# of the pyramid line
# returns an array
def endPyramidLine(array):
  subsets = []
  for x in array:
    subsets.append(x[-1])
  return subsets
  
# This function decyphers the message 
def decypher(array1, array):
  subsets = ""    
  for y in array1:
      for x in array:
        if(int(x[0]) == y):
          subsets += x[1]+  " "
            
  return subsets
# This function takes a file and breaks
# it to array of numbers and string based
# on each line
def decode_message(message_file):  
  file = open(message_file, "r")
  lines = file.readlines()
  subsets = []
  newSub = []
  for line in lines:
    good = line.strip()
    yes = good.split()
    subsets.append(yes) # return ["string", "string"]
  for i in subsets:
    newSub.append(int(i[0])) # return the numbers
    newSub.sort() # sort the numbers
  return [newSub,subsets]

myFile = decode_message("file.txt")
number = create_staircase(myFile[0])
endNumbers = takeEndingNumber(number)
message = u(endNumbers, myFile[1])
