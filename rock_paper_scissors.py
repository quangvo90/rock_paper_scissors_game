# Description: A simple rock, paper, scissors game using Tkinter
# Author: Quang Vo
# Last modified: 12/10/2023

import tkinter as tk
import random
from PIL import ImageTk, Image
import os

window = tk.Tk()
window.title("Rock Paper Scissors Game")
window.geometry("800x800")

image_folder = "images"
rock_image = ImageTk.PhotoImage(Image.open(os.path.join(image_folder, "rock.png")).resize((200, 200)))
paper_image = ImageTk.PhotoImage(Image.open(os.path.join(image_folder, "paper.png")).resize((200, 200)))
scissors_image = ImageTk.PhotoImage(Image.open(os.path.join(image_folder, "scissors.png")).resize((200, 200)))
rock_image_comp = ImageTk.PhotoImage(Image.open(os.path.join(image_folder, "rock.png")).resize((200, 200)))
paper_image_comp = ImageTk.PhotoImage(Image.open(os.path.join(image_folder, "paper.png")).resize((200, 200)))
scissors_image_comp = ImageTk.PhotoImage(Image.open(os.path.join(image_folder, "scissors.png")).resize((200, 200)))
blank_image = ImageTk.PhotoImage(Image.open(os.path.join(image_folder, "blank.png")).resize((200, 200)))
images_list = [rock_image, paper_image, scissors_image]

user_label = tk.Label(window, text="Your choice")
user_label.grid(row=0, column=0)
computer_label = tk.Label(window, text="Computer choice")
computer_label.grid(row=0, column=2)
rock_button = tk.Button(window, image=rock_image)
paper_button = tk.Button(window, image=paper_image)
scissors_button = tk.Button(window, image=scissors_image)
rock_button.grid(row=1, column=0)
paper_button.grid(row=1, column=1)
scissors_button.grid(row=1, column=2)
user_image_label = tk.Label(window, image=blank_image)
user_image_label.grid(row=2, column=0)
computer_image_label = tk.Label(window, image=blank_image)
computer_image_label.grid(row=2, column=2)

result_label = tk.Label(window, text="Good Luck!", font=("Roboto", 20))
result_label.grid(row=4, column=1)

def computer_choice():
    choices = ["rock", "paper", "scissors"]
    choice = random.choice(choices)
    return choice

def user_rock():
    user_choice = "rock"
    computer_pick = computer_choice()
    display_winner(user_choice, computer_pick)

def user_paper():
    user_choice = "paper"
    computer_pick = computer_choice()
    display_winner(user_choice, computer_pick)

def user_scissors():
    user_choice = "scissors"
    computer_pick = computer_choice()
    display_winner(user_choice, computer_pick)

def display_winner(user_choice, computer_choice):
    if user_choice == "rock" and computer_choice == "paper":
        result = "Sorry, you lost!"
        computer_image_label.config(image=paper_image_comp)
    elif user_choice == "rock" and computer_choice == "scissors":
        result = "You won!"
        computer_image_label.config(image=scissors_image_comp)
    elif user_choice == "paper" and computer_choice == "rock":
        result = "You won!"
        computer_image_label.config(image=rock_image_comp)
    elif user_choice == "paper" and computer_choice == "scissors":
        result = "Sorry, you lost!"
        computer_image_label.config(image=scissors_image_comp)
    elif user_choice == "scissors" and computer_choice == "rock":
        result = "Sorry, you lost!"
        computer_image_label.config(image=rock_image_comp)
    elif user_choice == "scissors" and computer_choice == "paper":
        result = "You won!"
        computer_image_label.config(image=paper_image_comp)
    else:
        result = "It's a tie!"
        if computer_choice == "rock":
            computer_image_label.config(image=rock_image_comp)
        elif computer_choice == "paper":
            computer_image_label.config(image=paper_image_comp)
        elif computer_choice == "scissors":
            computer_image_label.config(image=scissors_image_comp)
    if user_choice == "rock":
        user_image_label.config(image=rock_image)
    elif user_choice == "paper":
        user_image_label.config(image=paper_image)
    else:
        user_image_label.config(image=scissors_image)
    result_label.config(text=result)

rock_button.config(command=user_rock)
paper_button.config(command=user_paper)
scissors_button.config(command=user_scissors)

def start_game():
    rock_button.config(state=tk.NORMAL)
    paper_button.config(state=tk.NORMAL)
    scissors_button.config(state=tk.NORMAL)
    start_button.destroy()
    play_label.destroy()
    result_label.config(text="Good Luck!", font=("Roboto", 20))
    result_label.grid()

def show_start_screen():
    global start_button, play_label
    play_label = tk.Label(window, text="Do you want to play?", font=("Roboto", 20))
    play_label.grid(row=5, column=1)
    start_button = tk.Button(window, text="Start", command=start_game)
    start_button.grid(row=6, column=1)
    result_label.grid_remove()

show_start_screen()

rock_button.config(state=tk.DISABLED)
paper_button.config(state=tk.DISABLED)
scissors_button.config(state=tk.DISABLED)

window.mainloop()
