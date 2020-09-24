
import random
import time
global health
s = random.randint(1,50)

###############################################

                # Battle Code
  
###############################################

def battle():
                health = random.randint(10,30)
                enemy = 1
                damage = random.randint(1,10)
                enemyHealth = random.randint(10,50)
                enemyDamage = random.randint(1,5)
                while enemy == 1 and enemyHealth >0:
                                ask = input("You've encountered a monster... Enter 'Run' if you want to try and run, or 'Fight' if you want to attempt the fight: ")
                                if ask == "Fight" or ask == "fight" or ask == "f" or ask == "FIGHT" :
                                                if enemyHealth <= 0:
                                                                print("You win")
                                                                enemy = 0
                                                                walk()
                                                elif health <= 0:
                                                                print("You died")
                                                                credits()
                                                enemyHealth = enemyHealth - damage
                                                time.sleep(0.5)
                                                print ("Enemies health:", enemyHealth)
                                                health = health-enemyDamage
                                                time.sleep(0.5)
                                                print("Your health:", health)
                                elif ask == "Run" or ask == "run" or ask == "r" or ask == "RUN":
                                                Runchance = random.randint(1,10)
                                                if Runchance > 5:
                                                                print("You managed to get away")
                                                                walk()
                                                else:
                                                                print("You failed to get away")
                                                                health = health-enemyDamage
                                                                print("Your health:", health)
                print("You won")
                walk()

###############################################

                # Walking Code
  
###############################################
                
def walk():
                print("Walking")
                time.sleep(1)
                chance = random.randint(1,50)
                if chance >= 25:
                                battle()
                elif chance < 25:
                                print("You're safe, for now...")
                                again = input("Enter 'true' to continue walking or 'false' if you want to stop, the game will close: ")
                                if again == "T" or again == "True" or again == "true" or again == "t" or again == "TRUE" :
                                                print("You walk again")
                                                walk()
                                elif again == "False" or again == "false" or again == "f" or again == "FALSE" :
                                                credits()
                                else:
                                    ans = input("Invalid input. Continue walking?")
                                    if ans == "Yes" or ans == "yes" or ans == "y" or ans == "YES":
                                        walk()
                                    elif ans == "No" or ans == "no" or ans == "n" or ans == "NO":
                                        print("Closing game...")
                                        time.sleep(1)
                                        credits()
                                    else:
                                        print("Your answer wasn't recognised so you continue walking")


                                        walk()

                                                                                                                                                                                                    
###############################################

                # Location Code
  
###############################################

def location():
    location = ['forest' , 'desert' , 'mountains' , 'labyrinth' , 'caves']
    print("Spawning you in a random location")
    time.sleep(1)
    print("Your random spawn location is,", random.choice(location))
    time.sleep(2)
    walk()

###############################################

                # Credits
  
###############################################

def credits():
    print("""This program has been made possible thanks to:
                Sam Marsden
            """)
    exit()
location()


                
