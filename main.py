# Aley and Ron Interactive Quest Game
# 3/15/18 - 3/18/18

#begin game
def introduction():#begin game
  print ""
  print "Press 'enter'."
  answer = raw_input()
  if answer == "":
    print "Your story begins in the middle of the magic woods. You are lost with nothing but the clothes on your back to keep you warm. Your goal is to get back home...no matter what it takes."
    print ""
    camp_walk()
  else:
    print "Incorrect input!"
    introduction()
    
#calls berries() and centaur()    
def camp_walk():#first decision
  print "You've arrived at a crossroads. You can either make camp and rest for the night or you can continue walking."
  print "Type 'camp' or 'continue' to input your decision."
  answer = raw_input()
  if answer == "camp":
    print "You've decided to make camp. You will survive the night."
    print "You wake up the next morning and realize how hungry you are."
    print ""
    berries()
  elif answer == 'continue':
    print ""
    print "You've decided to continue walking. Hours have passed and exhaustion creeps in."
    centaur()
  else:
    print "Incorrect input!"
    camp_walk()
    
#calls ogre() and tools()  
def berries():
  print "After walking for some time, you come across a bush of strange colored berries."
  print "You know there is a possibility that the berries are poisonous. Do you eat them or leave them?"
  print "Type 'eat' or 'leave' to input your decision."
  answer = raw_input()
  if answer == "eat":
    print "After consuming the strangely pigmented berries, you gain super strength. Adrenaline is coursing through your veins and you feel like you could destroy anything."
    ogre()  #meeting the ogre
  elif answer == "leave":
    print "After leaving the berries behind, you decide to try hunting. You must now decide how to hunt. Will you make tools or not?"
    tools()
  else:
    print ""
    print "Incorrect input!"
    berries()
    
#calls train() and failure()  
def centaur():
  print "Suddenly you hear the most thunderous sound you have ever heard in your life. You turn around just as an enormous centaur slams you into the nearest tree."
  print ""
  print "You have a choice to make. Either you fight the ferocious centaur, or you run."
  print "Type 'fight' or 'run' to input your decision."
  answer = raw_input()
  if answer == "fight":
    print "The centaur easily bests you in combat. As you lay in the mud, however, it begins to pity you. The centaur tells you that it admires your courage and offers to train you."
    train()
  elif answer == "run":
    print "You begin to sprint towards an open path. The ogre catches up with you quickly and plucks you from the ground. In a final attempt to save yourself, you plead with the centaur to let you live. Disgusted with your lack of pride, the centaur calls you a coward and tramples you."
    failure()
  else: 
    print "Incorrect input!"
    centaur()
    
#helper that calls landSea()
def train():
  print ""
  print "You end up spending five years learning the art of combat from the centaur. Antusk, the centaur, has taught you all that he knows and it is time for you to decide how you want to head home. Will it be by land, or by sea?"
  landSea()
  
#calls climbTree() and sea()
def landSea():  
  print "Type in 'land' or 'sea' to input your decision."
  answer = raw_input()
  if answer == "land":
    print "You choose an arbitrary direction and try your luck with that path."
    climbTree()
  elif answer == "sea":
    print "You decide to gather material for a boat. After hours spent building an adequate sea vessel, you begin to venture out into the open sea, nervous for what you might find"
    sea()
  else: 
    print "Incorrect input!"
    landSea()

#calls mermaidSociety()    
def sea():
  print ""
  print "You realize that sailing is a lot harder than you thought it would be and your clothing is soaked from all of thimes you fell into the cold ocean. You realize you are lost at sea and begin to believe that the last thing you will see is the endless blue of the ocean. You fall asleep and await the darkness."
  print "Press 'enter' to continue reading."
  answer = raw_input()
  if answer == "":
    #mermaids
    print ""
    print "You wake to cold water splashing your sun-burnt face and are startled to find a mermaid peering at you from under the water. Entranced by her mysterious beauty, you reach out to her. Almost as if understanding, she pulls you into the water and takes you to her kingdom. You feel the crushing weight of the ocean all over you. It becomes almost unbearable until she places a necklace around your neck, giving you the ability to breathe underwater and swim with fish-like grace."
    mermaidSociety()
  else:
    print "Incorrect input!"

