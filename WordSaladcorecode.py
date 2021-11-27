import random
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


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
print("What is the first letter of the secret word?")

ans1 = secret_word_letters[random.randint(0,len(secret_word_letters)-1)]
ans2 = secret_word_letters[random.randint(0,len(secret_word_letters)-1)]
ans3 = secret_word_letters[random.randint(0,len(secret_word_letters)-1)]
ans4 = secret_word_letters[random.randint(0,len(secret_word_letters)-1)]

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

while ans4 == ans1 or ans4 == ans2 or ans4 == ans3:
    ans4 = secret_word_letters[random.randint(0,len(secret_word_letters)-1)]

#Build answer list and shuffle it
answer_list = [ans1,ans2,ans3, ans4]

random.shuffle(answer_list)

option1 = answer_list[0].upper()
option2 = answer_list[1].upper()
option3 = answer_list[2].upper()
option4 = answer_list[3].upper()

#Print possible answers
print("1.The first letter is "+option1)
print("2.The first letter is "+option2)
print("3.The first letter is "+option3)
print("4.The first letter is "+option4)
print("5.None of the above.")
print("Use the number corresponding to the desired letter to answer.")


#Show collage of secret word
plt.imshow(mpimg.imread('collage.jpg'))
plt.ion()
plt.axis("off")
plt.pause(0.001)
plt.show()

#Player input
player_answer = input()

#build check list
if player_answer == "1":
    if option1 == answer.upper():
        print("Correct!")
        print("The answer was "+secret_word)
        plt.close()
    else:
        print("Wrong!")
        print("The answer was "+secret_word)
        plt.close()
if player_answer == "2":
    if option2 == answer.upper():
        print("Correct!")
        print("The answer was "+secret_word)
        plt.close()
    else:
        print("Wrong!")
        print("The answer was "+secret_word)
        plt.close()
if player_answer == "3":
    if option3 == answer.upper():
        print("Correct!")
        print("The answer was "+secret_word)
        plt.close()
    else:
        print("Wrong!")
        print("The answer was "+secret_word)
        plt.close()
if player_answer == "4":
    if option4 == answer.upper():
        print("Correct!")
        print("The answer was "+secret_word)
        plt.close()
    else:
        print("Wrong!")
        print("The answer was "+secret_word)
        plt.close()
if player_answer == "5":
    if option1 != answer.upper() and option2 != answer.upper() and option3 != answer.upper() and option4 != answer.upper():
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

