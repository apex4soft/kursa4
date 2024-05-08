import os
import webbrowser

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from pygame import mixer

class App:

    def install_wsl(self):
        try:
            # Открываем терминал Windows
            os.system("start cmd /k wsl --install -d Ubuntu")
        finally:
            pass

    def open_terminal(self, question_number):
        try:
            # Открываем терминал Linux
            os.system(f'gnome-terminal -- bash -c "chmod +x ./Scripts/{question_number}.sh"')
            os.system(f'gnome-terminal -- bash -c "cd ./Scripts; ./{question_number}.sh"')
        finally:
            # Открываем терминал WSL Ubuntu
            os.system(f'start wsl -d Ubuntu bash -c "cd ./Scripts && ./{question_number}.sh"')

    def window_close(self, this_window):
        self.window_open = False
        this_window.destroy()

    def Intro_list(self):
        if self.window_open:
            return
        win_intro = Toplevel(self.root)
        win_intro.title('Introduction')
        icon = PhotoImage(file='IMG/LinuxIcon.png')
        win_intro.iconphoto(False, icon)
        win_intro.geometry("800x300")
        win_intro.resizable(0, 0)
        win_intro.focus()
        win_intro.wm_attributes("-topmost", 1)
        win_intro.protocol("WM_DELETE_WINDOW", lambda this_window=win_intro: self.window_close(this_window))
        self.window_open = True
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

    def Creators(self):
        try:
            # Открываем терминал Linux
            os.system(f'gnome-terminal -- bash -c "chmod +x ./Creators.sh"')
            os.system(f'gnome-terminal -- bash -c ./Creators.sh')
        finally:
            # Открываем терминал WSL Ubuntu
            os.system(f'start wsl -d Ubuntu bash -c "./Creators.sh"')

    def Onl_Term(self):
        webbrowser.open_new("https://bellard.org/jslinux/vm.html?url=alpine-x86.cfg&mem=192")

    def Tasks(self):
        if self.window_open:
            return
        # Чтение данных из файла
        with open('Scripts/Tasks.txt', 'r', encoding='utf-8') as file:
            r_tasks = file.read()
        win_task = Tk()
        win_task.title("Решённые задачи")
        win_task.focus()
        win_task.wm_attributes("-topmost", 1)
        win_task.protocol("WM_DELETE_WINDOW", lambda this_window=win_task: self.window_close(this_window))
        self.window_open = True
        label = Label(win_task, text=r_tasks)
        label.pack()

    def His(self):
        if self.window_open:
            return
        # Чтение данных из файла
        with open('Scripts/his.txt', 'r', encoding='utf-8') as file:
            r_tasks = file.read()
        win_his = Tk()
        win_his.title("История Linux")
        win_his.focus()
        win_his.wm_attributes("-topmost", 1)
        win_his.protocol("WM_DELETE_WINDOW", lambda this_window=win_his: self.window_close(this_window))
        self.window_open = True
        label = Label(win_his, text=r_tasks)
        label.pack()

    def increase_volume(self):
        if self.volume < 1:
            self.volume += 0.1
        self.sound1 = mixer.music.set_volume(self.volume)

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 0.1
        self.sound1 = mixer.music.set_volume(self.volume)


    def __init__(self):
        self.window_open = False

        # Музыка
        self.volume = 0.3
        mixer.init()
        self.sound1 = mixer.music.set_volume(self.volume)
        mixer.music.load("Music/Vodila.mp3")
        mixer.music.play(-1)

        self.root = Tk()
        self.root.title("Learn Linux")
        icon = PhotoImage(file='IMG/LinuxIcon.png')
        self.root.iconphoto(False, icon)
        self.root.geometry("1200x750+450+150")
        self.root.resizable(0, 0)

        self.canvas = Canvas(self.root, width=1200, height=750)
        self.canvas.pack()

        # фоновое изображение
        image_path = "./IMG/LBG.png"
        background_image = ImageTk.PhotoImage(Image.open(image_path))
        self.canvas.create_image(0, 0, anchor=NW, image=background_image)

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

        # Кнопка Скачать WSL Ubuntu
        self.button = ttk.Button(self.root, text='Скачать WSL Ubuntu', command=self.install_wsl, style='buttondesign1.Toolbutton', cursor='hand2')
        self.button.place(x=920, y=675)

        # Кнопка Введение
        self.button = ttk.Button(self.root, text='Введение', command=self.Intro_list, style='buttondesign1.Toolbutton', cursor='hand2')
        self.button.place(x=620, y=675)

        # Кнопка Разработчики
        self.button = ttk.Button(self.root, text='Разработчики', command=self.Creators, style='buttondesign1.Toolbutton', cursor='hand2')
        self.button.place(x=20, y=675)

        # Кнопка Решенные задачи
        self.button = ttk.Button(self.root, text='Решенные задачи', command=self.Tasks, style='buttondesign1.Toolbutton', cursor='hand2')
        self.button.place(x=20, y=625)

        # Кнопка История Linux
        self.button = ttk.Button(self.root, text='История Linux', command=self.His, style='buttondesign1.Toolbutton', cursor='hand2')
        self.button.place(x=20, y=575)

        # Кнопка Онлайн Терминал
        self.button = ttk.Button(self.root, text='Онлайн Терминал', command=self.Onl_Term, style='buttondesign1.Toolbutton', cursor='hand2')
        self.button.place(x=320, y=675)

        # Кнопка уменшить громкость
        self.button = ttk.Button(self.root, text='<', command=self.decrease_volume, style='buttondesign6.Toolbutton', cursor='hand2')
        self.button.place(x=1080, y=625)

        # Кнопка увеличить громкость
        self.button = ttk.Button(self.root, text='>', command=self.increase_volume, style='buttondesign6.Toolbutton', cursor='hand2')
        self.button.place(x=1130, y=625)

        # Кнопка 1
        self.button = ttk.Button(self.root, text='1', command=lambda question_number=1: self.open_terminal(question_number), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=50, y=50)

        # Кнопка 2
        self.button = ttk.Button(self.root, text='2', command=lambda question_number=2: self.open_terminal(question_number), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=125, y=50)

        # Кнопка 3
        self.button = ttk.Button(self.root, text='3', command=lambda question_number=3: self.open_terminal(question_number), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=200, y=50)

        # Кнопка 4
        self.button = ttk.Button(self.root, text='4', command=lambda question_number=4: self.open_terminal(question_number), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=275, y=50)

        # Кнопка 5
        self.button = ttk.Button(self.root, text='5', command=lambda question_number=5: self.open_terminal(question_number), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=350, y=50)

        # Кнопка 6
        self.button = ttk.Button(self.root, text='6', command=lambda question_number=6: self.open_terminal(question_number), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=425, y=50)

        # Кнопка 7
        self.button = ttk.Button(self.root, text='7', command=lambda question_number=7: self.open_terminal(question_number), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=500, y=50)

        # Кнопка 8
        self.button = ttk.Button(self.root, text='8', command=lambda question_number=8: self.open_terminal(question_number), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=575, y=50)

        # Кнопка 9
        self.button = ttk.Button(self.root, text='9', command=lambda question_number=9: self.open_terminal(question_number), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=650, y=50)

        # Кнопка 10
        self.button = ttk.Button(self.root, text='10', command=lambda question_number=10: self.open_terminal(question_number), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=725, y=50)

        # Кнопка 11
        self.button = ttk.Button(self.root, text='11', command=lambda question_number=11: self.open_terminal(question_number), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=800, y=50)

        # Кнопка 12
        self.button = ttk.Button(self.root, text='12', command=lambda question_number=12: self.open_terminal(question_number), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=875, y=50)

        # Кнопка 13
        self.button = ttk.Button(self.root, text='13', command=lambda question_number=13: self.open_terminal(question_number), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=950, y=50)

        # Кнопка 14
        self.button = ttk.Button(self.root, text='14', command=lambda question_number=14: self.open_terminal(question_number), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=1025, y=50)

        # Кнопка 15
        self.button = ttk.Button(self.root, text='15', command=lambda question_number=15: self.open_terminal(question_number), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=1100, y=50)

        # Кнопка 16
        self.button = ttk.Button(self.root, text='16', command=lambda question_number=16: self.open_terminal(question_number), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=50, y=125)

        # Кнопка 17
        self.button = ttk.Button(self.root, text='17', command=lambda question_number=17: self.open_terminal(question_number), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=125, y=125)

        # Кнопка 18
        self.button = ttk.Button(self.root, text='18', command=lambda question_number=18: self.open_terminal(question_number), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=200, y=125)

        # Кнопка 19
        self.button = ttk.Button(self.root, text='19', command=lambda question_number=19: self.open_terminal(question_number), style='buttondesign2.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=275, y=125)

        # Кнопка 20
        self.button = ttk.Button(self.root, text='20', command=lambda question_number=20: self.open_terminal(question_number), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=350, y=125)

        # Кнопка 21
        self.button = ttk.Button(self.root, text='21', command=lambda question_number=21: self.open_terminal(question_number), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=425, y=125)

        # Кнопка 22
        self.button = ttk.Button(self.root, text='22', command=lambda question_number=22: self.open_terminal(question_number), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=500, y=125)

        # Кнопка 23
        self.button = ttk.Button(self.root, text='23', command=lambda question_number=23: self.open_terminal(question_number), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=575, y=125)

        # Кнопка 24
        self.button = ttk.Button(self.root, text='24', command=lambda question_number=24: self.open_terminal(question_number), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=650, y=125)

        # Кнопка 25
        self.button = ttk.Button(self.root, text='25', command=lambda question_number=25: self.open_terminal(question_number), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=725, y=125)

        # Кнопка 26
        self.button = ttk.Button(self.root, text='26', command=lambda question_number=26: self.open_terminal(question_number), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=800, y=125)

        # Кнопка 27
        self.button = ttk.Button(self.root, text='27', command=lambda question_number=27: self.open_terminal(question_number), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=875, y=125)

        # Кнопка 28
        self.button = ttk.Button(self.root, text='28', command=lambda question_number=28: self.open_terminal(question_number), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=950, y=125)

        # Кнопка 29
        self.button = ttk.Button(self.root, text='29', command=lambda question_number=29: self.open_terminal(question_number), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=1025, y=125)

        # Кнопка 30
        self.button = ttk.Button(self.root, text='30', command=lambda question_number=30: self.open_terminal(question_number), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=1100, y=125)

        # Кнопка 31
        self.button = ttk.Button(self.root, text='31', command=lambda question_number=31: self.open_terminal(question_number), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=50, y=200)

        # Кнопка 32
        self.button = ttk.Button(self.root, text='32', command=lambda question_number=32: self.open_terminal(question_number), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=125, y=200)

        # Кнопка 33
        self.button = ttk.Button(self.root, text='33', command=lambda question_number=33: self.open_terminal(question_number), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=200, y=200)

        # Кнопка 34
        self.button = ttk.Button(self.root, text='34', command=lambda question_number=34: self.open_terminal(question_number), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=275, y=200)

        # Кнопка 35
        self.button = ttk.Button(self.root, text='35', command=lambda question_number=35: self.open_terminal(question_number), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=350, y=200)

        # Кнопка 36
        self.button = ttk.Button(self.root, text='36', command=lambda question_number=36: self.open_terminal(question_number), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=425, y=200)

        # Кнопка 37
        self.button = ttk.Button(self.root, text='37', command=lambda question_number=37: self.open_terminal(question_number), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=500, y=200)

        # Кнопка 38
        self.button = ttk.Button(self.root, text='38', command=lambda question_number=38: self.open_terminal(question_number), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=575, y=200)

        # Кнопка 39
        self.button = ttk.Button(self.root, text='39', command=lambda question_number=39: self.open_terminal(question_number), style='buttondesign3.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=650, y=200)

        # Кнопка 40
        self.button = ttk.Button(self.root, text='40', command=lambda question_number=40: self.open_terminal(question_number), style='buttondesign4.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=725, y=200)

        # Кнопка 41
        self.button = ttk.Button(self.root, text='41', command=lambda question_number=41: self.open_terminal(question_number), style='buttondesign4.Toolbutton',  padding=10, cursor='hand2')
        self.button.place(x=800, y=200)

        # Кнопка 42
        self.button = ttk.Button(self.root, text='42', command=lambda question_number=42: self.open_terminal(question_number), style='buttondesign4.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=875, y=200)

        # Кнопка 43
        self.button = ttk.Button(self.root, text='43', command=lambda question_number=43: self.open_terminal(question_number), style='buttondesign4.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=950, y=200)

        # Кнопка 44
        self.button = ttk.Button(self.root, text='44', command=lambda question_number=44: self.open_terminal(question_number), style='buttondesign4.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=1025, y=200)

        # Кнопка 45
        self.button = ttk.Button(self.root, text='45', command=lambda question_number=45: self.open_terminal(question_number), style='buttondesign4.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=1100, y=200)

        # Кнопка 46
        self.button = ttk.Button(self.root, text='46', command=lambda question_number=46: self.open_terminal(question_number), style='buttondesign4.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=50, y=275)

        # Кнопка 47
        self.button = ttk.Button(self.root, text='47', command=lambda question_number=47: self.open_terminal(question_number), style='buttondesign4.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=125, y=275)

        # Кнопка 48
        self.button = ttk.Button(self.root, text='48', command=lambda question_number=48: self.open_terminal(question_number), style='buttondesign4.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=200, y=275)

        def but49():
            # Кнопка 49
            self.button = ttk.Button(self.root, text='49', command=lambda question_number=49: self.open_terminal(question_number), style='buttondesign5.Toolbutton', padding=10, cursor='hand2')
            self.button.place(x=275, y=275)

        tasks = 'Scripts/Tasks.txt'
        with open(tasks, 'r') as file:
            line_count = sum(1 for line in file)

        if line_count >= 48:
            but49()

        # Кнопка 50
        self.button = ttk.Button(self.root, text='50', command=lambda question_number=50: self.open_terminal(question_number), style='buttondesign5.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=50, y=350)

        # Кнопка 51
        self.button = ttk.Button(self.root, text='51', command=lambda question_number=51: self.open_terminal(question_number), style='buttondesign5.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=125, y=350)

        # Кнопка 52
        self.button = ttk.Button(self.root, text='52', command=lambda question_number=52: self.open_terminal(question_number), style='buttondesign5.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=200, y=350)

        # Кнопка 53
        self.button = ttk.Button(self.root, text='53', command=lambda question_number=53: self.open_terminal(question_number), style='buttondesign5.Toolbutton', padding=10, cursor='hand2')
        self.button.place(x=275, y=350)

        self.root.mainloop()


if __name__ == "__main__":
    app = App()
