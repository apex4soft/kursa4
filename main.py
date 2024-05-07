import os
import webbrowser

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from pygame import mixer


def install_wsl():
    try:
        # Открываем терминал Windows
        os.system("start cmd /k wsl --install -d Ubuntu")
    finally:
        pass


def open_terminal(question_number):
    try:
        # Открываем терминал Linux
        os.system(f'gnome-terminal -- bash -c "chmod +x ./Scripts/{question_number}.sh"')
        os.system(f'gnome-terminal -- bash -c ./Scripts/{question_number}.sh')
    finally:
        # Открываем терминал WSL Ubuntu
        os.system(f'start wsl -d Ubuntu bash -c "cd ./Scripts && ./{question_number}.sh"')


def window_close(this_window):
    global window_open
    window_open = False
    this_window.destroy()


def Intro_list():
    global window_open
    if window_open:
        return
    win_intro = Toplevel(root)
    win_intro.title('Introduction')
    win_intro.iconphoto(False, icon)
    win_intro.geometry("800x300")
    win_intro.resizable(0, 0)
    win_intro.focus()
    win_intro.wm_attributes("-topmost", 1)
    win_intro.protocol("WM_DELETE_WINDOW", lambda this_window=win_intro: window_close(this_window))
    window_open = True
    canvas1 = Canvas(win_intro, width=800, height=300, background='yellow')
    canvas1.pack()
    win_info_text = (
        f'Приветствую в изучении ОС Linux!\n\n'
        f'В этом приложении вы изучите основные команды\n'
        f'и примеры их использованиея\n'
        f'Также немного затронем теорию Bash скриптов\n\n'
        f'Для получения документации всех команд введите в терминал команду "MAN"\n'
        f'Для получения документации ключей для команды введите "команда" -help\n\n'
        f'!ВНИМАНИЕ!\n'
        f'НЕ УДАЛЯЙТЕ И НЕ ИЗМЕНЯЙТЕ ФАЙЛЫ, КОТОРЫЕ НЕ УКАЗАНЫ В ЗАДАНИЯХ\n'
        f'ЭТО ПОМОЖЕТ ИЗБЕЖАТЬ ПОЛОМКИ ПРИЛОЖЕНИЯ'
    )  # Текст intro
    canvas1.create_text(375, 150, text=win_info_text, font=('Arial', 14), justify=CENTER, anchor=CENTER)


def Creators():
    try:
        # Открываем терминал Linux
        os.system(f'gnome-terminal -- bash -c "chmod +x ./Creators.sh"')
        os.system(f'gnome-terminal -- bash -c ./Creators.sh')
    finally:
        # Открываем терминал WSL Ubuntu
        os.system(f'start wsl -d Ubuntu bash -c "./Creators.sh"')


def Onl_Term():
    webbrowser.open_new("https://bellard.org/jslinux/vm.html?url=alpine-x86.cfg&mem=192")


def Tasks():
    # Чтение данных из файла
    with open('Scripts/Tasks.txt', 'r', encoding='utf-8') as file:
        r_tasks = file.read()
    win_task = Tk()
    win_task.title("Решённые задачи")
    label = Label(win_task, text=r_tasks)
    label.pack()


def His():
    # Чтение данных из файла
    with open('Scripts/his.txt', 'r', encoding='utf-8') as file:
        r_tasks = file.read()
    win_task = Tk()
    win_task.title("История Linux")
    label = Label(win_task, text=r_tasks)
    label.pack()


def increase_volume():
    global volume
    global sound1
    if volume < 1:
        volume += 0.1
    sound1 = mixer.music.set_volume(volume)


def decrease_volume():
    global volume
    global sound1
    if volume > 0:
        volume -= 0.1
    sound1 = mixer.music.set_volume(volume)


# Музыка
volume = 0.3
mixer.init()
sound1 = mixer.music.set_volume(volume)
mixer.music.load("Music/1.mp3")
mixer.music.play(-1)

# Окно
root = Tk()  # создаем корневой объект - окно
root.title("Learn Linux")  # устанавливаем заголовок окна
icon = PhotoImage(file='IMG/LinuxIcon.png')  # иконка в углу
root.iconphoto(False, icon)
root.geometry("1200x750+450+150")  # устанавливаем размеры окна
root.resizable(0, 0)

