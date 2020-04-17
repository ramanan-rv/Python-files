def isPhoneNumber(text):
  # Required format 012-456-8910
  
  # Eliminate if string is not 12 characters long 
  if len(text) != 12:
    return False
  
  # Eliminate if 4th and 8th characters are not '-'
  if text[3] and text[7] != '-':
    return False
  # Check if rest of the characters are numbers  
  if text[0:3].isdigit() and text[4:7].isdigit() and text[8:12].isdigit():
    return True
  else:
    return False

phone = input("Enter phone number in the format nnn-nnn-nnnn \n") 
print(isPhoneNumber(phone))