#calls decision() and failure()
def mermaidSociety():
  print ""
  print "The mermaid has taken you to an empty throne. She sets you on it and a hoard of mermaids rush toward you. The mermaid that brought you down to the ocean bed asks you if you will do her family the honor of ruling. Type 'yes' or 'no' to input your decision."
  answer = raw_input()
  if answer == "yes":
    print ""
    print "The mermaids erupt in applause and cheers. You have been declared the new ruler of this aquatic society and you spend the next 15 years guiding the mermaid race."
    decision()
  elif answer == "no":
    print ""
    print "The family of mermaids become enraged. They don't even give you time to explain yourself and they charge at you. You feel nothing but pain and see nothing but red bubbles as they devour you for refusing their offer."
    failure()

#calls introduction()
def decision():
  print "Press 'enter' to continue."
  answer = raw_input()
  if answer == "":
    print "After serving the mermaid race well for a decade and a half, it is time to return home. There is nothing more you can do to help the mermaids and you've just been informed that the reign of any leader must only last 15 years at which point the current ruler is eaten and the quest for another begins. The mermaids guide you safely to the shore, thanking you for all you've done for them. They wish you good fortune on your journey home and you begin your journey again."
    introduction()
  else:
    print "Incorrect input!"
    decision()
  
#calls prompt
def failure(): #called whenever death occurs
  print "You are now dead. Good luck in the afterlife."
  prompt()
  
#calls ogrePack() and cottage()
def ogre():
  print ""
  print "You continue searching for the path that leads out of the magical woods when you smell something that makes your skin crawl. You react just fast enough to avoid being ripped apart by a disgustingly green ogre."
  print "You musst quickly decide whether to fight the ogre and risk death or to run."
  print "Type 'fight' or 'run' to input your decision."
  answer = raw_input()
  if answer == "fight":
    print "You bravely stand your ground as the ogre charges towards you. The ogre, confused by your lack of fear, stops right before slamming into you and raspily asks you why you aren't afraid."
    print "Without saying a word, you grab it by the shoulders and rip it apart. You see the light leave the confused ogre's eyes and you feel like you could overcome any obstacle put before you."
    ogrePack()
  elif answer == "run":
    print "Forgetting that you have newly acquired super strength, you decide to run as far away from the ogre as possible."
    print "You run for what seems like days until you stumble across a homely cottage."
    cottage()
  else:
    print "Incorrect input!"
    ogre()
    
#helper that calls failure()  
def ogrePack():
  print ""
  print "Content with your victory, you go in search of something or someone else to quench your thirst for blood. As you're walking, you smell the familiar stench of ogre. As it fills your lungs, you call out to what you suspect is another pitiful ogre."
  print ""
  print "After a few minutes of waiting for the ogre to show its face, a pack of the green devils trudges towards you. They see the ogre head that you've been carrying as a trophy and become enraged. They begin to attack you, ripping the limbs from your body until the only thing you know is pain."
  failure()
  
#calls wolves() and cottage()  
def tools():
  print ""
  print "Type 'yes' to make tools or 'no' to hunt without tools."
  answer = raw_input()
  if answer == "no":
    print "You decide to try your luck with the strength you have left and go out in search of something you can eat."
    print ""
    print "After failing to catch the rabbits and rats that have crossed your path, you decide to sleep for the night. You hear the howling of a pack of wolves and groggily try to make your way up the tree you were leaning on. The wolves hear your attempt at a quick escape and hunt you down."
    wolves()
  elif answer == "yes":
    print "You decide to make a wooden spear and a rock knife. After you've acquired your weapons, you go out in search for small animals to catch. After hours of poking your spear into bushes, you decide to make a trap. The trap you create is simple and sure to work. You fall asleep while waiting. A thud and a squeal wake you; you've caught a rabbit! Happy with your catch, you feast on the rabbit and decide to continue walking in search of a path that leads home."
    cottage()
  else:
    print "Incorrect input!"
    tools()
    
#calls climbTree and witch()    
def cottage():
  print ""
  print "You finally come across a familiar structure, a cottage. Type 'in' to go inside the cottage or 'pass' to continue walking."
  answer = raw_input()
  if answer == "pass":
    print ""
    print "The painful reminder of home urges you to avoid the cottage at all costs. You decide to continue on the faded path."
    climbTree()
  elif answer == "in":
    print "You knock on the door. No one answers and the door creepily creaks open. Despite the eerie atmosphere surrounding the cottage, you go in."
    witch()
  else:
    print "Incorrect input!"
    cottage()
    
