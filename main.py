import tkinter.messagebox as msg
from tkinter import *
import tkinter.ttk as ttk
import tkinter.filedialog as filebox
from PIL import Image


def image_format():
    def format_now(input_path, output_path, output_format):  # type: (str, str, str) -> None
        image = Image.open(input_path)

        image.save(output_path, format=output_format.lower())

        msg.showinfo("Finish", "成功转换！")

    def choose_file():
        file = filebox.askopenfilename()
        SelectVariable.set(file)
        inputpath.insert(0, SelectVariable.get())

    def save_file():
        file = filebox.asksaveasfilename()
        SaveVariable.set(file)
        outputpath.insert(0, SaveVariable.get())

    top = Toplevel()
    top.attributes("-topmost", True)
    top.geometry("1060x40")

    SelectVariable = StringVar()
    SaveVariable = StringVar()
    formatVar = StringVar()

    main = Frame(top)
    main.place(x=0, y=0, width=1060, height=40)

    inputpath = Entry(main)
    Label(main, text="图片路径").grid(column=0, row=0)
    Button(main, text="选择", command=choose_file).grid(column=2, row=0)
    inputpath.grid(column=1, row=0)

    choose = ttk.Combobox(main, textvariable=formatVar)
    Label(main, text="要转换的图片格式").grid(column=3, row=0)
    choose.grid(column=4, row=0)
    choose['value'] = ("png", "jpg", "ico", "icns", "jpeg")
    choose.current(0)

    outputpath = Entry(main)
    Label(main, text="保存路径").grid(column=5, row=0)
    Button(main, text="选择", command=save_file).grid(column=7, row=0)
    outputpath.grid(column=6, row=0)

    start = Button(main, text="开始转换", command=lambda: format_now(
        inputpath.get(), outputpath.get(), formatVar.get()))
    start.grid(column=8, row=0)

    top.mainloop()


root = Tk()
root.geometry("800x600")
Label(root, text="欢迎", font=("", 30)).place(x=10, y=10, width=120, height=80)
Button(root, text="图片格式转换", command=image_format,
       relief=FLAT).place(x=140, y=50, width=120, height=40)

root.mainloop()
