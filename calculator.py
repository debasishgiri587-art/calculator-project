import tkinter as tk

# ---------------- Window Setup ----------------
root = tk.Tk()
root.title("Calculator")
root.geometry("320x520")   # ✅ correct size
root.configure(bg="black")
root.resizable(False, False)

# ---------------- Display ----------------
expression = ""
display = tk.StringVar()

def press(value):
    global expression
    expression += str(value)
    display.set(expression)

def clear():
    global expression
    expression = ""
    display.set("")

def backspace():
    global expression
    expression = expression[:-1]
    display.set(expression)

def calculate():
    global expression
    try:
        result = str(eval(expression))
        display.set(result)
        expression = result
    except:
        display.set("Error")
        expression = ""

entry = tk.Entry(
    root,
    textvariable=display,
    font=("Arial", 24),
    bg="black",
    fg="white",
    bd=0,
    justify="right"
)
entry.pack(fill="x", ipady=25, padx=10, pady=10)

# ---------------- Button Styles ----------------
btn_num = {
    "font": ("Arial", 18),
    "bg": "#2c2c2c",
    "fg": "white",
    "bd": 0,
    "width": 5,
    "height": 3
}

btn_op = {
    "font": ("Arial", 18),
    "bg": "#3c3c3c",
    "fg": "white",
    "bd": 0,
    "width": 5,
    "height": 3
}

btn_equal = {
    "font": ("Arial", 18),
    "bg": "#ff7f50",
    "fg": "white",
    "bd": 0,
    "width": 5,
    "height": 3
}

# ---------------- Buttons Frame ----------------
frame = tk.Frame(root, bg="black")
frame.pack(expand=True, fill="both")

# Make grid expand properly ✅
for i in range(5):
    frame.rowconfigure(i, weight=1)
for j in range(4):
    frame.columnconfigure(j, weight=1)

buttons = [
    ("C", clear), ("%", lambda: press("%")), ("⌫", backspace), ("/", lambda: press("/")),
    ("7", lambda: press(7)), ("8", lambda: press(8)), ("9", lambda: press(9)), ("*", lambda: press("*")),
    ("4", lambda: press(4)), ("5", lambda: press(5)), ("6", lambda: press(6)), ("-", lambda: press("-")),
    ("1", lambda: press(1)), ("2", lambda: press(2)), ("3", lambda: press(3)), ("+", lambda: press("+")),
    ("00", lambda: press("00")), ("0", lambda: press(0)), (".", lambda: press(".")), ("=", calculate)
]

row = 0
col = 0

for text, cmd in buttons:
    if text == "=":
        tk.Button(frame, text=text, command=cmd, **btn_equal).grid(
            row=row, column=col, padx=5, pady=5, sticky="nsew"
        )
    elif text in ["+", "-", "*", "/", "%", "C", "⌫"]:
        tk.Button(frame, text=text, command=cmd, **btn_op).grid(
            row=row, column=col, padx=5, pady=5, sticky="nsew"
        )
    else:
        tk.Button(frame, text=text, command=cmd, **btn_num).grid(
            row=row, column=col, padx=5, pady=5, sticky="nsew"
        )

    col += 1
    if col == 4:
        col = 0
        row += 1

# ---------------- Run App ----------------
root.mainloop()