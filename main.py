from tkinter import *
import random

canvas_width = 450
canvas_height = 450
speed = 50
is_paused = False
is_sorting = False
current_i = 0
current_j = 0


win = Tk()
win.title("Visual Sorting Algorithms")
win.geometry("500x650")

canvas = Canvas(win, width=450, height=450, bg="gray")
canvas.grid(row=0, column=0, padx=25, pady=10)
barHeight = [random.randint(10,400) for _ in range(50)]


def generate(highlight_indices=None, color_override=None):
    canvas.delete("all")
    bar_width = canvas_width / len(barHeight)
    for i in range(len(barHeight)):
        x0 = i * bar_width
        x1 = x0 + bar_width
        y0 = canvas_height - barHeight[i]
        y1 = canvas_height

        if highlight_indices and i in highlight_indices:
            color = "red"
        elif color_override:
            color = color_override
        else:
            color = "skyblue"

        canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        

def bubble_step(i,j):
    global is_paused, current_i, current_j, is_sorting
    n = len(barHeight)
    
    if is_paused:
        current_i = i
        current_j = j
        is_sorting = False
        return

    if i >= len(barHeight) - 1:
        generate(color_override="#5cb85c")
        is_sorting = False
        return

    if j < n - i - 1:
        if barHeight[j] > barHeight[j + 1]:
            barHeight[j], barHeight[j + 1] = barHeight[j + 1], barHeight[j]
        generate(highlight_indices=[j, j + 1])
        canvas.after(speed, lambda: bubble_step(i, j + 1))
    else:
        canvas.after(speed, lambda: bubble_step(i + 1, 0))


def bubble():
    global is_paused, is_sorting
    switch()
    if is_sorting:
        return
    is_paused = False
    is_sorting = True
    bubble_step(0, 0)


def faster():
    global speed
    if speed > 5:
        speed -= 5


def slower():
    global speed
    if speed <= 500:
        speed += 5


def stop():
    global is_paused
    is_paused = True


def continueSort():
    global is_paused, is_sorting
    if is_sorting:
        return
    is_paused = False        
    is_sorting = True
    bubble_step(current_i, current_j)

def switch():
    if sort_button["state"] == NORMAL:
        sort_button["state"] = DISABLED
    else:
        sort_button["state"] = NORMAL


main_frame = Frame(win)
main_frame.grid(row=1, column=0, pady=10)

generate_button = Button(main_frame, text="Generate", command=generate)
generate_button.pack(side=LEFT, padx=5)

sort_button = Button(main_frame, text="Sort", command=bubble)
sort_button.pack(side=LEFT, padx=5)

button_frame = Frame(win)
button_frame.grid(row=2, column=0, pady=10)

slower_button = Button(button_frame, text="➖", command=slower)
slower_button.pack(side=LEFT, padx=5)

faster_button = Button(button_frame, text="➕", command=faster)
faster_button.pack(side=LEFT, padx=5)

run_frame = Frame(win)
run_frame.grid(row=3, column=0, pady=10)

stop_button = Button(run_frame, text="⏹️", command=stop)
stop_button.pack(side=LEFT, padx=5)

continueSort_button = Button(run_frame, text="▶️", command=continueSort)
continueSort_button.pack(side=LEFT, padx=5)

win.mainloop()