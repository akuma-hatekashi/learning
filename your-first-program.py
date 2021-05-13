def say_hi(name):
  if name == '':
    print("you didn't enter your name!")
  else:
    print("hi there...")
    for letter in name:
      print(letter)
      
name = input()
say_hi(name)
