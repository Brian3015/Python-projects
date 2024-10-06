import customtkinter

# used to calculate equations
calculation = ""

# creating window
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("640x480")

# creating frame to put buttons on
frame = customtkinter.CTkFrame(master=app)
frame.pack(pady=0, padx=0, fill="both", expand=True)

# creating the space to enter numbers
number_entry = customtkinter.CTkEntry(master=frame, font=("Arial", 50), height=135, width=395)
number_entry.place(x=240, y=15)


# creating buttons

def buttons(text):
    global calculation
    calculation += text
    current = number_entry.get()
    number_entry.delete(0, "end")
    number_entry.insert(0, current + text)


def clear():
    number_entry.delete(0, "end")


def backspace():
    number_entry.delete(len(number_entry.get())-1,"end")



def equal():
    global calculation
    try:
        calculation = str(eval(calculation))
        number_entry.delete(0, "end")
        number_entry.insert(0, calculation)
    except:
        clear_field()
        number_entry.insert(0, "Error")


def clear_field():
    global calculation
    calculation = ""
    number_entry.delete(0, "end")


# making the buttons function

equal_sign = customtkinter.CTkButton(master=frame, text="=", font=("Arial", 18), height=75, width=75,
                                     command=equal)
equal_sign.place(x=560, y=400)

modulo = customtkinter.CTkButton(master=frame, text="%", font=("Arial", 18), height=75, width=75,
                                 command=lambda: buttons("%"))
modulo.place(x=560, y=320)

parenthesis = customtkinter.CTkButton(master=frame, text="( )", font=("Arial", 18), height=75, width=75,
                                      command=lambda: buttons("()"))
parenthesis.place(x=560, y=240)

clear = customtkinter.CTkButton(master=frame, text="AC", font=("Arial", 18), height=75, width=75,
                                command=clear)
clear.place(x=560, y=160)

add = customtkinter.CTkButton(master=frame, text="+", font=("Arial", 18), height=75, width=75,
                              command=lambda: buttons("+"))
add.place(x=480, y=400)

subtract = customtkinter.CTkButton(master=frame, text="-", font=("Arial", 18), height=75, width=75,
                                   command=lambda: buttons("-"))
subtract.place(x=480, y=320)

multiply = customtkinter.CTkButton(master=frame, text="x", font=("Arial", 18), height=75, width=75,
                                   command=lambda: buttons("*"))
multiply.place(x=480, y=240)

divide = customtkinter.CTkButton(master=frame, text="÷", font=("Arial", 18), height=75, width=75,
                                 command=lambda: buttons("/"))
divide.place(x=480, y=160)

backspace = customtkinter.CTkButton(master=frame, text="Delete", font=("Arial", 18), height=75, width=75,
                                    command=backspace)
backspace.place(x=400, y=400)

three = customtkinter.CTkButton(master=frame, text="3", font=("Arial", 18), height=75, width=75,
                                command=lambda: buttons("3"))
three.place(x=400, y=320)

six = customtkinter.CTkButton(master=frame, text="6", font=("Arial", 18), height=75, width=75,
                              command=lambda: buttons("6"))
six.place(x=400, y=240)

nine = customtkinter.CTkButton(master=frame, text="9", font=("Arial", 18), height=75, width=75,
                               command=lambda: buttons("9"))
nine.place(x=400, y=160)

decimal = customtkinter.CTkButton(master=frame, text=".", font=("Arial", 18), height=75, width=75,
                                  command=lambda: buttons("."))
decimal.place(x=320, y=400)

two = customtkinter.CTkButton(master=frame, text="2", font=("Arial", 18), height=75, width=75,
                              command=lambda: buttons("2"))
two.place(x=320, y=320)

five = customtkinter.CTkButton(master=frame, text="5", font=("Arial", 18), height=75, width=75,
                               command=lambda: buttons("5"))
five.place(x=320, y=240)

eight = customtkinter.CTkButton(master=frame, text="8", font=("Arial", 18), height=75, width=75,
                                command=lambda: buttons("8"))
eight.place(x=320, y=160)

zero = customtkinter.CTkButton(master=frame, text="0", font=("Arial", 18), height=75, width=75,
                               command=lambda: buttons("0"))
zero.place(x=240, y=400)

one = customtkinter.CTkButton(master=frame, text="1", font=("Arial", 18), height=75, width=75,
                              command=lambda: buttons("1"))
one.place(x=240, y=320)

four = customtkinter.CTkButton(master=frame, text="4", font=("Arial", 18), height=75, width=75,
                               command=lambda: buttons("4"))
four.place(x=240, y=240)

seven = customtkinter.CTkButton(master=frame, text="7", font=("Arial", 18), height=75, width=75,
                                command=lambda: buttons("7"))
seven.place(x=240, y=160)

app.mainloop()
