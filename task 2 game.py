import tkinter as tk
from PIL import Image, ImageTk  
import random

root = tk.Tk()
root.title("Rock Paper Scissors")
root.config(bg="#1e1e2f")  # Dark professional background
root.geometry("900x500")

user_score = 0
comp_score = 0
choices = ["rock", "paper", "scissors"]

def load_image(path, size=(150, 150)):
    img = Image.open(path)
    img = img.resize(size)
    return ImageTk.PhotoImage(img)


# Load images AFTER root is created
image_map = {
    "rock": load_image(r"C:\Users\pansu\OneDrive\Desktop\todo_list.py\todo_list.json\ston.py\rock.png.jpg"),
    "paper": load_image(r"C:\Users\pansu\OneDrive\Desktop\todo_list.py\todo_list.json\ston.py\paper.png.jpg"),
    "scissors": load_image(r"C:\Users\pansu\OneDrive\Desktop\todo_list.py\todo_list.json\ston.py\scissors.png.jpg"),
    "rock-user": load_image(r"C:\Users\pansu\OneDrive\Desktop\todo_list.py\todo_list.json\ston.py\rock-user.png.jpg"),
    "paper-user": load_image(r"C:\Users\pansu\OneDrive\Desktop\todo_list.py\todo_list.json\ston.py\paper-user.png.jpg"),
    "scissors-user": load_image(r"C:\Users\pansu\OneDrive\Desktop\todo_list.py\todo_list.json\ston.py\scissors-user.png.jpg")
}


def play(user_choice):
    global user_score, comp_score
    comp_choice = random.choice(choices)
    user_label.config(image=image_map[f"{user_choice}-user"])
    comp_label.config(image=image_map[comp_choice])

    if user_choice == comp_choice:
        result = "It's a Draw!"
    elif (user_choice == "rock" and comp_choice == "scissors") or \
         (user_choice == "paper" and comp_choice == "rock") or \
         (user_choice == "scissors" and comp_choice == "paper"):
        user_score += 1
        result = "You Win!!!"
    else:
        comp_score += 1
        result = "You Lose!"

    user_score_label.config(text=str(user_score))
    comp_score_label.config(text=str(comp_score))
    result_label.config(text=result)

# --- UI Frames ---
top_frame = tk.Frame(root, bg="#00acbf")
top_frame.pack(pady=20)

mid_frame = tk.Frame(root, bg="#00acbf")
mid_frame.pack()

bottom_frame = tk.Frame(root, bg="#00acbf")
bottom_frame.pack(pady=20)

# --- USER ---
tk.Label(top_frame, text=": USER :", font=("Helvetica", 18, "bold"), bg="#00acbf", fg="white").grid(row=0, column=0, padx=120)
user_label = tk.Label(top_frame, image=image_map["rock-user"], bg="#00acbf")
user_label.grid(row=1, column=0)
user_score_label = tk.Label(top_frame, text="0", font=("Helvetica", 22), bg="#00acbf", fg="white")
user_score_label.grid(row=2, column=0)

# --- COMPUTER ---
tk.Label(top_frame, text=": COMPUTER :", font=("Helvetica", 18, "bold"), bg="#00acbf", fg="white").grid(row=0, column=1, padx=120)
comp_label = tk.Label(top_frame, image=image_map["rock"], bg="#00acbf")
comp_label.grid(row=1, column=1)
comp_score_label = tk.Label(top_frame, text="0", font=("Helvetica", 22), bg="#00acbf", fg="white")
comp_score_label.grid(row=2, column=1)

# --- RESULT LABEL ---
result_label = tk.Label(mid_frame, text="Make your move!", font=("Helvetica", 20, "bold"), bg="#ffffff", fg="#000000")
result_label.pack()

# --- BUTTONS ---
btn_style = {"width": 15, "font": ("Helvetica", 14, "bold"), "fg": "white", "padx": 10}

tk.Button(bottom_frame, text="ROCK", bg="#e74c3c", command=lambda: play("rock"), **btn_style).pack(side="left", padx=10)
tk.Button(bottom_frame, text="PAPER", bg="#3498db", command=lambda: play("paper"), **btn_style).pack(side="left", padx=10)
tk.Button(bottom_frame, text="SCISSOR", bg="#2ecc71", command=lambda: play("scissors"), **btn_style).pack(side="left", padx=10)

# --- Start the app ---
root.mainloop()
 