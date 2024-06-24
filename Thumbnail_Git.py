'''
goal > create script that generates thumbnails

what does the script need?
thumbnail templates
font
font placement
font size

what functions does it need?
let the user choose the thumbnail to create
let the user enter the text they want it to say
'''

#importing packages
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import textwrap

#getting thumbnail jpeg paths
#paths to thumbnail options
thumbnail_1 = "" 
thumbnail_2 = ""
thumbnail_3 = ""
thumbnail_4 = ""
thumbnail_5 = ""
thumbnail_6 = ""

#creating list of thumbnail options
options = ['thumbnail_1', 'thumbnail_2', 'thumbnail_3', 'thumbnail_4', 'thumbnail_5', 'thumbnail_6']

#printing instructions for user
print("this program helps create thumbnails")
print("what thumbnail are you looking to create?")

for option in options:
    print(option)

print("please enter the option you want as you see it")

#getting user choice and building in fail safe
user_choice = input()

while user_choice not in options:
    print("It seems there was a type in your input. Please enter the option you want as it appears.")
    for option in options:
        print(option)
    user_choice = input()

#if statements
if user_choice == 'thumbnail_1':
    thumbnail = thumbnail_1

elif user_choice == 'thumbnail_2':
    thumbnail = thumbnail_2

elif user_choice == 'thumbnail_3':
    thumbnail = thumbnail_3

elif user_choice == 'thumbnail_4':
    thumbnail = thumbnail_4

elif user_choice == 'thumbnail_5':
    thumbnail = thumbnail_5

elif user_choice == 'thumbnail_6':
    thumbnail = thumbnail_6


#getting font file and creating font variable
font_path = "***path to font here***/Fjalla_One/FjallaOne-Regular.ttf"
font = ImageFont.truetype(font_path, 45)

#opening image
img = Image.open(thumbnail)

I1 = ImageDraw.Draw(img)

print("what do you want your thumbnail to say?")

thumbnail_text = input()
thumbnail_text = str(thumbnail_text)

print("your thumbnail will say...")
print(thumbnail_text)
print('is this correct? y or n')

answers = ['y','n']

user_answer = input()

while user_answer not in answers:
    print(thumbnail_text)
    print('is the above text what you want your thumbnail to read? y or n')
    user_answer = input()

while user_answer == 'n':
    print("please enter what you want your thumbnail to day")
    thumbnail_text = input()
    thumbnail_text = str(thumbnail_text)
    print(thumbnail_text)
    print('is the above text what you want your thumbnail to read? y or n')
    user_answer = input()

#creating variable so the text doesn't overrun jpeg
para = textwrap.wrap(thumbnail_text, width = 20)

#creating text on image
pad = 25
current_h = 195
for line in para:
    h = 50 #I1.textsize(line, font=font)
    line_string = str(line)
    I1.text((250, current_h), line, font=font, fill=(28,207,201), anchor='mm', align='center')
    current_h += h + pad

string_ending = thumbnail_text.replace(" ", "_")
string_ending = str(string_ending)

illegal_characters = ['#', '%', '&', '{', '}', '<', '>', '*', '?', ' ', '$', '!', "'", '"', ':', '@', '+', '`', '|', '=']

for i in illegal_characters:
    string_ending = string_ending.replace(i, "_")

save_path = ("***put your save path here***"+ string_ending +".jpg")

print(save_path)

img.save(save_path)

print('done')
