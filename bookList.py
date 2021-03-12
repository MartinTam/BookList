from tkinter import *
import sqlite3

root = Tk()
root.geometry('1400x700')
root.title('Book List')
# ---------------------------------------------------------

# Create and connect to the database
connect = sqlite3.connect('bookDatabase.db')
cursor = connect.cursor()

try:
    cursor.execute("CREATE TABLE bookList (book text, author text);")
except:
    pass

# ---------------------------------------------------------

# Title
title = Label(root, text = 'Book List', font = ('Comicsans', 20)).grid(row = 0, column = 0, columnspan = 4, pady = 30)

# Add new book
bookNameTitle = Label(root, text = 'Name of the book:').grid(row = 1, column = 1)
authorNameTitle = Label(root, text = 'Name of the author:').grid(row = 1, column = 2)

bookNameType = Entry(root, width = 70)
bookNameType.grid(row = 2, column = 1, padx = 50)

authorNameType = Entry(root, width = 70)
authorNameType.grid(row = 2, column = 2)

# Function to add book to the database
def addBook():

    # Connect to the database
    connect = sqlite3.connect('bookDatabase.db')
    cursor = connect.cursor()

    # Add book to the database
    if bookNameType.get() != '' and authorNameType.get() != '':
        values = [ ( bookNameType.get(), authorNameType.get() ) ]
        cursor.executemany("INSERT INTO bookList VALUES (?,?)", values)

    # Clear the entry box
    bookNameType.delete(0, END)
    authorNameType.delete(0, END)

    # Commit and close the database
    connect.commit()
    connect.close()

addButton = Button(root, text = 'ADD', fg = 'white', bg = 'green', command = addBook).grid(row = 2, column = 3, padx = 20)

# Function to show the database
def showList():
    # Connect to the database
    connect = sqlite3.connect('bookDatabase.db')
    cursor = connect.cursor()

    cursor.execute("SELECT * FROM bookList;")
    output = cursor.fetchall()

    increment = 1
    startRow = 6

    for x in output:
        checkbox = Checkbutton(root, text = str(increment) ). grid(row = startRow, column = 0)
        book = Label(root, text = x[0]).grid(row = startRow, column = 1)
        author = Label(root, text = x[1]).grid(row = startRow, column = 2)
        update = Button(root, text = 'CHANGE').grid(row = startRow, column = 3)

        increment += 1
        startRow += 1

    # Commit and close the database
    connect.commit()
    connect.close()

# Show the list
showButton = Button(root, text = 'SHOW THE LIST', command = showList).grid(row = 3, column = 0, columnspan = 4, pady = 20)

# Function to hide the database
def hideList():
    mainWidgets = [
        '.!label', 
        '.!label2', 
        '.!label3', 
        '.!entry', 
        '.!entry2', 
        '.!button', 
        '.!button2', 
        '.!button3'
        ]

    for widgets in root.winfo_children():
        for main in mainWidgets:
            if str(widgets) != main:
                widgets.destroy()

hideButton = Button(root, text = 'HIDE THE LIST', command = hideList).grid(row = 4, column = 0, columnspan = 4, pady = 20)

# Delete button
deleteButton = Button(root, text = 'DELETE', fg = 'white', bg = 'red').grid(row = 5, column = 0, columnspan = 4, pady = 20)

'''
# Example data
checkbox_0 = Checkbutton(root, text = '1'). grid(row = 5, column = 0)
book_0 = Label(root, text = 'Harry Potter and The Half Blood Prince').grid(row = 5, column = 1)
author_0 = Label(root, text = 'J.K.Rowling').grid(row = 5, column = 2)
update_0 = Button(root, text = 'CHANGE').grid(row = 5, column = 3)
'''


# ---------------------------------------------------------

# Commit and close the database
connect.commit()
connect.close()

# ---------------------------------------------------------
root.mainloop()