style = ttk.Style()
style.theme_use("clam")
# Toolbutton дизайн для (синик) кнопок доков
style.configure('buttondesign1.Toolbutton', font="Arial 18", width=19, anchor="center")
style.map('buttondesign1.Toolbutton', background=[('active', 'yellow'), ('!disabled', 'lightblue')], foreground=[('active', 'black'), ('!disabled', 'black')])
# Toolbutton дизайн для (зеленых) кнопок легких задач
style.configure('buttondesign2.Toolbutton', font="Arial 24", width=2, anchor="center")
style.map('buttondesign2.Toolbutton', background=[('active', 'yellow'), ('!disabled', 'green')], foreground=[('active', 'black'), ('!disabled', 'black')])
# Toolbutton дизайн для (оранжевых) кнопок средних задач
style.configure('buttondesign3.Toolbutton', font="Arial 24", width=2, anchor="center")
style.map('buttondesign3.Toolbutton', background=[('active', 'yellow'), ('!disabled', 'orange')], foreground=[('active', 'black'), ('!disabled', 'black')])
# Toolbutton дизайн для (красных) кнопок тяжелых задач
style.configure('buttondesign4.Toolbutton', font="Arial 24", width=2, anchor="center")
style.map('buttondesign4.Toolbutton', background=[('active', 'yellow'), ('!disabled', 'red')], foreground=[('active', 'black'), ('!disabled', 'black')])
# Toolbutton дизайн для (пурпурных) кнопок bash скриптов
style.configure('buttondesign5.Toolbutton', font="Arial 24", width=2, anchor="center")
style.map('buttondesign5.Toolbutton', background=[('active', 'yellow'), ('!disabled', 'purple')], foreground=[('active', 'black'), ('!disabled', 'black')])
# Toolbutton дизайн для (синик) кнопок звука
style.configure('buttondesign6.Toolbutton', font="Arial 24", width=2, anchor="center")
style.map('buttondesign6.Toolbutton', background=[('active', 'yellow'), ('!disabled', 'lightblue')], foreground=[('active', 'black'), ('!disabled', 'black')])

canvas = Canvas(root, width=1200, height=750)
canvas.pack()

# фоновое изображение
image_path = "./IMG/LBG.png"
background_image = ImageTk.PhotoImage(Image.open(image_path))
canvas.create_image(0, 0, anchor=NW, image=background_image)

# Кнопка Скачать WSL Ubuntu
button = ttk.Button(root, text='Скачать WSL Ubuntu', command=install_wsl, style='buttondesign1.Toolbutton', cursor='hand2')
button.place(x=920, y=675)

window_open = False

# Кнопка уменшить громкость
button = ttk.Button(root, text='<', command=decrease_volume, style='buttondesign6.Toolbutton', cursor='hand2')
button.place(x=1080, y=625)

# Кнопка увеличить громкость
button = ttk.Button(root, text='>', command=increase_volume, style='buttondesign6.Toolbutton', cursor='hand2')
button.place(x=1130, y=625)

# Кнопка Введение
button = ttk.Button(root, text='Введение', command=Intro_list, style='buttondesign1.Toolbutton', cursor='hand2')
button.place(x=620, y=675)

# Кнопка Разработчики
button = ttk.Button(root, text='Разработчики', command=Creators, style='buttondesign1.Toolbutton', cursor='hand2')
button.place(x=20, y=675)

# Кнопка Решенные задачи
button = ttk.Button(root, text='Решенные задачи', command=Tasks, style='buttondesign1.Toolbutton', cursor='hand2')
button.place(x=20, y=625)

# Кнопка История Linux
button = ttk.Button(root, text='История Linux', command=His, style='buttondesign1.Toolbutton', cursor='hand2')
button.place(x=20, y=575)

# Кнопка Онлайн Терминал
button = ttk.Button(root, text='Онлайн Терминал', command=Onl_Term, style='buttondesign1.Toolbutton', cursor='hand2')
button.place(x=320, y=675)

