from tkinter import *


class root(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        # Setup Menu
        MainMenu(self)
        # Setup Frame
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for Frm in (StartPage, PageOne, PageTwo):
            frame = Frm(container, self)
            self.frames[Frm] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text="Welcome to Start Page", fg="White", bg="Black")
        label.pack(padx=15, pady=15, fill=X)
        page_one = Button(self, text="Page One", fg="Blue", command=lambda: controller.show_frame(PageOne))
        page_one.pack(padx=10, pady=10)
        page_two = Button(self, text="Page Two", fg="Blue", command=lambda: controller.show_frame(PageTwo))
        page_two.pack(padx=10, pady=10)


class PageOne(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text="Page One", fg="White", bg="Black")
        label.pack(padx=10, pady=10, fill=X)

        start_page = Button(self, text="Start Page", fg="Brown", command=lambda: controller.show_frame(StartPage))
        start_page.pack(padx=10, pady=10)
        page_two = Button(self, text="Page Two", fg="Green", command=lambda: controller.show_frame(PageTwo))
        page_two.pack(padx=10, pady=10)
        self.clickbutton = Button(self, text="Enter your Details", fg="Blue", command=self.show_entry_fields)
        self.clickbutton.pack(padx=10, pady=10)

    def show_entry_fields(self):
        parent = Tk()
        label1 = Label(parent, text="First Name")
        label1.grid(row=0, column=0)
        label2 = Label(parent, text="Last Name")
        label2.grid(row=1, column=0)
        label2 = Label(parent, text="Email ID")
        label2.grid(row=2, column=0)
        label2 = Label(parent, text="Mobile Number")
        label2.grid(row=3, column=0)

        e1 = Entry(parent)
        e2 = Entry(parent)
        e3 = Entry(parent)
        e4 = Entry(parent)

        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        e3.grid(row=2, column=1)
        e4.grid(row=3, column=1)

        Button(parent, text='Quit', command=parent.quit).grid(row=6, column=0, sticky=W, pady=4)
        Button(parent, text='Save').grid(row=6, column=1, sticky=W, pady=4)



class PageTwo(Frame):
    def __init__(self, parent1, controller):
        Frame.__init__(self, parent1)

        label = Label(self, text="Page Two", fg="White", bg="Black")
        label.pack(padx=10, pady=10, fill=X)

        start_page = Button(self, text="Start Page", fg="Brown", command=lambda: controller.show_frame(StartPage))
        start_page.pack(padx=10, pady=10)
        page_one = Button(self, text="Page One", fg="Green", command=lambda: controller.show_frame(PageOne))
        page_one.pack(padx=10, pady=10)
        self.clickbutton = Button(self, text="Click Here", fg="Blue", command=self.text_image)
        self.clickbutton.pack(padx=10, pady=10)
        self.quitbutton = Button(self, text="Exit", fg="Red", command=self.quit)
        self.quitbutton.pack(padx=10, pady=10, side=BOTTOM)


    def text_image(self):
        photo = PhotoImage(file="img.png")
        label = Label(image=photo)
        label.image = photo  # to keep a reference
        label.pack(padx=5, pady=5)
        w = Label(text="Hello, world!\n""This is the image of the Earth seen from the outer space. The Earth looks beautiful.", height=8)
        w.pack()


class MainMenu:
    def __init__(self, master):
        mymenu = Menu(master)
        master.config(menu=mymenu)

        submenu = Menu(mymenu)
        mymenu.add_cascade(label="File", menu=submenu)
        submenu.add_command(label="New")
        submenu.add_command(label="Open")
        submenu.add_command(label="Save")
        submenu.add_separator()
        submenu.add_command(label="Projects")
        submenu.add_command(label="Exit", command=quit)

        newmenu = Menu(mymenu)
        mymenu.add_cascade(label="Edit", menu=newmenu)
        newmenu.add_command(label="Cut")
        newmenu.add_command(label="Copy")
        newmenu.add_command(label="Paste")
        newmenu.add_separator()
        newmenu.add_command(label="Find")
        newmenu.add_command(label="Replace")

app = root()
app.mainloop()
