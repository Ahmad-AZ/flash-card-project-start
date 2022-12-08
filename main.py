import random
from tkinter import *
import pandas as pd
from os.path import exists


random_word ={}
data_fr = {}
BACKGROUND_COLOR = "#B1DDC6"
#

#---------------------------- Read Data ------------------

try:
    data_fr =pd.read_csv('data/words_to_learn.csv')

except FileNotFoundError:
    data_fr =pd.read_csv('data/german_words.csv')

finally:
    data_fr = data_fr.to_dict(orient='records')



#------------------------ Button Func --------------------------
def right_words():
    global random_word
    data_fr.remove(random_word)
    data = pd.DataFrame(data_fr)
    data.to_csv('data/words_to_learn.csv',index=False)
    next_card()



def next_card():
    global random_word, flip_timer
    window.after_cancel(flip_timer) # will invalidate the timer after clicking one of the buttons
    random_word = random.choice(data_fr)
    canvas.itemconfigure(language, text= 'German', fill='black')
    canvas.itemconfigure(word, text=random_word['German'], fill='black')
    canvas.itemconfigure(card_image, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

#-------------------------- change Canvas Image ---------------------

def flip_card():

    canvas.itemconfig(language, text= 'Arabic', fill= 'white')
    canvas.itemconfig(word, text=random_word['Arabic'], fill='white')
    canvas.itemconfigure(card_image, image=card_back_img)



#--------------------------- UI ---------------------------

window = Tk()
window.title("Flash Card")
window.config(padx= 50, pady=50 , background=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)







# Canvas
card_back_img = PhotoImage(file='images/card_back.png')
card_front_img= PhotoImage(file='images/card_front.png')



canvas = Canvas(master=window, width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_image = canvas.create_image(400, 262, image= card_front_img)
# canvas text
language = canvas.create_text(400, 150, text="Title", font=('Ariel', 40, 'italic'))
word = canvas.create_text(400,263, text='Word', font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)


# Button
right_img= PhotoImage(file='images/right.png')
right_button = Button(window, image= right_img, highlightthickness=0, command=right_words)
right_button.grid(row=1, column=1)

wrong_img= PhotoImage( file='images/wrong.png')
wrong_button= Button(window, image= wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)





next_card()
window.mainloop()