#calls climbTree() and landSea()    
def wolves():
  print ""
  print "It is time to decide whether you will fight the wolves or try to run from the pack."
  print "Type 'fight' or 'run' to input your decision."
  answer = raw_input()
  if answer == "fight":
    print "You decide that fighting the wolves is your only chance of survival. You pick up the nearest rocks and launch it toward the pack. The rock hits one of the wolves and only angers the pack more. In a final attempt to save your life, you break off a branch from a tree and swing it at the wolves. The pack hears a yelp in the distance and becomes more interested in the thought of prey that doesn't fight back. They turn and run towards some other helpless animal."
    print ""
    print "You climb up the tree and rest for the night."
    print ""
    print "In the morning, you climb down the tree and continue walking."
    climbTree()
  elif answer == "run":
    print ""
    print "You decide to run from the pack. In order to buy yourself some time before you start running for your life, you pick up the nearest rock and launch it towards the brush behind the wolves. When they turn, you run."
    print ""
    print "They almost reach you when you come across a running river. You quickly jump into the river and let the current take you downstream. They wolves know better than to follow you into the river and they give up their pursuit."
    print ""
    print "After some time, you end up in a lake and swim out to the shore. Thankful to be alive, you decide to focus all your energy into going home."
    landSea()
  else:
    print "Incorrect input!"
    wolves()
    
#calls descent() and river()
def climbTree():
  print ""
  print "You realize that you have been walking for a long time and everything has started to look familiar. You see the tallest tree you have ever seen and think to climb it and orientate yourself."
  print "Type 'climb' to go up the tree regardless of the danger of falling or 'path' to continue on the path."
  answer = raw_input()
  if answer == 'climb':
    print "You decide to climb the tree. On the way up, you begin to see the path you need to take to escape the woods. When you reach the top you see the the road you've been searching for. Filled with hope from knowing which way to go, you start your descent down the tree."
    descent()
  elif answer == 'path':
    print ""
    print "Remembering your fear of heights, you decide to continue walking on the path. You stubbornly continue walking down the faded path for what seems like weeks, stopping to rest when hunger or thirst hit."
    print ""
    river()
  else:
    print "Incorrect input!"
    climbTree()
    
#calls failure()
def descent():
  print ""
  print "The sun is setting and it's becoming harder to see the branches below you. Without the sun to guide your descent, you rely on your memory to know which branches are stable enough to support your weight."
  print ""
  print "Press enter to continue reading."
  answer = raw_input()
  if answer == "":
    print "Suddenly you hear a snap and your hands grip the branch above your head. As you hang helplessly from the branch, you hear the howling of hungry wolves. You begin to feel the fatigue in your muscles as the super strength you gained from the berries fades. The dew on the underbrush calls to you and in an effort to retain the pride you have left, you decide to let go of the branch and plummit toward the open-mouthed wolves."
    failure()
  else:
    print "Incorrect input!"
    descent()
    
#calls helper method, witchFight(), created to shorten witch()  
def witch():
  print ""
  print "As soon as you step into the cottage, the smell of sage and moss travel through your nostrils. You call out 'hello' and wait a few minutes before proceeding to walk inside."
  print "You take a moment to admire the strange concoction held within a bulbous jar when you hear a piercing cackle coming from further in the cottage. Startled, you yell, 'Who goes there?'. No one answers and you walk further into the cottage."
  print ""
  print "As fear takes a hold of you, you think about turning back and leaving the cottage and traveling elsewhere. Before you can make your decision, you become inexplicably paralyzed. A hideous witch comes up behind you and says that when she releases you from her spell, you can either fight her or run."
  witchFight()
  
#calls helper method preRiv(), created to shorten river(), and helper witchAnswer(), created to shorten witch()  
def witchFight():
  print ""
  print "Type 'fight' or 'run' to make your decision."
  answer = raw_input()
  if answer == "fight":
    print "You tell her you wish to fight and she squeals with delight at the thought of killing you and using your parts to make potions and spells."
    print ""
    print "You begin to fight and when you easily knock her off her broom, you realize that the witch is not as strong as she claims to be."
    print "Empowered by this information, you begin to grab the items nearest to your hands and launch them at the monster. You unknowingly pick up and throw deadly potions at the witch and you watch as she dies a painfully slow death."
    preRiv()
  elif answer == "run":
    print "The witch, greatful that she doesn't have to waste potions, spells, and strength to kill you decides that she will help you escape the magic woods."
    witchAnswer()
  else:
    print "Incorrect input!"
    witchFight()
 
#calls river()    
def preRiv():
  print ""
  print "Press 'enter' to continue reading."
  given = raw_input()
  if given == "":
    print ""
    print "After the witch's foul figure dissovles into nothing, you loot her cottage. Luckily, the potions are labeled so you are able to take only the things that will be useful. You finish looting the witch's cottage and step outside. You decide to continue down the path that led you to the cottage."
    river()
  else:
    print "Incorrect input!"
    preRiv()

