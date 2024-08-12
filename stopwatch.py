import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("Stopwatch")

# Global variables for the timer
running = False
counter = 0

# Function to update the timer display
def update_timer():
    if running:
        global counter
        counter += 1
        
        minutes = counter // 6000
        seconds = (counter // 100) % 60
        milliseconds = counter % 100
        
        time_display.config(text=f"{minutes:02}:{seconds:02}:{milliseconds:02}")
        root.after(10, update_timer)

# Start the timer
def start():
    global running
    if not running:
        running = True
        update_timer()

# Pause the timer
def pause():
    global running
    running = False

# Reset the timer
def reset():
    global running, counter
    running = False
    counter = 0
    time_display.config(text="00:00:00")

# Set up the display for the timer
time_display = tk.Label(root, text="00:00:00", font=("Arial", 40))
time_display.pack()

# Start button
start_button = tk.Button(root, text="Start", font=("Arial", 15), command=start)
start_button.pack(side=tk.LEFT, padx=5)

# Pause button
pause_button = tk.Button(root, text="Pause", font=("Arial", 15), command=pause)
pause_button.pack(side=tk.LEFT, padx=5)

# Reset button
reset_button = tk.Button(root, text="Reset", font=("Arial", 15), command=reset)
reset_button.pack(side=tk.LEFT, padx=5)

# Run the application
root.mainloop() 