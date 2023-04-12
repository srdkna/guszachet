import datetime
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

import pymysql
from connect import host, user, password, database

connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=database,
    cursorclass=pymysql.cursors.DictCursor
)

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\guszachet\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def insert():
    with connection.cursor() as cursor:
        name1 = entry_1.get()

        sql = f"INSERT INTO `gruz` (`name`) VALUES ('{name1}')"
        print(sql)
        cursor.execute(sql)
        connection.commit()

def insert():
    with connection.cursor() as cursor:
        kod_stelaz1 = entry_4.get()
        numder_yaceek1 = entry_5.get()
        massa1 = entry_3.get()
        now = datetime.datetime.now()
        date1 = (now.strftime("%Y-%m-%d"))

        sql = f"INSERT INTO `position`(`id_stelaj`, `number_yaceek`, `massa`, `date`) VALUES ({kod_stelaz1},'{numder_yaceek1}', '{massa1}', '{date1}')"
        cursor.execute(sql)
        connection.commit()


window = Tk()
window.title("склад Середкина Александра")

window.geometry("1100x700")
window.configure(bg="#FFFFFF")

canvas = Canvas(window, bg="#FFFFFF",
                height=700,
                width=1100,
                bd=0,
                highlightthickness=0,
                relief="ridge")

canvas.place(x=0, y=0)  # размещение всех элементов ввода ровно на канву

# поле ввода (название товара)
entry_image_1 = PhotoImage(file=relative_to_assets("entry_name.png"))
entry_bg_1 = canvas.create_image(291.0, 219.0, image=entry_image_1)

entry_1 = Entry(bd=0,
                bg="#D1D1D1",
                fg="#000716",
                highlightthickness=0)

entry_1.place(x=111.0, y=199.0, width=360.0, height=38.0)

# поле ввода стелажа
entry_image_4 = PhotoImage(file=relative_to_assets("entry_id_stelaj.png"))
entry_bg_4 = canvas.create_image(291.0, 294.0, image=entry_image_4)

entry_4 = Entry(bd=0,
                bg="#D1D1D1",
                fg="#000716",
                highlightthickness=0)

entry_4.place(x=111.0, y=274.0, width=360.0, height=38.0)

# поле ввода номер ячейки
entry_image_5 = PhotoImage(file=relative_to_assets("entry_numder_yaceek.png"))
entry_bg_5 = canvas.create_image(291.0, 369.0, image=entry_image_5)

entry_5 = Entry(bd=0,
                bg="#D1D1D1",
                fg="#000716",
                highlightthickness=0)

entry_5.place(x=111.0, y=349.0, width=360.0, height=38.0)

# поле ввода масса
entry_image_3 = PhotoImage(file=relative_to_assets("entry_massa.png"))
entry_bg_3 = canvas.create_image(291.0, 444.0, image=entry_image_3)

entry_3 = Entry(bd=0,
                bg="#D1D1D1",
                fg="#000716",
                highlightthickness=0)

entry_3.place(x=111.0, y=424.0, width=360.0, height=38.0)

# поле ввода Дата укладки
entry_image_2 = PhotoImage(file=relative_to_assets("entry_date.png"))
entry_bg_2 = canvas.create_image(291.0, 519.0, image=entry_image_2)

entry_2 = Entry(bd=0,
                bg="#D1D1D1",
                fg="#000716",
                highlightthickness=0)

entry_2.place(x=111.0, y=499.0, width=360.0, height=38.0)

# Текстики то биж лейблы

canvas.create_text(362.0, 59.0,
                   anchor="nw",
                   text="Склад товаров\n",
                   fill="#514438",
                   font=("Inter", 50 * -1))

canvas.create_text(101.0, 170.0,
                   anchor="nw",
                   text="Название товара\n",
                   fill="#423434",
                   font=("Inter", 20 * -1))

canvas.create_text(101.0, 245.0,
                   anchor="nw",
                   text="Код стелажа",
                   fill="#423434",
                   font=("Inter", 20 * -1))

canvas.create_text(101.0, 320.0,
                   anchor="nw",
                   text="Номер ячейки",
                   fill="#423434",
                   font=("Inter", 20 * -1))

canvas.create_text(101.0, 395.0,
                   anchor="nw",
                   text="Масса\n",
                   fill="#423434",
                   font=("Inter", 20 * -1))

canvas.create_text(101.0, 470.0,
                   anchor="nw",
                   text="Дата укладки\n",
                   fill="#423434",
                   font=("Inter", 20 * -1))


# Две конпки коричневого цвета где кнопка 1 вводит данные а кнопка 2 считает свободные ячейки


button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))

button_1 = Button(image=button_image_1,
                  borderwidth=0,
                  highlightthickness=0,
                  command=insert,
                  relief="flat")

button_1.place(x=101.0, y=557.0, width=182.0, height=40.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2,
                  borderwidth=0,
                  highlightthickness=0,
                  command=lambda: print("button_2 clicked"),
                  relief="flat")

button_2.place(x=724.0, y=557.0, width=182.0, height=40.0)

# кол-во ячеек и сторона с подсчетом

canvas.create_text(617.0, 404.0,
                   anchor="nw",
                   text=" колличество свободных ячеек ",
                   fill="#514438",
                   font=("Inter", 30 * -1))

canvas.create_text(660.0, 507.0,
                   anchor="nw",
                   text="Свободные ячейки:",
                   fill="#423434",
                   font=("Inter", 20 * -1))

# поле в котором будет появляться кол во свободных ячеек
entry_image_6 = PhotoImage(file=relative_to_assets("entry_svobod_yaceek.png"))
entry_bg_6 = canvas.create_image(919.0, 519.0, image=entry_image_6)

entry_6 = Entry(bd=0,
                bg="#D1D1D1",
                fg="#000716",
                highlightthickness=0)

entry_6.place(x=876.0, y=499.0, width=86.0, height=38.0)

# картинка с каробками
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(815.0, 265.0, image=image_image_1)

window.resizable(False, False)
window.mainloop()
