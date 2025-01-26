# README

## Overview
This script uses Python's `turtle` module to create a graphical scene. The script includes functions to draw clouds, a sun, and a body of water, creating a simple yet visually appealing landscape.

## Features
1. **Draw Cloud**
   - Draws a cloud using four overlapping circles.
   - Parameters:
     - `x` (int): The x-coordinate of the cloud's position.
     - `y` (int): The y-coordinate of the cloud's position.
     - `size` (int): The radius of each circle in the cloud.
     - `color_name` (str): The color of the cloud.

2. **Draw Sun**
   - Draws a sun with customizable rays.
   - Parameters:
     - `x` (int): The x-coordinate of the sun's center.
     - `y` (int): The y-coordinate of the sun's center.
     - `strahlen` (int): The number of rays extending from the sun.

3. **Draw Sea**
   - Fills the bottom portion of the screen with a blue rectangle to represent water.

## Requirements
- Python 3.x
- `turtle` module (pre-installed with Python)

## How to Run
1. Ensure you have Python 3 installed on your system.
2. Copy the code into a Python file (e.g., `drawing_scene.py`).
3. Run the file in a Python environment that supports GUI (e.g., IDLE or directly on your computer).

## Example Usage
To draw a full scene with clouds, a sun, and water, use the following:

```python
from turtleforbeginners import *
from turtle import *

# Set up the turtle screen
setup(800, 600)

# Draw the sea
meer()

# Draw clouds
# Parameters: x-coordinate, y-coordinate, size, color
draw_cloud(-200, 150, 30, "white")
draw_cloud(100, 200, 40, "white")

# Draw the sun
# Parameters: x-coordinate, y-coordinate, number of rays
Sonne(0, 0, 12)

# Finish drawing
done()
```

## Customization
- **Clouds**: Change the `x`, `y`, `size`, and `color_name` to place and style clouds differently.
- **Sun**: Modify `strahlen` to increase or decrease the number of rays.
- **Sea**: Adjust the position and size of the rectangle in the `meer()` function to change its appearance.

## Output
The script produces a graphical window with a:
- Blue rectangle representing water.
- Sun with orange rays.
- White clouds positioned at specified coordinates.

## Author
This script was created to demonstrate the use of the `turtle` module for drawing simple graphical scenes in Python.

## License
This project is licensed under the MIT License.
