from tkinter import *

def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text='')

def get_operator(op):
    current = result_label['text']
    new = current + op
    result_label.config(text=new)

def get_result():
    try:
        expression = result_label['text']
        result = eval(expression)
        result_label.config(text=str(round(result, 2)))
    except ZeroDivisionError:
        result_label.config(text="Divide by 0")
    except:
        result_label.config(text="Error")

root = Tk()
root.title("Smart Calc")
root.geometry("320x460")
root.resizable(False, False)
root.configure(background="#1e1e2e")  # Dark background

# Result display
result_label = Label(root, text='', bg="#1e1e2e", fg="#f8f8f2", anchor='e')
result_label.grid(row=0, column=0, columnspan=4, pady=(30, 15), padx=10, sticky="we")
result_label.config(font=('Calibri', 32, 'bold'), height=2)

# Button style
btn_bg = "#3b82f6"
btn_fg = "white"
btn_font = ('Calibri', 16, 'bold')
op_bg = "#10b981"

# Row 1
Button(root, text='7', bg=btn_bg, fg=btn_fg, font=btn_font, width=5, height=2, command=lambda: get_digit(7)).grid(row=1, column=0)
Button(root, text='8', bg=btn_bg, fg=btn_fg, font=btn_font, width=5, height=2, command=lambda: get_digit(8)).grid(row=1, column=1)
Button(root, text='9', bg=btn_bg, fg=btn_fg, font=btn_font, width=5, height=2, command=lambda: get_digit(9)).grid(row=1, column=2)
Button(root, text='+', bg=op_bg, fg='white', font=btn_font, width=5, height=2, command=lambda: get_operator('+')).grid(row=1, column=3)

# Row 2
Button(root, text='4', bg=btn_bg, fg=btn_fg, font=btn_font, width=5, height=2, command=lambda: get_digit(4)).grid(row=2, column=0)
Button(root, text='5', bg=btn_bg, fg=btn_fg, font=btn_font, width=5, height=2, command=lambda: get_digit(5)).grid(row=2, column=1)
Button(root, text='6', bg=btn_bg, fg=btn_fg, font=btn_font, width=5, height=2, command=lambda: get_digit(6)).grid(row=2, column=2)
Button(root, text='-', bg=op_bg, fg='white', font=btn_font, width=5, height=2, command=lambda: get_operator('-')).grid(row=2, column=3)

# Row 3
Button(root, text='1', bg=btn_bg, fg=btn_fg, font=btn_font, width=5, height=2, command=lambda: get_digit(1)).grid(row=3, column=0)
Button(root, text='2', bg=btn_bg, fg=btn_fg, font=btn_font, width=5, height=2, command=lambda: get_digit(2)).grid(row=3, column=1)
Button(root, text='3', bg=btn_bg, fg=btn_fg, font=btn_font, width=5, height=2, command=lambda: get_digit(3)).grid(row=3, column=2)
Button(root, text='*', bg=op_bg, fg='white', font=btn_font, width=5, height=2, command=lambda: get_operator('*')).grid(row=3, column=3)

# Row 4
Button(root, text='C', bg="#ef4444", fg='white', font=btn_font, width=5, height=2, command=clear).grid(row=4, column=0)
Button(root, text='0', bg=btn_bg, fg=btn_fg, font=btn_font, width=5, height=2, command=lambda: get_digit(0)).grid(row=4, column=1)
Button(root, text='=', bg=op_bg, fg='white', font=btn_font, width=5, height=2, command=get_result).grid(row=4, column=2)
Button(root, text='/', bg=op_bg, fg='white', font=btn_font, width=5, height=2, command=lambda: get_operator('/')).grid(row=4, column=3)

root.mainloop()
