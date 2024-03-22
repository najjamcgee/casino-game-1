"""
Name: Najja McGee
Date: July 2nd, 2023
Course: CIS 111
Program Name: Project #1: Casino Games

Algirithim:
1. import random module
2. Create a counter variable that keeps track of the user's winnings 
3. Display "Welcome to the Amazing Nubian's Casino" and the Casino Games with the directions, and assign a number value either  1 through 6
-Straight up bet (single number selection) Bet pays 35 to 1
-Split bet(single number selection, covers number +/- 1) Bet pays 17 to 1
-Street bet (single number selection, covers number + 2 subsequent numbers) Bet pays 11 to 1
-Top bet (Covers any number between 1-18) Bet pays even money.
-Bottom bet (Covers any number between 19-36) Bet pays even money.
-Even/odd bet (Covers all even or odd numbers 1-36) Bet pays even money.

4.Prompt the user to pick a game with the number 1 through 6 and that all bets pay $5 
5. Display it is Spinning the Wheel

6. If 1 is inputed then they have selected the "Straight Up Bet" game
7. During the Staight Up game prompt the user to randomly selct a number between 1 through 36
8. If the random generate number matches the user inputed number  muliply how much they paid by 35 and assign it to its respectable variable
9. Display they won and the amount of money they have won if not display they lost

10. If 2 is inputed then they have selected "Split Bet" game
11. During the "Split Bet" game prompt the user to randomly select a number betweer 1 through 36
12. Then set a range in a if-else statement to where the user number is in the range of +- 1 the number or the actual random number and they win.
13. When the number of how much they paid you will multiply that number by 17
14. Display they won and the amount of money they have won if not display they lost

15. If 3 is inputed then they have selected "Street Bet" game
16. During the "Street Bet" game prompt the user to randomly select a number 1 through 36
17. Then set a range in a if-else statement to where the user number is in the range of + 1, 2, or the random numbers after it.
18. When the number of how much they paid you will multiply that number by 11
19. Display they won and the amount of money they have won if not display they lost

20. If 4 is inputed then they have selected "Top Bet" game
21. During the "Top Bet" game prompt the user to randomly select a number 1 through 37
22. Create a range that only allows numbers 1 through 18 to win
23. If number is between that range the user wins $10
24. Display they won and how much they won if not display they lost

25. If 5 is inputed then they have selected "Bottom Bet" game
26. During the "Bottom Bet" game prompt the user to randomly select a number 1 through 37
27. Create a range that only allows numbers 19 through 36 to win
28. If number is between that range but they're odd the user wins $10
29. Display they won and how much they won if not display they lost

30. If 6 is inputed then they have selected "Even/Odd Bet" game
31. Prompt the user to enter either "odd" or "even"
32. If the number mod 2 is 0 its even
33. If the number mod 2 is 1 its odd
34. If right the user won and win $10
35. Display they won and how much they won if not display they lost

36. Else prompt the user to press enter to Quit if they do not want to play

"""
import random

winning_amount = 0


while True: 
  print("Welcome to the Amazing Nubian's Casino!")
  print()
  print("All bets are $5. You can choose how to place your bet from the following menu: ")
  print()
  print("1. Straight up (single number selection) Bet pays 35 to 1.")
  print("2. Split (single number selection, covers number +/- 1) Bet pays 17 to 1.")
  print("3. Street (single number selection, covers number + 2 subsequent numbers) Bet pays 11 to 1.")
  print("4. Top (Covers any number between 1-18) Bet pays even money.")
  print("5. Bottom (Covers any number between 19-36) Bet pays even money.")
  print("6. Even/odd (Covers all even or odd numbers 1-36) Bet pays even money.")
  print("7. Quit game.")
  print()
  
  user_input = int(input("Enter a game you want to play: "))
  if user_input == 7:
    print("You have ended the game. Thanks for coming!")
    break
  elif user_input == 1:
    print()
    user_bet1 = int(input("Place your bet: "))
    print()
    print("...........Spinning the Wheel...........")
    print()
    user_ran = random.randint(1,36)
    print("Number rolled: ",user_ran)
    print()
    if user_bet1 == user_ran:
      #winnings = user_bet1 * 35
      winnings = 35 * 5
      winning_amount += winnings
      print(f"You Won! Money, Money, Moneey! Your winnings are: ${winning_amount}")
      print()
    else:
      print("Sorry, you lose! Thanks for playing!")
      print()
  elif user_input == 2:
    print()
    user_bet1 = int(input("Place your bet: "))
    print()
    print("...........Spinning the Wheel...........")
    print()
    user_ran = random.randint(1,36)
    print()
    print("Number rolled: ", user_ran)
    if (user_bet1 == user_ran) or ( user_bet1 == user_ran + 1) or ( user_bet1 == user_ran - 1):
      #winnings = user_bet1 * 17
      winnings = 17 * 5
      winning_amount += winnings
      print(f"You Won! Money, Money, Moneey! Your winnings are: ${winning_amount}")
      print()
    else:
      print("Sorry, you lose! Thanks for playing!")
      print()
  elif user_input == 3:
    print()
    user_bet1 = int(input("Place your bet: "))
    print()
    print("...........Spinning the Wheel...........")
    print()
    user_ran = random.randint(1,36)
    print("Number rolled: ", user_ran)
    print()
    if (user_bet1 == user_ran) or (user_bet1 == user_ran + 1) or (user_bet1 == user_ran + 2):
      print(f"You Won! Money, Money, Moneey! Your winnings are: ${winning_amount}")
      print()
      #winnings = user_bet1 * 11
      winnings = 11 * 5
      winning_amount += winnings
    else:
      print("Sorry, you lose! Thanks for playing!")
      print()
  elif user_input == 4:
    print()
    user_ran = random.randint(1,36)
    print(f"Number rolled: {user_ran}")
    if user_ran in range(1,19):
      winnings = 10
      winning_amount += winnings
      print(f"You, Won! Money, Money, Moneey! Your winnings are: ${winning_amount}")
      print()
    else:
      print("Sorry, you lose! Thanks for playing!")
      print()
  elif user_input == 5:
    print()
    user_ran = random.randint(1,36)
    print(f"Number rolled: {user_ran}")
    if user_ran in range(19,37):
      winnings = 10
      winning_amount += winnings
      print(f"You, Won! Money, Money, Moneey! Your winnings are: ${winning_amount}")
      print()
    else:
      print("Sorry, you lose! Thanks for playing!")
      print()
  elif user_input == 6:
    print()
    print("...........Spinning the Wheel...........")
    user_ran = random.randint(1,36)
    user_bet1 = str(input("Would you like even or odd?: "))
    print(f"Number rolled: {user_ran}")
    if user_ran % 2== 0 and user_bet1 == "even":
      print()
      winnings = 10
      winning_amount += winnings
      print(f"You, Won! Money, Money, Moneey! Your winnings are: ${winning_amount}")
      print()
    elif user_ran % 2 == 1 and user_bet1 == "odd":
      print()
      winnings = 10
      winning_amount += winnings
      print(f"You, Won! Money, Money, Moneey! Your winnings are: ${winning_amount}")
      print()
    else:
      print("Sorry, you lose! Thanks for playing!")
    
      