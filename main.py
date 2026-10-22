from tkinter import *

window = Tk()
window.geometry("400x400")
window.title("РОЗКЛАД ЗАНЯТЬ")

def show_day(l1, l2, l3, l4, l5, l6, l7):
    firstLabel.config(text="Урок 1: " + l1)
    secondLabel.config(text="Урок 2: " + l2)
    thirdLabel.config(text="Урок 3: " + l3)
    fourthLabel.config(text="Урок 4: " + l4)
    fifthLabel.config(text="Урок 5: " + l5)
    sixthLabel.config(text="Урок 6: " + l6)
    seventhLabel.config(text="Урок 7: " + l7)

def monday():
    show_day("Фізика", "Фізична культура", "Географія", "Всесвітня історія",
             "Біологія", "Алгебра", "Українська література")

def tuesday():
    show_day("Англійська мова", "Геометрія", "Англ. мова/Українська література",
             "Музика", "Географія", "Здоров'я, Безпека, Добробут", "Українська мова")

def wednesday():
    show_day("Фізична культура", "Зарубіжна література", "Алгебра",
             "Англійська мова", "Трудове навчання", "Трудове навчання",
             "Англійська мова")

def thursday():
    show_day("Геометрія", "Українська мова", "Англійська мова",
             "Історія України", "Фізика", "Інформатика", "Мистецтво")

def friday():
    show_day("Фізична культура", "Біологія", "Хімія",
             "Історія України/Громад. освіта", "Українська мова", "Алгебра",
             "Зарубіжна література")

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

main_menu = Menu(window)

days_menu = Menu(main_menu, tearoff=0)
days_menu.add_command(label="Понеділок", command=monday)
days_menu.add_command(label="Вівторок", command=tuesday)
days_menu.add_command(label="Середа", command=wednesday)
days_menu.add_command(label="Четвер", command=thursday)
days_menu.add_command(label="П'ятниця", command=friday)

main_menu.add_cascade(label="Обрати день тижня", menu=days_menu)

window.config(menu=main_menu)
window.mainloop()