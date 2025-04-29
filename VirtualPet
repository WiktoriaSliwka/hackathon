import time
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk  # Import Pillow for animated GIFs
import os

class VirtualPet:
    def __init__(self):
        self.health = 100
        self.alive = True
        
    def attend_lesson(self):
        if self.alive:
            self.health = min(self.health + 10, 100)
            
    def miss_lesson(self):
        if self.alive:
            self.health -= 10
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
        pet_image_label.config(image=dead_image)
        stop_animation()
    elif pet.health > 60:  # Show animation only when health > 30
        pet_label.config(text="🐾 Your pet is fine! 🐾")
        start_gif_animation(full_health_gif_frames)  # Start animation for full health
    else:  # Health <= 30 but still alive
        pet_label.config(text="🐾 Your pet is weak! 🐾")
        pet_image_label.config(image=low_health_image)
        stop_animation()

# Function to remove background color from GIF
def remove_background(gif, background_color=(255, 255, 255)):
    frames = []
    for frame in range(gif.n_frames):
        gif.seek(frame)
        frame_image = gif.convert("RGBA")  # Convert to RGBA to handle transparency
        data = frame_image.getdata()
        new_data = []
        for item in data:
            # Replace the background color with transparency
            if item[:3] == background_color:
                new_data.append((255, 255, 255, 0))  # Fully transparent
            else:
                new_data.append(item)
        frame_image.putdata(new_data)
        frames.append(frame_image)
    return frames

# Animation control variables
animation_running = False
animation_id = None

# Function to stop animation
def stop_animation():
    global animation_running, animation_id
    if animation_running and animation_id is not None:
        root.after_cancel(animation_id)  # Cancel the scheduled animation
        animation_running = False
        animation_id = None

# Function to animate the GIF
def start_gif_animation(frames):
    global gif_frame, animation_running, animation_id
    
    # Stop any existing animation first
    stop_animation()
    
    gif_frame = 0  # Initialize gif_frame
    animation_running = True
    
    def animate():
        global gif_frame, animation_id, animation_running
        if not animation_running:
            return  # Exit if animation was stopped
            
        gif_frame = (gif_frame + 1) % len(frames)  # Cycle through frames
        gif_image = ImageTk.PhotoImage(frames[gif_frame])
        pet_image_label.config(image=gif_image)
        pet_image_label.image = gif_image  # Keep a reference to avoid garbage collection
        
        # Schedule next frame
        animation_id = root.after(100, animate)  # Adjust the delay as needed
    
    # Start the animation
    animate()

# Setup GUI
root = tk.Tk()
root.title("Virtual Pet Attendance")
pet = VirtualPet()

# Load images and GIFs with error handling
try:
    # Make sure paths are correct
    gif_path = "Assets/happy_cat.gif"
    sad_path = "Assets/sad_cat.png"
    dead_path = "Assets/rip.png"
    
    print(f"Loading GIF from: {os.path.abspath(gif_path)}")
    
    full_health_gif = Image.open(gif_path)  # Load GIF with Pillow
    full_health_gif_frames = remove_background(full_health_gif)  # Remove background
    
    # Convert the first frame to PhotoImage for initial display
    first_frame = ImageTk.PhotoImage(full_health_gif_frames[0])
    
    low_health_image = PhotoImage(file=sad_path)
    dead_image = PhotoImage(file=dead_path)
    
except Exception as e:
    print(f"Error loading images: {e}")
    print(f"Current working directory: {os.getcwd()}")
    root.destroy()
    exit()

# Initial UI setup
pet_label = tk.Label(root, text="🐾 Your pet is alive 🐾", font=("Arial", 24))
pet_label.pack(pady=10)

health_label = tk.Label(root, text=f"Health: {pet.health}", font=("Arial", 18))
health_label.pack(pady=5)

pet_image_label = tk.Label(root)
pet_image_label.pack(pady=10)

tap_button = tk.Button(root, text="Tap In (Attend)", command=tap_in)
tap_button.pack(pady=5)

miss_button = tk.Button(root, text="Miss Lesson", command=miss_lesson)
miss_button.pack(pady=5)

# Start the animation for the initial state (since health starts at 100 > 30)
start_gif_animation(full_health_gif_frames)

root.mainloop()
