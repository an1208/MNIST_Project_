from tkinter import *
import numpy as np
from PIL import ImageGrab
from Prediction import predict

window = Tk()
window.title("Handwritten Digit Recognition")
l1 = Label()

def MyProject():
    global l1

    widget = cv
    x = window.winfo_rootx() + widget.winfo_x()
    y = window.winfo_rooty() + widget.winfo_y()
    x1 = x + widget.winfo_width()
    y1 = y + widget.winfo_height()

    img = ImageGrab.grab().crop((x, y, x1, y1)).resize((28, 28))

    # Convert to grayscale and invert colors
    img = img.convert('L')
    img = np.array(img)
    img = 255 - img  # Invert colors

    # Normalize pixel values (0 to 1)
    img = img / 255.0  

    # Reshape to match model input shape
    vec = img.reshape(1, 784)

    # Load the trained weights
    Theta1 = np.loadtxt('Theta1.txt')
    Theta2 = np.loadtxt('Theta2.txt')

    # Predict digit
    pred = predict(Theta1, Theta2, vec)

    # Clear previous prediction
    l1.destroy()

    # Display the new result
    l1 = Label(window, text=f"Digit = {pred[0]}", font=('Algerian', 20))
    l1.place(x=230, y=420)

lastx, lasty = None, None

def clear_widget():
    global cv, l1
    cv.delete("all")
    l1.destroy()

def event_activation(event):
    global lastx, lasty
    cv.bind('<B1-Motion>', draw_lines)
    lastx, lasty = event.x, event.y

def draw_lines(event):
    global lastx, lasty
    x, y = event.x, event.y
    cv.create_line((lastx, lasty, x, y), width=25, fill='white', capstyle=ROUND, smooth=TRUE, splinesteps=12)
    lastx, lasty = x, y

# UI Components
L1 = Label(window, text="Handwritten Digit Recognition", font=('Algerian', 25), fg="blue")
L1.place(x=35, y=10)

b1 = Button(window, text="1. Clear Canvas", font=('Algerian', 15), bg="orange", fg="black", command=clear_widget)
b1.place(x=120, y=370)

b2 = Button(window, text="2. Prediction", font=('Algerian', 15), bg="white", fg="red", command=MyProject)
b2.place(x=320, y=370)

cv = Canvas(window, width=350, height=290, bg='black')
cv.place(x=120, y=70)
cv.bind('<Button-1>', event_activation)

window.geometry("600x500")
window.mainloop()
