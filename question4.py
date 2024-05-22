#write a program to find the sum of digits of a given number'
num=int(input("Enter a number:"))
sum=0
for i in range(0,num):
 if(num>0):
  r=num%10
  sum=sum+r
  num=num//10
print(sum)
