def Collatz_seq(number):
  print(number,end=" ")
  if(number==1):
    print(number//2)

  while(number>1):
    if(number%2==0):
      number=number//2
      print(number,end=" ")
    else:
      number=3*(number)+1
      print(number,end=" ")

number=int(input("Enter number:"))
Collatz_seq(number)