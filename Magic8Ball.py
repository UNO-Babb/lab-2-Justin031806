#Magic8Ball.py
#Name:
#Date:
#Assignment:

import random 

def main():
  #Create a list of your responses.
  answers=["not really","sure","okay","Very good","incorrect","try again","almost there","you did it"]
  print("Magic 8 Ball")
  #Prompt the user for their question.


  #Answer question randomly with one of the options from your earlier list.

  num =random.random() #decimal 0-1
  num=num*1000 #number 0-999 with decimals
  num=int(num) # no more decimals
  num=num%8 #0-7
  

  question=input("Ask me a question:")
  print(answers[num])
  


if __name__ == '__main__':
  main()
