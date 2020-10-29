print("Title of program: Post Exam Activity bot")
print()
while True:
  description = input("Could you describe how you feel after the examinations?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("Keep smiling. Life is good! You should spread this positivity to others around you! Sprinkle it around like confetti!!")
      counter += 1
    if each_word == "bored":
      feelings_list.append("bored")
      encouragement_list.append("Find something fun to do, like learning a new instrument or catch up with some family time. Or...maybe you can just catch up on sleep too!! 😄")
      counter += 1
    if each_word == "tiring":
      feelings_list.append("tiring")
      encouragement_list.append("Get some sleep. You deserve it after working so hard. Remember, early to bed, early to rise, makes a child healthy, wealthy and wise!! Rest well :)")
      counter += 1
    if each_word == "relieved":
      feelings_list.append("relieved")
      encouragement_list.append("Relax after the stressful examinations. You have done well! You can now do whatever you want! Yay!")
      counter += 1

    if each_word == "dead tired":
      feelings_list.append("dead tired")
      encouragement_list.append("Just find something fun to do, like relax. Or maybe, you should get some sleep and rest your tired body...good night...")
      counter += 1
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("Talk to your friends! They'll know what to do. Or you can talk to your parents. However, remember that happiness is like waves, they will come back someday, so don't feel so down!")
      counter += 1  
      
    if each_word == "annoyed":
      feelings_list.append("annoyed")
      encouragement_list.append("Stop what you are doing and breath in and out. Why not politely asking the person to stop doing what makes you annoyed? If not, you can just ignore him/her and walk away...")
      counter += 1
    if each_word == "useless":
      feelings_list.append("useless")
      encouragement_list.append("You are more useful than annoying ads that companies spend thousands on!! I'm sure someone knows your worth! Stay happy or maybe talk to a friend!")
      counter += 1
    if each_word == "inferior":
      feelings_list.append("inferior")
      encouragement_list.append("Its alright. Although you may feel inferior to some of your other classmates, you shouldn't be comparing yourselves to them and you should work on how to better improve yourself!")
      counter += 1
    if each_word == "disappointed"
      feelings_list.append("disappointed")
      encouragement_list.append("It's natural that you may feel disappointed by your performance this time around, but I'm sure with hard work and determination you can do better next year!")
      counter += 1
      
    if counter == 0:

      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". " + encouragement_list[0] + " Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". " + encouragement + " Hope you feel better :)"

  print()
  print(output)
  print()
