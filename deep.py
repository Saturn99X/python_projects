# get the user's answer
answer = input("what is the answer to the great question of life, the universe and everything: ")

# generate response
i = 0
while i == 0:
 if answer == "42":
  int(answer)
  print("yes")
  break
 elif answer == "forty-two":
  print("yes")
  break
 elif answer == "forty two":
  print("yes")
  break
 else:
  print("no")
  i = 1
