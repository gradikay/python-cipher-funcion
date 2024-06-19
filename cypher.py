# goood
def create_staircase(nums):
  step = 1
  subsets = []
  while len(nums) != 0:
    if len(nums) >= step:
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
    else:
      return False
      
  return subsets
  
def takeEndingNumber(create_staircase):
  subsets = []
  for x in create_staircase:
    subsets.append(x[-1])
  return subsets
  
def u(realNumber, array):
  subsets = ""
  for x in realNumber:
    subsets = subsets + array[x - 1] + " "
  return subsets

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

#def findWord(array, array2):
#  for x in array:
#     array2[]  

myFile = decode_message("file.txt")
number = create_staircase(myFile[0])
endNumbers = takeEndingNumber(number)
message = u(endNumbers, myFile[1])
thi = [[2,"me"],[1,"you"]]
#print(myFile)
#print(number)  
print(endNumbers)
#print(thi[0][1])

