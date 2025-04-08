import tkinter as tk
from PIL import Image, ImageDraw

# Canvas size
canvas_width = 200
canvas_height = 200

# Create main window
root = tk.Tk()
root.title("Draw and Save")

# Create a black canvas
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg='black')
canvas.pack()

# Create a blank image and draw object using PIL
image = Image.new("L", (canvas_width, canvas_height), 'black')
draw = ImageDraw.Draw(image)

# Draw white circles as the brush strokes
def draw_on_canvas(event):
    x1, y1 = (event.x - 8), (event.y - 8)
    x2, y2 = (event.x + 8), (event.y + 8)
    canvas.create_oval(x1, y1, x2, y2, fill='white', outline='white')
    draw.ellipse([x1, y1, x2, y2], fill='white')

# Save the drawing as an image file
def save_image():
    image.save("drawing.png")
    print("Image saved as drawing.png")

# Clear the canvas and reset the image
def clear_canvas():
    canvas.delete("all")
    draw.rectangle([0, 0, canvas_width, canvas_height], fill="black")

# Bind mouse motion to drawing
canvas.bind("<B1-Motion>", draw_on_canvas)

# Buttons
tk.Button(root, text="Save Drawing", command=save_image).pack()
tk.Button(root, text="Clear", command=clear_canvas).pack()

# Start the GUI loop
root.mainloop()
