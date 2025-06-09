# Visual Sorting Algorithms

A Python application that visualizes sorting algorithms using Tkinter GUI. This interactive tool helps users understand how different sorting algorithms work by displaying the step-by-step process visually.

## Features

- **Algorithm Visualization**: Watch the sorting process in real-time with colored bars
- **Multiple Algorithms**: Currently supports Bubble Sort and Insertion Sort
- **Playback Controls**: Start, stop, continue, and reset sorting operations
- **Speed Adjustment**: Control the visualization speed (faster/slower)
- **Random Data Generation**: Create new random datasets to sort

## How to Use

1. Click the **Generate** button to create a random array of values (represented as bars)
2. Select a sorting algorithm from the dropdown menu (Bubble or Insertion)
3. Click the **Sort** button to start the visualization
4. Use the playback controls:
   - ⏹️ (Stop): Pause the sorting process
   - ▶️ (Continue): Resume a paused sorting process
   - **Reset**: Clear the canvas and reset all values
5. Adjust the sorting speed using the ➖ (slower) and ➕ (faster) buttons

## Screenshots

![Sorting visualization in action](/img.png)


## Visual Feedback

- **Blue bars**: Unsorted/normal elements
- **Red bars**: Elements currently being compared or moved
- **Green bars**: Completely sorted array (when sorting is finished)

## Implementation Details

- Written in Python using Tkinter for the GUI
- Implements step-by-step visualization of sorting algorithms
- Uses canvas for rendering the bars
- Each algorithm is implemented as a recursive function with step-by-step execution

## Requirements

- Python 3.x
- Tkinter

## Running the Application

```
python main.py
```

This project provides an educational tool for understanding sorting algorithms through visual representation, making it easier to grasp the concepts of different sorting techniques.