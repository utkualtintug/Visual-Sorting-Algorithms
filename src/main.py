from tkinter import *
from tkinter import messagebox
import random

# Canvas and application state variables
canvas_width = 450
canvas_height = 450
speed = 50              # Animation speed (lower = faster)
is_paused = False       # Tracks if sorting is paused
is_sorting = False      # Tracks if sorting is in progress
is_reseted = False      # Tracks if application has been reset
current_i = 0           # Current position in outer loop
current_j = 0           # Current position in inner loop
numOfBar = 0            # Number of bars to display
barHeight = []          # List containing heights of bars
insertion_key = None    # Temporary variable for insertion sort
selection_key = None    # Tracks minimum index for selection sort

# Initialize main window
win = Tk()
win.title("Visual Sorting Algorithms")
win.geometry("510x700")

# Create canvas for visualization
canvas = Canvas(win, width=450, height=450, bg="gray")
canvas.grid(row=0, column=0, padx=25, pady=10)

def randomNumber():
    """Generate random numbers for bar heights"""
    global barHeight, is_reseted, numOfBar
    is_reseted = False

    try:
        numOfBar = int(num_of_bar.get())
        generate_button["state"] = DISABLED
        aList = [random.randint(10,400) for _ in range(numOfBar)]
        barHeight = aList
        return barHeight
    except ValueError:
        messagebox.showerror("Input Error","Please enter a number!")
        barHeight = [] 
        return []
    
def generate(highlight_indices=None, color_override=None):
    """Draw bars on canvas with optional highlighting"""
    global barHeight, is_sorting

    if is_sorting == False:
        reset()

    if len(barHeight) == 0:
        randomNumber() 

    if len(barHeight) == 0:
        return
        
    reset_button["state"] = NORMAL
    canvas.delete("all")  # Clear canvas before drawing
    bar_width = canvas_width / len(barHeight)
    for i in range(len(barHeight)):
        # Calculate bar position
        x0 = i * bar_width
        x1 = x0 + bar_width
        y0 = canvas_height - barHeight[i]
        y1 = canvas_height

        # Determine bar color based on state
        if highlight_indices and i in highlight_indices:
            color = "red"  # Highlight bars being compared
        elif color_override:
            color = color_override  # Override color (e.g., for completed sort)
        else:
            color = "skyblue"  # Default color

        canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        

def sorting():
    """Start sorting with selected algorithm"""
    global is_paused, is_sorting
    switch()
    if is_sorting:
        return
    is_paused = False
    is_sorting = True

    # Choose algorithm based on selection
    if selected_algo.get() == "Bubble":
        bubble_step(0, 0)
    elif selected_algo.get() == "Insertion":
        insertion_step(1, 0)
    elif selected_algo.get() == "Selection":
        selection_step(0, 1)


def bubble_step(i,j):
    """Recursive implementation of bubble sort"""
    global is_paused, current_i, current_j, is_sorting
    n = len(barHeight)
    
    # Handle pause state
    if is_paused:
        current_i = i
        current_j = j
        is_sorting = False
        return

    # Check if sorting is complete
    if i >= len(barHeight) - 1:
        generate(color_override="#5cb85c")  # Green color for sorted array
        is_sorting = False
        sort_button["state"] = NORMAL
        algo_menu["state"] = NORMAL
        generate_button["state"] = NORMAL
        return

    # Process current comparison in inner loop
    if j < n - i - 1:
        if barHeight[j] > barHeight[j + 1]:
            barHeight[j], barHeight[j + 1] = barHeight[j + 1], barHeight[j]  # Swap if needed
        generate(highlight_indices=[j, j + 1])  # Highlight current comparison
        canvas.after(speed, lambda: bubble_step(i, j + 1))  # Move to next comparison
    else:
        # Inner loop complete, move to next pass
        canvas.after(speed, lambda: bubble_step(i + 1, 0))


def insertion_step(i, j):
    """Recursive implementation of insertion sort"""
    global is_paused, current_i, current_j, is_sorting, insertion_key
    
    # Handle pause state
    if is_paused:
        current_i = i
        current_j = j
        is_sorting = False
        return

    # Check if sorting is complete
    if i >= len(barHeight):
        generate(color_override="#5cb85c")  # Green color for sorted array
        is_sorting = False
        sort_button["state"] = NORMAL
        algo_menu["state"] = NORMAL
        generate_button["state"] = NORMAL
        return

    # Get current key if starting a new insertion
    if insertion_key is None:
        insertion_key = barHeight[i]
        j = i - 1

    # Shift elements greater than key to the right
    if j >= 0 and barHeight[j] > insertion_key:
        barHeight[j + 1] = barHeight[j]
        generate(highlight_indices=[j, j + 1])
        canvas.after(speed, lambda: insertion_step(i, j - 1))
    else:
        # Found correct position, insert key
        barHeight[j + 1] = insertion_key
        insertion_key = None
        generate(highlight_indices=[j + 1])
        canvas.after(speed, lambda: insertion_step(i + 1, i))
        