#calls introduction() and failure()    
def river():
  print ""
  print "You come across a river and realize how parched you actually are. You must now decide whether you will drink from the river and risk ingesting parasites or if you will try to make it back home and hope to avoid dehydration."
  print "Type 'drink' to quench your thirst with river water or 'pass' to continue walking."
  answer = raw_input()
  if answer == "drink":
    print ""
    print "You drink the delicious river water and continue walking. You have unintentionally ingested a parasite! As soon as you stand up, you fall into a deep sleep and awake to find that you are right back where you started."
    introduction()
  elif answer == "pass":
    print ""
    print "You've decided not to take your chances with whatever parasites lurk within the river water and continue walking."
    print ""
    print "You spend hours walking and finally collapse from both exhaustion and dehydration. You realize you're never going to escape the clutches of the magic forest and you give in to the darkness."
    failure()
  else:
    print ""
    print "Incorrect input!"
    river()
    
#helper method to okay game again; calls introduction() and quit()   
def prompt():
  print ""
  print "To play again, type 'again'. Enter anything else to quit."
  answer = raw_input()
  if answer == "again":
    introduction()
  else:
    quit()
    
#calls hitchHike() and failure()
def witchAnswer():
  print "She asks you what your greatest desire is. If it is to go home, type 'home'. If not, take your chances answering the witch."
  answer = raw_input()
  if answer == "home":
    print ""
    print "The witch grants you a potion that when consumed, illuminates the path to the road that will lead you home."
    print "You thank the witch and drink the potion. You now know the way to go and you joyfully leave the cottage, filled with hope that you'll make it home."
    hitchHike()
  else:
    print "The witch becomes infuriated that you took her offer of service as a joke and casts a spell that turns your insides out."
    failure()
    
#calls rides() and river()
def hitchHike():
  print ""
  print "After all that you endured in the magic woods, you finally read a paved road! All that is left now is to decide whether you will try to hitchhike or if you will walk the rest of the way."
  print "Type 'hitch' or 'walk' to input your decision."
  answer = raw_input()
  if answer == "hitch":
    print ""
    print "You decide to trust in luck and wait for someone to drive toward you."
    print "Hours have passed and you've begun to lose hope when, in the distance, you hear the rumbling of an engine. Excited, you run out to the middle of the street and make yourself as large as possible so that what you suspect is a driver will be able to spot you in the woodland darkness."
    rides()
  elif answer == "walk":
    print ""
    river()
  else:
    print "Incorrect input!"
    hitchHike()
    
#calls helper methods oldDeath() and trucker(), used to shorten rides()  
def rides():
  print ""
  print "To your surprise, two drivers pull over to their respective side of the road when they see you. They're both willing to give you a ride so now you must choose between the intimidating truck driver and an old lady with a puppy in the backseat."
  print "Type 'lady' or 'trucker' to input your decision."
  answer = raw_input()
  if answer == "lady":
    print ""
    print "You decide to ride with the old lady. You begin to relax, knowing that you are far away from any danger and you fall asleep. You wake up hours later, shackled to a wet wall. Confused, you cry out for help. The steel door in the front of the rood opens and the old lady who gave you a ride steps in. You begin pleading to be set free."
    print ""
    oldDeath()
  elif answer == "trucker":
    print "Despite the fear you're filled with at the sight of the truck driver, you decide to decline the old lady's offer. Something seemed off about her demeanor... and her puppy."
    trucker()
  else:
    print "Incorrect input!"
    rides()
    
#calls failure()  
def oldDeath():
  print "Press 'enter' to continue reading."
  answer = raw_input()
  if answer == "":
    print "The old lady ominously walks toward you and tells you that she can't. She says, 'I'm sorry. I have to feed him.'"
    print ""
    print "You follow her gaze to the other end of the room and you see the puppy that was in her back seat step out of the darkness. You watch with horror as its shape morphs into something from another world. You cry out once more as it snarls and lunges toward you and then, nothing."
    failure()
  else:
    print "Incorrect input!"
    oldDeath()
    
#calls success()
def trucker():
  print ""
  print "Press 'enter' to continue reading."
  answer = raw_input()
  if answer == "":
    print "The drive home with the trucker is quiet and unexpectedly pleasant. After driving for a couple of hours, the driver delivers you home safely."
    success()
  else:
    print "Incorrect input!"
    trucker()

def success():
  print "You enter your home and head straight for your bedroom. You fall into the most deep sleep you have ever known and when you wake up the next morning, you tell yourself that it was all just a really convoluted dream and go to work."
  prompt()
  
#begin game
introduction()