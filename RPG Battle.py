#RPG Battle
#By:Damian M.-H.

import random
from tkinter import*
import tkinter.simpledialog
import tkinter.messagebox 

#create a window
root = Tk()
w = Label(root, text="RPG Batttle Simulator")
w.pack()

#Startup
messagebox.showinfo("Welcome to RPG Battle","Hello, you are playing RPG Battle. In this game you will fight an enemy with" + 
                    " randomly generated stats and weapons along with stats and weapons of your own. On the other hand" +
                    " you both have fixed HP. Good luck.")
name = simpledialog.askstring("Hero's Title","What shall be your hero's name?")                          
hp = 100
equip = 0
eequip = 0
strength = random.randint(10,20)
armor = random.randint(1,10)
weapon = random.randint(1,5)
if weapon == 1:
    equip = "spiked gaunlets"
elif weapon == 2:
    equip = "a dagger"
elif weapon == 3:
    equip = "a longsword"
elif weapon == 4:
    equip = "a battle axe"
elif weapon == 5:
    equip = "a greatsword"
ehp = 100
estrength = random.randint(10,20)
earmor = random.randint(1,10)
eweapon = random.randint(1,5)
if eweapon == 1:
    eequip = "spiked gaunlets"
elif eweapon == 2:
    eequip = "a dagger"
elif eweapon == 3:
    eequip = "a longsword"
elif eweapon == 4:
    eequip = "a battle axe"
elif eweapon == 5:
    eequip = "a greatsword"
        
messagebox.showinfo("Hero Stats"," Your hero, " + name + ", has a strength of " + str(strength) + ", " + str(armor) +
                    " armor, and " + str(equip) + ".")
messagebox.showinfo("Enemy Stats"," Your enemy has a strength of " + str(estrength) + ", " + str(earmor) +
                    " armor, and " + str(eequip) + ".")

messagebox.showinfo("","LET THE FIGHT BEGIN!")

#Fight Startup
messagebox.showinfo("","You are a gladitor by the title of, " + name + ", and are about to begin to fight your new enemy" + 
                    " in a bloody arena")
question = simpledialog.askstring("Fight or Flight","Do you wish to fight your Enemy (yes/no)? ")

while (question != "yes" or question != "no"):
    if question == "no":
        root.destroy()
        messagebox.showinfo(""," You drop your weapon and surender to your enemy...")
        messagebox.showinfo(""," Unfortunately, your enemy is kind of a smelly butt head and kills you on the spot.")
        messagebox.showinfo("","GAME OVER")
    elif question == "yes":
        break

#Combat
attack = 0
eattack = 0
damage = 0
edamage = 0
roll = 0
erol = 0
victory = 0
while(hp >= 0 and ehp >= 0):
    first = random.randint(0,1)
    if first == 0:
        messagebox.showinfo("Attack", name + " strikes...")
        attack = random.randint(0,20)
        if attack >= earmor:
            roll = random.randint(1,10) 
            damage = roll + weapon + ((strength - (strength % 2)) / 2)
            ehp -= damage
            if ehp > 0:
                messagebox.showinfo("Contact",name + "'s blade strikes his foe, dealing " + str(damage) + " damage and" +
                                " leaving the enemy at " + str(ehp) + " Hp.")
            else:
                messagebox.showinfo("Final Blow",name + " strikes his foe and lands the killing blow")
                victory = 1
        else:
            messagebox.showinfo("Miss","But misses his enemy")
            
    else:
        messagebox.showinfo("Attack","Your foe strikes...")
        eattack = random.randint(0,20)
        if eattack >= armor:
            eroll = random.randint(1,10)
            edamage = eroll + eweapon + ((estrength - (estrength % 2)) / 2)
            hp -= edamage
            
            if hp > 0:
                messagebox.showinfo("Contact"," The foe's blade strikes " + name + ", dealing " + str(edamage) + " damage " +
                                " and leaving " + name + " at " + str(hp) + " Hp.")    
            else:
                messagebox.showinfo("Final Blow","The foe strikes " + name + " and lands the killing blow")
                victory = 0
        else:
            messagebox.showinfo("Miss","But misses " + name + ". ")
if victory == 1:
    messagebox.showinfo("Victory!",name + " kills his foe and the crowd goes wild! With this victory, he is " +
                        "able to fight another day")
    messagebox.showinfo("","THE END")
else:
    messagebox.showinfo("Failure","Your enemy lands the final blow, ending your life and career")
    messagebox.showinfo("","GAME OVER")
        
            
        
        
    

    

      
        

        

    
    



                    
