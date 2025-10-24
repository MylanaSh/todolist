import tkinter as tk
from tkinter import ttk, Text
import tkinter.messagebox as messagebox
from datetime import datetime  #для фільтрів по даті
import json

root = tk.Tk()
root.title("Список завдань (To-Do Manager)")
root.state('zoomed')
root.configure(bg="#ffafcc")
icon = tk.PhotoImage(file='Снимок экрана 2025-10-14 101900.png')
root.iconphoto(False, icon)

#верхній блок - додавання завдання
frame_input = ttk.LabelFrame(root, text="Додати нове завдання", padding=10)
frame_input.pack(fill="x", padx=10, pady=10)

#назва
ttk.Label(frame_input, text="Назва завдання:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry_title = ttk.Entry(frame_input, width=40)
entry_title.grid(row=0, column=1, sticky="w", padx=5, pady=5)

#опис
ttk.Label(frame_input, text="Опис:").grid(row=1, column=0, sticky="nw", padx=5, pady=5)
text_description = Text(frame_input, width=40, height=4)
text_description.grid(row=1, column=1, sticky="w", padx=5, pady=5)

#дедлайн
ttk.Label(frame_input, text="Дедлайн (д-м-р):").grid(row=2, column=0, sticky="w", padx=5, pady=5)
entry_deadline = ttk.Entry(frame_input, width=20)
entry_deadline.grid(row=2, column=1, sticky="w", padx=5, pady=5)

#пріоритет
ttk.Label(frame_input, text="Пріоритет:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
combo_priority = ttk.Combobox(frame_input, values=["Високий", "Середній", "Низький"], state="readonly")
combo_priority.grid(row=3, column=1, sticky="w", padx=5, pady=5)

#категорія
ttk.Label(frame_input, text="Категорія:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
combo_category = ttk.Combobox(frame_input, values=["Робота", "Навчання", "Особисте", "Покупки"], state="readonly")
combo_category.grid(row=4, column=1, sticky="w", padx=5, pady=5)

#статус
status_var = tk.BooleanVar()
check_status = ttk.Checkbutton(frame_input, text="Виконано", variable=status_var)
check_status.grid(row=5, column=1, sticky="w", padx=5, pady=5)

#кнопка додавання
btn_add = tk.Button(frame_input, text="Додати завдання", bg="#a53860", fg="white")
btn_add.grid(row=6, column=1, sticky="w", pady=10)

#основна область (ліворуч - список, праворуч - керування)
main_frame = tk.Frame(root, bg="#ffafcc")
main_frame.pack(fill="both", expand=True, padx=10, pady=5)

#ліва частина: пошук, фільтри, список завдань
left_frame = tk.Frame(main_frame, bg="#ffafcc")
left_frame.pack(side="left", fill="both", expand=True, padx=(0, 5))

#пошук і фільтри
frame_filters = ttk.LabelFrame(left_frame, text="Пошук і фільтри", padding=10)
frame_filters.pack(fill="x", pady=5)

ttk.Label(frame_filters, text="Пошук за назвою:").grid(row=0, column=0, padx=5, pady=5)
entry_search = ttk.Entry(frame_filters, width=30)
entry_search.grid(row=0, column=1, padx=5, pady=5)
btn_search = tk.Button(frame_filters, text="Знайти", bg="#a53860", fg="white")
btn_search.grid(row=0, column=2, padx=5, pady=5)
btn_search = tk.Button(frame_filters, text="Знайти", bg="#a53860", fg="white")
btn_search.grid(row=0, column=2, padx=5, pady=5)

ttk.Label(frame_filters, text="Категорія:").grid(row=1, column=0, padx=5, pady=5)
combo_filter_category = ttk.Combobox(frame_filters, values=["Усі", "Робота", "Навчання", "Особисте", "Покупки"], state="readonly")
combo_filter_category.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_filters, text="Пріоритет:").grid(row=1, column=2, padx=5, pady=5)
combo_filter_priority = ttk.Combobox(frame_filters, values=["Усі", "Високий", "Середній", "Низький"], state="readonly")
combo_filter_priority.grid(row=1, column=3, padx=5, pady=5)

ttk.Label(frame_filters, text="Статус:").grid(row=1, column=4, padx=5, pady=5)
combo_filter_status = ttk.Combobox(frame_filters, values=["Усі", "Виконані", "Невиконані"], state="readonly")
combo_filter_status.grid(row=1, column=5, padx=5, pady=5)

btn_today = tk.Button(frame_filters, text="Завдання на сьогодні", bg="#a53860", fg="white")
btn_today.grid(row=1, column=6, padx=5, pady=5)

btn_sort = tk.Button(frame_filters, text="Сортувати за дедлайном", bg="#a53860", fg="white")
btn_sort.grid(row=1, column=4, padx=5, pady=5)

# Список завдань
frame_list = ttk.LabelFrame(left_frame, text="Список завдань", padding=10)
frame_list.pack(fill="both", expand=True, pady=10)

listbox_tasks = tk.Listbox(frame_list, height=15, selectmode="extended")
listbox_tasks.pack(fill="both", expand=True, side="left")

scrollbar = ttk.Scrollbar(frame_list, orient="vertical", command=listbox_tasks.yview)
scrollbar.pack(side="right", fill="y")
listbox_tasks.config(yscrollcommand=scrollbar.set)

#права частина: керування та статистика
right_frame = tk.Frame(main_frame, bg="#ffafcc")
right_frame.pack(side="right", fill="y", padx=(5, 0))

#фрейм керування
frame_actions = ttk.LabelFrame(right_frame, text="Керування завданнями", padding=10)
frame_actions.pack(fill="x", pady=10)

ttk.Label(frame_actions, text="Видалити за назвою:").grid(row=0, column=0, padx=5, pady=5)
entry_delete = ttk.Entry(frame_actions, width=25)
entry_delete.grid(row=1, column=0, padx=5, pady=5)

ttk.Label(frame_filters, text="Статус:").grid(row=2, column=0, padx=5, pady=5)
combo_filter_status = ttk.Combobox(frame_filters, values=["Усі", "Виконані", "Невиконані"], state="readonly")
combo_filter_status.grid(row=2, column=1, padx=5, pady=5)

btn_delete_one = tk.Button(frame_actions, text="Видалити вибране", bg="#a53860", fg="white")
btn_delete_one.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

btn_delete_done = tk.Button(frame_actions, text="Видалити виконані", bg="#a53860", fg="white")
btn_delete_done.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

btn_delete_all = tk.Button(frame_actions, text="Видалити всі", bg="#a53860", fg="white")
btn_delete_all.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

btn_save = tk.Button(frame_actions, text="Зберегти у файл", bg="#a53860", fg="white")
btn_save.grid(row=5, column=0, padx=5, pady=10, sticky="ew")

btn_reset_filters = tk.Button(frame_filters, text="Скинути фільтри", bg="#a53860", fg="white")
btn_reset_filters.grid(row=2, column=4, padx=5, pady=5)


#статистика
frame_stats = ttk.LabelFrame(right_frame, text="Статистика", padding=10)
frame_stats.pack(fill="x", pady=(0, 10))

label_done = ttk.Label(frame_stats, text="Виконано: 0")
label_done.pack(anchor="w", padx=5, pady=3)

label_not_done = ttk.Label(frame_stats, text="Невиконано: 0")
label_not_done.pack(anchor="w", padx=5, pady=3)

tasks = []

#ФУНКЦІЇ
def update_listbox(filtered=None):

    listbox_tasks.delete(0, tk.END)
    current_list = filtered if filtered is not None else tasks

    for i, task in enumerate(current_list):
        text = f"{task['title']} [{task['category']}] — {task['deadline']}"
        listbox_tasks.insert(tk.END, text)

        if task["done"]:
            listbox_tasks.itemconfig(i, {"fg": "gray"})
        elif task["priority"] == "Високий":
            listbox_tasks.itemconfig(i, {"fg": "red"})
        elif task["priority"] == "Середній":
            listbox_tasks.itemconfig(i, {"fg": "orange"})
        else:
            listbox_tasks.itemconfig(i, {"fg": "green"})

    update_stats()


def update_stats():
    done = sum(1 for t in tasks if t["done"])
    not_done = len(tasks) - done
    label_done.config(text=f"Виконано: {done}")
    label_not_done.config(text=f"Невиконано: {not_done}")


def add_task():
    title = entry_title.get().strip()
    description = text_description.get("1.0", "end").strip()
    deadline = entry_deadline.get().strip()
    priority = combo_priority.get()
    category = combo_category.get()
    done = status_var.get()

    if not title:
        messagebox.showerror("ERROR", "Назва завдання не може бути порожньою!")
        return

    task = {
        "title": title,
        "description": description,
        "deadline": deadline,
        "priority": priority,
        "category": category,
        "done": done
    }

    tasks.append(task)
    update_listbox()

    entry_title.delete(0, tk.END)
    text_description.delete("1.0", tk.END)
    entry_deadline.delete(0, tk.END)
    combo_priority.set("")
    combo_category.set("")
    status_var.set(False)

def delete_by_name(_event):
    name = entry_delete.get().strip()
    if not name:
        messagebox.showerror("Попередження","Введіть назву завдання для видалення!")
        return
    found_tasks = [t for t in tasks if t["title"].lower() == name.lower()]
    if not found_tasks:
        messagebox.showinfo("Інформація", f"Завдання '{name}' не знайдено.")
        return
    if messagebox.askyesno("Підтвердження", f"Видалити {len(found_tasks)} завдання з назвою '{name}'?"):
        for t in found_tasks:
            tasks.remove(t)
        update_listbox()
        messagebox.showinfo("Успіх", f"Завдання '{name}' видалено.")
        entry_delete.delete(0, tk.END)
def delete_selected():
    selected = listbox_tasks.curselection()
    if not selected:
        messagebox.showinfo("INFO", "Оберіть завдання для видалення.")
        return

    for index in reversed(selected):
        del tasks[index]
    update_listbox()

def delete_all():
    if messagebox.askyesno("CONFIRMATION", "Видалити всі завдання?"):
        tasks.clear()
        update_listbox()


#фільтрація та пошук
def search_task():    #шукає завдання за ключовим словом у назві або описі
    keyword = entry_search.get().lower().strip()
    if not keyword:
        update_listbox()
        return

    filtered = [t for t in tasks if keyword in t["title"].lower() or keyword in t["description"].lower()]
    update_listbox(filtered)


def filter_tasks():     #фільтрує за категорією, пріоритетом і статусом
    cat = combo_filter_category.get()
    pr = combo_filter_priority.get()
    st = combo_filter_status.get()

    filtered = tasks

    if cat and cat != "Усі":
        filtered = [t for t in filtered if t["category"] == cat]
    if pr and pr != "Усі":
        filtered = [t for t in filtered if t["priority"] == pr]
    if st == "Виконані":
        filtered = [t for t in filtered if t["done"]]
    elif st == "Невиконані":
        filtered = [t for t in filtered if not t["done"]]

    update_listbox(filtered)


def show_today_tasks():     #показує завдання з дедлайном на сьогодні
    today = datetime.now().strftime("%d-%m-%Y")
    filtered = [t for t in tasks if t["deadline"] == today]
    update_listbox(filtered)


def reset_filters():      #скидає всі фільтри
    entry_search.delete(0, tk.END)
    combo_filter_category.set("Усі")
    combo_filter_priority.set("Усі")
    combo_filter_status.set("Усі")
    update_listbox()

def save_to_file():
    try:
        with open("tasks.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(tasks, ensure_ascii=False, indent=4))
            messagebox.showinfo("Успіх!","Файл збережено!")
    except FileNotFoundError:
        messagebox.showerror("Помилка!","Не вдалося зберегти файл!")

def load_from_file():
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            tasks.clear()
            tasks.extend(data)
        update_listbox()
    except FileNotFoundError:
        pass

#прив'язування кнопок
btn_add.config(command=add_task)
btn_delete_one.config(command=delete_selected)
btn_delete_all.config(command=delete_all)
btn_search.config(command=search_task)
combo_filter_category.bind("<<ComboboxSelected>>", lambda e: filter_tasks())
combo_filter_priority.bind("<<ComboboxSelected>>", lambda e: filter_tasks())
combo_filter_status.bind("<<ComboboxSelected>>", lambda e: filter_tasks())
btn_today.config(command=show_today_tasks)
btn_reset_filters.config(command=reset_filters)
btn_save.config(command=save_to_file)
entry_delete.bind("<Return>", delete_by_name)

load_from_file() #завантаження збереженого файлу
root.mainloop()
