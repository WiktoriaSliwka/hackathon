import time
import tkinter as tk

class VirtualPet:
    def __init__(self):
        self.health = 500
        self.alive = True
    
    def attend_lesson(self):
        if self.alive:
            self.health = min(self.health + 10, 500)
    
    def miss_lesson(self):
        if self.alive:
            self.health -= 20
            if self.health <= 0:
                self.health = 0
                self.alive = False


def tap_in():
    pet.attend_lesson()
    update_ui()

def miss_lesson():
    pet.miss_lesson()
    update_ui()

def update_ui():
    health_label.config(text=f"Health: {pet.health}")
    if not pet.alive:
        pet_label.config(text="💀 Your pet has died 💀")
    else:
        pet_label.config(text="🐾 Your pet is alive 🐾")


#paddy is padding 
# Setup GUI
        
root = tk.Tk()
root.title("Virtual Pet Attendance")

pet = VirtualPet()

pet_label = tk.Label(root, text="🐾 Your pet is alive 🐾", font=("Arial", 24))
pet_label.pack(pady=10)

health_label = tk.Label(root, text="Health: 100", font=("Arial", 18))
health_label.pack(pady=5)

tap_button = tk.Button(root, text="Tap In (Attend)", command=tap_in)
tap_button.pack(pady=5)

miss_button = tk.Button(root, text="Miss Lesson", command=miss_lesson)
miss_button.pack(pady=5)

root.mainloop()