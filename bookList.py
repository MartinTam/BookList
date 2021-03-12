from tkinter import *

root = Tk()
root.geometry('1400x700')
root.title('Book List')
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

addButton = Button(root, text = 'ADD', fg = 'white', bg = 'green').grid(row = 2, column = 3)

# Delete button
deleteButton = Button(root, text = 'DELETE', fg = 'white', bg = 'red').grid(row = 3, column = 0, columnspan = 4, pady = 20)

# Example data
checkbox_0 = Checkbutton(root, text = '1'). grid(row = 4, column = 0)
book_0 = Label(root, text = 'Harry Potter and The Half Blood Prince').grid(row = 4, column = 1)
author_0 = Label(root, text = 'J.K.Rowling').grid(row = 4, column = 2)
update_0 = Button(root, text = 'CHANGE').grid(row = 4, column = 3)

checkbox_1 = Checkbutton(root, text = '2'). grid(row = 5, column = 0)
book_1 = Label(root, text = 'Harry Potter and The Half Blood Prince').grid(row = 5, column = 1)
author_1 = Label(root, text = 'J.K.Rowling').grid(row = 5, column = 2)
update_1 = Button(root, text = 'CHANGE').grid(row = 5, column = 3)

checkbox_2 = Checkbutton(root, text = '3'). grid(row = 6, column = 0)
book_2 = Label(root, text = 'Harry Potter and The Half Blood Prince').grid(row = 6, column = 1)
author_2 = Label(root, text = 'J.K.Rowling').grid(row = 6, column = 2)
update_2 = Button(root, text = 'CHANGE').grid(row = 6, column = 3)

# ---------------------------------------------------------
root.mainloop()