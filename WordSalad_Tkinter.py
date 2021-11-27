import random
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import tkinter as tk


#1/ Pick random word from a list
#Generate list
word_list = list(open("wordsalad.txt").read().split())
#Pick a random word
secret_word = word_list[random.randint(0,len(word_list)-1)]

#2/ Reorganize letters in a random order
#Put all letters from the secret word in a list
secret_word_letters=[]
for letter in secret_word:
    secret_word_letters=secret_word_letters+[letter]
#Shuffle the list
random.shuffle(secret_word_letters)

#3/ Show picture with possible letters
#Create a list with secret word letters JPG format
list_letters_jpg=[]
for char in secret_word_letters:
    image_char = char+".jpg"
    image_char = str(image_char)
    im = Image.open(image_char)
    list_letters_jpg.append(im)

#Create collage JPG
col = len(secret_word)
x=0
width=54*len(secret_word)
new_im = Image.new('RGB', (width, 67), "white")
for colnb in range(col):
    new_im.paste(list_letters_jpg[colnb],(54*colnb,0))
    x=x+1
new_im.save("collage.jpg")


#4/ Guessing stage, prompt user
#Generate possible answers // Possibility that NONE OF THE ABOVE
answer = secret_word[0]
#print("What is the first letter of the secret word?")

ans1 = secret_word_letters[random.randint(0,len(secret_word_letters)-1)]
ans2 = secret_word_letters[random.randint(0,len(secret_word_letters)-1)]
ans3 = secret_word_letters[random.randint(0,len(secret_word_letters)-1)]

#define check variables
var1 = ans1 == ans2
var2 = ans1 == ans3
var3 = ans2 == ans3

#continue redefine variable as long as repeated
while var1 == True or var2 == True or var3 == True:

    if var1 == True:
        ans1 = secret_word_letters[random.randint(0,len(secret_word_letters)-1)]
        var1 = ans1 == ans2
        var2 = ans1 == ans3
    if var2 == True:
        ans1 = secret_word_letters[random.randint(0,len(secret_word_letters)-1)]
        var1 = ans1 == ans2
        var2 = ans1 == ans3
    if var3 == True:
        ans2 = secret_word_letters[random.randint(0,len(secret_word_letters)-1)]
        var1 = ans1 == ans2
        var3 = ans2 == ans3

#Build answer list and shuffle it
answer_list = [ans1,ans2,ans3]

random.shuffle(answer_list)

option1 = answer_list[0].upper()
option2 = answer_list[1].upper()
option3 = answer_list[2].upper()

#Print possible answers
#print("1.The first letter is "+option1)
#print("2.The first letter is "+option2)
#print("3.The first letter is "+option3)
#print("4.None of the above.")
#print("Use the number corresponding to the desired letter to answer.")

#Show choice box


root = tk.Tk()

v = tk.IntVar()
v.set(1)  # initializing the choice

letter_choice = [
    (option1),
    (option2),
    (option3),
    ("None of the above."),
]

#input from player
def ShowChoice():
    print(v.get())

tk.Label(root,
         text="""What is the first letter of the secret word?""",
         justify = tk.LEFT,
         padx = 20).pack()


for val in letter_choice:
    tk.Radiobutton(root,
                   text=val,
                   indicatoron=0,
                   width=20,
                   padx=20,
                   variable=v,
                   command=ShowChoice,
                   value=val).pack(anchor=tk.W)

root.mainloop()


#Show collage of secret word
plt.imshow(mpimg.imread('collage.jpg'))
plt.ion()
plt.axis("off")
plt.pause(0.001)
plt.show()




#build check list

if player_answer == "0":
    if option1 == answer.upper():
        print("Correct!")
        print("The answer was "+secret_word)
        plt.close()
    else:
        print("Wrong!")
        print("The answer was "+secret_word)
        plt.close()
if player_answer == "1":
    if option2 == answer.upper():
        print("Correct!")
        print("The answer was "+secret_word)
        plt.close()
    else:
        print("Wrong!")
        print("The answer was "+secret_word)
        plt.close()
if player_answer == "2":
    if option3 == answer.upper():
        print("Correct!")
        print("The answer was "+secret_word)
        plt.close()
    else:
        print("Wrong!")
        print("The answer was "+secret_word)
        plt.close()
if player_answer == "3":
    if option1 != answer.upper() and option2 != answer.upper() and option3 != answer.upper():
        print("Correct!")
        print("The answer was "+secret_word)
        plt.close()
    else:
        print("Wrong!")
        print("The answer was "+secret_word)
        plt.close()


#Count trials
#Which letter does it start with?

#Extras:
#1/ Challenge mode with 10 questions and stats at the end
#2/ Free mode with subsequent questions and possibility to chose how many questions
#3/ Restart/Reset button

