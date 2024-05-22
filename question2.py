# find if the given number is a palindrome or not?
str=input("Enter a string:")
if(str==str[::-1]):
  print(f'{str} is a palindrome')
else:
  print("Not a palindrome")
