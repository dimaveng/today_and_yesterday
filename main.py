from tkinter import *

window = Tk()
window.geometry = "300x400"
window.title = "РОЗКЛАД ЗАНЯТЬ"

firstLabel = Label(window, text="Урок 1: оберіть день", font="Arial 12")
firstLabel.pack()

secondLabel = Label(window, text="Урок 2: оберіть день", font="Arial 12")
secondLabel.pack()

thirdLabel = Label(window, text="Урок 3: оберіть день", font="Arial 12")
thirdLabel.pack()

fourthLabel = Label(window, text="Урок 4: оберіть день", font="Arial 12")
fourthLabel.pack()

fifthLabel = Label(window, text="Урок 5: оберіть день", font="Arial 12")
fifthLabel.pack()

sixthLabel = Label(window, text="Урок 6: оберіть день", font="Arial 12")
sixthLabel.pack()

seventhLabel = Label(window, text="Урок 7: оберіть день", font="Arial 12")
seventhLabel.pack()

main_menu = Tk.Menu(window)
window.config(menu=main_menu)

days_menu = Menu(main_menu, tearoff=0)
days_menu.add_command(label="Понеділок", command=monday)
days_menu.add_command(label="Вівторок", command=tuesday)
days_menu.add_command(label="Середа", command=wednesday)
days_menu.add_command(label="Четвер", command=thursday)
days_menu.add_command(label="П'ятниця", command=friday)

main_menu.add_cascade(label="Обрати день неділі", menu=days_menu)

window.config(menu=main_menu)
window.mainloop()