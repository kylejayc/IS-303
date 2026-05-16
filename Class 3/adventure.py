hook = "You are walking through a forest with the queen's " \
"precious cargo. You hear a loud thump in the trees to the left of you. " \
"What do you do? A. Run and hide in the forest, risking the cargo's safety. B. Go back the way you came. C. Investigate the noise. "

decision_a = "You hide behind a tree and fall into a reality-warping hole. You land in the desert planet of Tatooine in the Star Wars universe. What do you do? " \
"What do you do? D. Get in the empty podracer in the middle of the desert. E. Call for help with your transponder. F. Commit suicide."

decision_b = "You turn around but notice a bounty hunter that's been on your trail the whole time. They are obviously armed. " \
"What do you do? G. H. I."

decision_c = "You investigate the mysterious thump and discover a seemingly harmless young womp rat that had fallen from a branch, when suddenly, an old man appears behind you. He apologizes and says the womp rat is his pet and he had lost track of him. " \
"As a form of apology for his trouble. He asks if he can grant you any favor you could possibly imagine. Do you J. Tell him to go away. K. Ask him what he's doing on this planet. L. Draw your weapon. "

decision = input(hook)    #Collect decision from user
decision = decision.upper()


#Write what happens when you choose...
if decision == "A": 
    decision_2 = input(decision_a)
elif decision == "B": 
    decision_2 = input(decision_b)
elif decision == "C":
    decision_2 = input(decision_c)
else:
    print("Not a valid option. You are dead.")
   


