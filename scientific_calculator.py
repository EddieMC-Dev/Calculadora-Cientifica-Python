from tkinter import Tk, Frame, Label, Button, RAISED, RIDGE, StringVar
from math import sqrt, tan, log, log10, pi, cos, sin, e


def execute_functions(event):
    if event == "=":
        calculate()
    elif event == "C":
        clear_display()
    else:
        input_values(event)

def input_values(event):
    global contents
    if contents[-1] in "+-." and event in "+-.":
        pass
    else:
        contents = contents + str(event)

    info.set(contents)
    
def calculate():
    global contents
    resultado = eval(contents)
    if type(resultado) == float:
        resultado = str(round(resultado, 10))   
    if str(resultado)[-2] == "." and str(resultado)[-1] == "0":  
        resultado = str(int(float(resultado)))
    clear_display()
    info.set(str(resultado))

def clear_display():
    global contents
    contents = ' '
    info.set(' ')


# Colors
black = "#373738"
white = "#feffff"
blue = "#28454d"
gray = "#545454"

# Window
window = Tk()
window.title("Calculadora Científica")
window.geometry("320x392")
window.maxsize(320, 392)
window.minsize(320, 392)
window.config(bg=white)

# Display
contents = ' '
info = StringVar()
frame_display = Frame(window, width=320, height=70, bg=blue)
frame_display.grid(row=0, column=0)
label_display = Label(frame_display, width=17, height=2, textvariable=info, 
                      font=('Ivy 23'), anchor="e", fg=white, bg=blue,
                      padx=10)
label_display.place(x=0, y=5)

# Buttons
frame_buttons = Frame(window, width=320, height=355, bg=gray)
frame_buttons.grid(row=1, column=0)

buttons_text = ["tan", "sin", "cos", "sqrt", "log", "log10", "e", "pow",
                "pi", ",", "(", ")"] + [char for char in "C%/789*456-123+0.="]
buttons_bg = ([black] * 4 * 3 + [gray] * 3 + [black, black, black, gray] * 3
              + [black, black, gray])

buttons_width = [10] * 4 * 3 + [22, 10, 10] + [10] * 4 * 3 + [22, 10, 10]
buttons_x = ([0, 80, 160, 240] * 3 + [0, 160, 240] + [0, 80, 160, 240] * 3
             + [0, 160, 240]) 
buttons_y = ([0] * 4 + [41] * 4 + [81] * 4 + [121] * 3 + [161] * 4 + [201] * 4
             + [241] * 4 + [281] * 3)

for idx, text in enumerate(buttons_text):
    button = Button(frame_buttons, text=text, width=buttons_width[idx],
                    height=2, font=('Ivy 9 bold'), bg=buttons_bg[idx], 
                    fg=white, relief=RAISED, overrelief=RIDGE,
                    activebackground=black, activeforeground=gray,
                    command=lambda event=text: execute_functions(event))
    button.place(x=buttons_x[idx], y=buttons_y[idx])

# Loop
window.mainloop()
