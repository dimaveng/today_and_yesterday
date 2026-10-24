from tkinter import *
from tkinter import simpledialog
import os
import json
import pyglet

pyglet.font.add_file("./Minecraft_1.1.ttf")

window = Tk()
window.geometry("400x650")
window.title("РОЗКЛАД ЗАНЯТЬ")

schedule = {
    "Понеділок": ["Фізика", "Фізична культура", "Географія", "Всесвітня історія",
                  "Біологія", "Алгебра", "Українська література"],
    "Вівторок": ["Англійська мова", "Геометрія", "Англ. мова/Українська література",
                 "Музика", "Географія", "Здоров'я, Безпека, Добробут", "Українська мова"],
    "Середа": ["Фізична культура", "Зарубіжна література", "Алгебра",
               "Англійська мова", "Трудове навчання", "Трудове навчання",
               "Англійська мова"],
    "Четвер": ["Геометрія", "Українська мова", "Англійська мова",
               "Історія України", "Фізика", "Інформатика", "Мистецтво"],
    "П'ятниця": ["Фізична культура", "Біологія", "Хімія",
                 "Історія України/Громад. освіта", "Українська мова", "Алгебра",
                 "Зарубіжна література"],
}

HW_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "homework.json")

def load_homework():
    empty = {day: [""] * 7 for day in schedule}
    if not os.path.exists(HW_FILE):
        return empty
    try:
        with open(HW_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        return empty
    for day, items in data.items():
        if day in empty:
            for i, hw in enumerate(items[:7]):
                empty[day][i] = hw
    return empty

def save_homework():
    with open(HW_FILE, "w", encoding="utf-8") as f:
        json.dump(homework, f, ensure_ascii=False, indent=2)

homework = load_homework()

current_day = None

def show_day(day):
    global current_day
    current_day = day
    for i in range(7):
        lesson_labels[i].config(text=f"Урок {i + 1}: {schedule[day][i]}")
        hw = homework[day][i]
        hw_labels[i].config(text="ДЗ: " + (hw if hw else "—"))

def edit_homework(i):
    if current_day is None:
        return
    text = simpledialog.askstring(
        "Домашнє завдання",
        f"ДЗ з уроку {i + 1} ({schedule[current_day][i]}):",
        initialvalue=homework[current_day][i],
        parent=window,
    )
    if text is not None:
        homework[current_day][i] = text
        save_homework()
        show_day(current_day)

lesson_labels = []
hw_labels = []

for i in range(7):
    lesson = Label(window, text=f"Урок {i + 1}: оберіть день",
                   font=("Minecraft 1.1", 12))
    lesson.pack()
    lesson_labels.append(lesson)

    hw = Label(window, text="", font=("Minecraft 1.1", 10),
               fg="gray", wraplength=380, cursor="hand2")
    hw.pack()
    hw.bind("<Button-1>", lambda event, n=i: edit_homework(n))
    hw_labels.append(hw)

main_menu = Menu(window)

days_menu = Menu(main_menu, tearoff=0)
for day in schedule:
    days_menu.add_command(label=day, command=lambda d=day: show_day(d))

main_menu.add_cascade(label="Обрати день тижня", menu=days_menu)

window.config(menu=main_menu)
window.mainloop()