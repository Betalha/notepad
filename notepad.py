import tkinter as tk
from tkinter import filedialog, Text, END, INSERT, WORD, LEFT, BOTH, TRUE
from tkinter.ttk import Button, Style, Frame

def saveFile():
    new_file = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=[('Text files', '*.txt')])
    if new_file is None:
        return
    text = str(entry.get(1.0, END))
    new_file.write(text)
    new_file.close()

def openFile():
    file = filedialog.askopenfile(mode='r', filetypes=[('Text files', '*.txt')])
    if file is not None:
        content = file.read()
        entry.delete(1.0, END)
        entry.insert(INSERT, content)
        file.close()

def clearFile():
    entry.delete(1.0, END)

canvas = tk.Tk()
canvas.geometry("600x400")
canvas.title("Notepad Elegante")
bg_color = "#2d2d2d"
canvas.config(bg=bg_color)

style = Style()
style.theme_use('clam')
style.configure('TFrame', background=bg_color)
style.configure('TButton', background="#3c3f41", foreground="white", padding=10, font=('Arial', 10))

top = Frame(canvas, style='TFrame')
top.pack(pady=10, padx=10, fill='x')

b1 = Button(top, text="Abrir", command=openFile)
b1.pack(side=LEFT, padx=5)

b2 = Button(top, text="Salvar", command=saveFile)
b2.pack(side=LEFT, padx=5)

b3 = Button(top, text="Limpar", command=clearFile)
b3.pack(side=LEFT, padx=5)

b4 = Button(top, text="Sair", command=canvas.quit)
b4.pack(side=LEFT, padx=5)

entry = Text(canvas, wrap=WORD, bg="#1e1e1e", fg="#d4d4d4", insertbackground="white", font=("Consolas", 12), padx=10, pady=10)
entry.pack(expand=TRUE, fill=BOTH, padx=10, pady=(0, 10))

canvas.mainloop()