# Кнопка 1
button = ttk.Button(root, text='1', command=lambda: open_terminal(1), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
button.place(x=50, y=50)

# Кнопка 2
button = ttk.Button(root, text='2', command=lambda: open_terminal(2), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
button.place(x=125, y=50)

# Кнопка 3
button = ttk.Button(root, text='3', command=lambda: open_terminal(3), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
button.place(x=200, y=50)

# Кнопка 4
button = ttk.Button(root, text='4', command=lambda: open_terminal(4), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
button.place(x=275, y=50)

# Кнопка 5
button = ttk.Button(root, text='5', command=lambda: open_terminal(5), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
button.place(x=350, y=50)

# Кнопка 6
button = ttk.Button(root, text='6', command=lambda: open_terminal(6), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
button.place(x=425, y=50)

# Кнопка 7
button = ttk.Button(root, text='7', command=lambda: open_terminal(7), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
button.place(x=500, y=50)

# Кнопка 8
button = ttk.Button(root, text='8', command=lambda: open_terminal(8), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
button.place(x=575, y=50)

# Кнопка 9
button = ttk.Button(root, text='9', command=lambda: open_terminal(9), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
button.place(x=650, y=50)

# Кнопка 10
button = ttk.Button(root, text='10', command=lambda: open_terminal(10), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
button.place(x=725, y=50)

# Кнопка 11
button = ttk.Button(root, text='11', command=lambda: open_terminal(11), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
button.place(x=800, y=50)

# Кнопка 12
button = ttk.Button(root, text='12', command=lambda: open_terminal(12), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
button.place(x=875, y=50)

# Кнопка 13
button = ttk.Button(root, text='13', command=lambda: open_terminal(13), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
button.place(x=950, y=50)

# Кнопка 14
button = ttk.Button(root, text='14', command=lambda: open_terminal(14), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
button.place(x=1025, y=50)

# Кнопка 15
button = ttk.Button(root, text='15', command=lambda: open_terminal(15), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
button.place(x=1100, y=50)

# Кнопка 16
button = ttk.Button(root, text='16', command=lambda: open_terminal(16), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
button.place(x=50, y=125)

# Кнопка 17
button = ttk.Button(root, text='17', command=lambda: open_terminal(17), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
button.place(x=125, y=125)

# Кнопка 18
button = ttk.Button(root, text='18', command=lambda: open_terminal(18), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
button.place(x=200, y=125)

# Кнопка 19
button = ttk.Button(root, text='19', command=lambda: open_terminal(19), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
button.place(x=275, y=125)

# Кнопка 20
button = ttk.Button(root, text='20', command=lambda: open_terminal(20), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
button.place(x=350, y=125)

# Кнопка 21
button = ttk.Button(root, text='21', command=lambda: open_terminal(21), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
button.place(x=425, y=125)

# Кнопка 22
button = ttk.Button(root, text='22', command=lambda: open_terminal(22), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
button.place(x=500, y=125)

# Кнопка 23
button = ttk.Button(root, text='23', command=lambda: open_terminal(23), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
button.place(x=575, y=125)

# Кнопка 24
button = ttk.Button(root, text='24', command=lambda: open_terminal(24), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
button.place(x=650, y=125)

# Кнопка 25
button = ttk.Button(root, text='25', command=lambda: open_terminal(25), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
button.place(x=725, y=125)

# Кнопка 26
button = ttk.Button(root, text='26', command=lambda: open_terminal(26), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
button.place(x=800, y=125)

# Кнопка 27
button = ttk.Button(root, text='27', command=lambda: open_terminal(27), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
button.place(x=875, y=125)

# Кнопка 28
button = ttk.Button(root, text='28', command=lambda: open_terminal(28), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
button.place(x=950, y=125)

# Кнопка 29
button = ttk.Button(root, text='29', command=lambda: open_terminal(29), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
button.place(x=1025, y=125)

# Кнопка 30
button = ttk.Button(root, text='30', command=lambda: open_terminal(30), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
button.place(x=1100, y=125)

# Кнопка 31
button = ttk.Button(root, text='31', command=lambda: open_terminal(31), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
button.place(x=50, y=200)

# Кнопка 32
button = ttk.Button(root, text='32', command=lambda: open_terminal(32), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
button.place(x=125, y=200)

# Кнопка 33
button = ttk.Button(root, text='33', command=lambda: open_terminal(33), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
button.place(x=200, y=200)

# Кнопка 34
button = ttk.Button(root, text='34', command=lambda: open_terminal(34), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
button.place(x=275, y=200)

# Кнопка 35
button = ttk.Button(root, text='35', command=lambda: open_terminal(35), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
button.place(x=350, y=200)

# Кнопка 36
button = ttk.Button(root, text='36', command=lambda: open_terminal(36), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
button.place(x=425, y=200)

# Кнопка 37
button = ttk.Button(root, text='37', command=lambda: open_terminal(37), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
button.place(x=500, y=200)

# Кнопка 38
button = ttk.Button(root, text='38', command=lambda: open_terminal(38), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
button.place(x=575, y=200)

# Кнопка 39
button = ttk.Button(root, text='39', command=lambda: open_terminal(39), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
button.place(x=650, y=200)

# Кнопка 40
button = ttk.Button(root, text='40', command=lambda: open_terminal(40), style='buttondesign4.Toolbutton', padding=10, cursor='hand2')
button.place(x=725, y=200)

# Кнопка 41
button = ttk.Button(root, text='41', command=lambda: open_terminal(41), style='buttondesign4.Toolbutton', padding=10, cursor='hand2')
button.place(x=800, y=200)

# Кнопка 42
button = ttk.Button(root, text='42', command=lambda: open_terminal(42), style='buttondesign4.Toolbutton', padding=10, cursor='hand2')
button.place(x=875, y=200)

# Кнопка 43
button = ttk.Button(root, text='43', command=lambda: open_terminal(43), style='buttondesign4.Toolbutton', padding=10, cursor='hand2')
button.place(x=950, y=200)

# Кнопка 44
button = ttk.Button(root, text='44', command=lambda: open_terminal(44), style='buttondesign4.Toolbutton', padding=10, cursor='hand2')
button.place(x=1025, y=200)

# Кнопка 45
button = ttk.Button(root, text='45', command=lambda: open_terminal(45), style='buttondesign4.Toolbutton', padding=10, cursor='hand2')
button.place(x=1100, y=200)

# Кнопка 46
button = ttk.Button(root, text='46', command=lambda: open_terminal(46), style='buttondesign4.Toolbutton', padding=10, cursor='hand2')
button.place(x=50, y=275)

# Кнопка 47
button = ttk.Button(root, text='47', command=lambda: open_terminal(47), style='buttondesign4.Toolbutton', padding=10, cursor='hand2')
button.place(x=125, y=275)

# Кнопка 48
button = ttk.Button(root, text='48', command=lambda: open_terminal(48), style='buttondesign4.Toolbutton', padding=10, cursor='hand2')
button.place(x=200, y=275)


def but49():
    # Кнопка 49
    button = ttk.Button(root, text='49', command=lambda: open_terminal(49), style='buttondesign5.Toolbutton', padding=10, cursor='hand2')
    button.place(x=275, y=275)


tasks = 'Scripts/Tasks.txt'
with open(tasks, 'r') as file:
    line_count = sum(1 for line in file)

if line_count >= 48:
    but49()

# Кнопка 50
button = ttk.Button(root, text='50', command=lambda: open_terminal(50), style='buttondesign5.Toolbutton', padding=10, cursor='hand2')
button.place(x=50, y=350)

# Кнопка 51
button = ttk.Button(root, text='51', command=lambda: open_terminal(51), style='buttondesign5.Toolbutton', padding=10, cursor='hand2')
button.place(x=125, y=350)

# Кнопка 52
button = ttk.Button(root, text='52', command=lambda: open_terminal(52), style='buttondesign5.Toolbutton', padding=10, cursor='hand2')
button.place(x=200, y=350)

# Кнопка 53
button = ttk.Button(root, text='53', command=lambda: open_terminal(53), style='buttondesign5.Toolbutton', padding=10, cursor='hand2')
button.place(x=275, y=350)

root.mainloop()
