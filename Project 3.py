#Importing Tkinter
from tkinter import *

#importing save as and open file function
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
import subprocess

#Setting an instance of Tkinter
compiler = Tk()

#Setting the icon of the Compiler
compiler.iconbitmap("Icon.ico")

#Setting a title for the compiler
compiler.title("Group 3 Compiler")

#Setting Global file path
file_path = ''

def set_file_path(path):
    global file_path
    file_path = path

#Create new file function
def new_file():
    editor.delete("1.0", END)
    compiler.title('New File - Group 3')

#saving a file
def save():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)

#opening a file
def open_file():
    path = askopenfilename(filetypes=[('Python files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)

#Running a funtion
def run():
    if file_path == '':
        save_prompt = Toplevel()
        message = Label(save_prompt, text="Kindly save your code first")
        message.pack()
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0', error)

#Creating a Menu Bar
menu_bar = Menu(compiler)

#Menu bar
menu_file = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='File', menu=menu_file)
menu_file.add_command(label='New', command=new_file)
menu_file.add_command(label='Open', command=open_file)
menu_file.add_command(label='Save', command=save)
menu_file.add_command(label='Run', command=run)
menu_file.add_separator()
menu_file.add_command(label='Exit', command=exit)

compiler.config(menu=menu_bar)

#Adding a text editor
editor = Text()
editor.pack()

#Adding an output box
code_output = Text(height=10, fg="black", bg="lightgrey")
code_output.pack()

#Exit button
close_button = Button(compiler, text="Close Program", command=compiler.quit, fg="grey", bg="black")
close_button.pack()

#Running the compiler
compiler.mainloop()