def selection_step(i, j):
    """Recursive implementation of selection sort"""
    global is_paused, current_i, current_j, is_sorting, selection_key
    
    # Handle pause state
    if is_paused:
        current_i = i
        current_j = j
        is_sorting = False
        return

    # Check if sorting is complete
    if i >= len(barHeight):
        generate(color_override="#5cb85c")  # Green color for sorted array
        is_sorting = False
        sort_button["state"] = NORMAL
        algo_menu["state"] = NORMAL
        generate_button["state"] = NORMAL
        return

    # Initialize minimum index for current pass
    if selection_key is None:
        selection_key = i
        
    # Find minimum element in unsorted portion
    if j < len(barHeight):
        if barHeight[j] < barHeight[selection_key]:
            selection_key = j
        
        generate(highlight_indices=[i, j, selection_key])
        canvas.after(speed, lambda: selection_step(i, j + 1))
    else:
        # Swap minimum with first unsorted element
        barHeight[i], barHeight[selection_key] = barHeight[selection_key], barHeight[i]
        generate(highlight_indices=[i, selection_key])
        selection_key = None 
        canvas.after(speed, lambda: selection_step(i + 1, i + 2))


def faster():
    """Increase animation speed"""
    global speed
    if speed > 5:
        speed -= 5


def slower():
    """Decrease animation speed"""
    global speed
    if speed <= 500:
        speed += 5


def stop():
    """Pause sorting"""
    global is_paused
    is_paused = True


def continueSort():
    """Resume sorting from where it was paused"""
    global is_paused, is_sorting
    if is_sorting:
        return
    is_paused = False        
    is_sorting = True

    # Continue with the appropriate algorithm
    if selected_algo.get() == "Bubble":
        bubble_step(current_i, current_j)
    elif selected_algo.get() == "Insertion":
        insertion_step(current_i, current_j)
    elif selected_algo.get() == "Selection":
        selection_step(current_i, current_j)


def switch():
    """Toggle button states"""
    if sort_button["state"] == NORMAL:
        algo_menu["state"] = DISABLED
        sort_button["state"] = DISABLED
    else:
        sort_button["state"] = NORMAL


def reset():
    """Reset application to initial state"""
    global barHeight, is_reseted, is_paused, insertion_key, selection_key
    is_reseted = True
    is_paused = True
    insertion_key = None
    selection_key = None

    reset_button["state"] = DISABLED
    generate_button["state"] = NORMAL
    algo_menu["state"] = NORMAL
    if is_sorting:
        sort_button["state"] = NORMAL
    barHeight.clear()
    canvas.delete("all")

# Input frame for number of bars
input_frame = Frame(win)
input_frame.grid(row=1, column=0, pady=10)

num_of_bar_text = Label(input_frame, text="Number of bars:")
num_of_bar_text.pack(side=LEFT, padx=5)

num_of_bar = Entry(input_frame, width=10)
num_of_bar.pack(side=LEFT, padx=5)
num_of_bar.focus()

generate_button = Button(input_frame, text="Generate", command=generate)
generate_button.pack(side=LEFT, padx=5)

# Main frame for algorithm selection and sort button
main_frame = Frame(win)
main_frame.grid(row=2, column=0, pady=10)

sort_button = Button(main_frame, text="Sort", command=sorting)
sort_button.pack(side=LEFT, padx=5)

selected_algo = StringVar()
selected_algo.set("Bubble")

algo_menu = OptionMenu(main_frame, selected_algo, "Bubble", "Insertion", "Selection")
algo_menu.pack(side=LEFT, padx=5)

# Speed control buttons
button_frame = Frame(win)
button_frame.grid(row=3, column=0, pady=10)

slower_button = Button(button_frame, text="➖", command=slower)
slower_button.pack(side=LEFT, padx=5)

faster_button = Button(button_frame, text="➕", command=faster)
faster_button.pack(side=LEFT, padx=5)

# Playback control buttons
run_frame = Frame(win)
run_frame.grid(row=4, column=0, pady=10)

stop_button = Button(run_frame, text="⏹️", command=stop)
stop_button.pack(side=LEFT, padx=5)

continueSort_button = Button(run_frame, text="▶️", command=continueSort)
continueSort_button.pack(side=LEFT, padx=5)

reset_button = Button(run_frame, text="Reset", command=reset)
reset_button.pack(side=LEFT, padx=5)

# Start the application
win.mainloop()