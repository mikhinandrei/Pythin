"""
    Конвертер температур.
    Программа написана на языке Python.
    Цель - быстрый, простой, качественный перевод температур
    из разных шкал измерения.
    Программа распространяется по лицензии GNU GPL.
"""

import re
from tkinter import *


class Converter(Frame):

    def __init__(self, master):
        super(Converter, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.make_menu()

    def create_widgets(self):
        Label(self, text = u'Выберите начальную шкалу', font = ('Arial', 10)).grid(row = 0, column = 2, sticky = W)
        Label(self, text = u'Выберите конечную шкалу', font = ('Arial', 10)).grid(row = 0, column = 8, sticky = W)
        #################################################################################################
        #                                   INIT RADIOBUTTONS                                           #
        #################################################################################################
        self.id_from = StringVar() ; self.id_from.set(0)                                                #
        self.id_to   = StringVar() ; self.id_to.set(0)                                                  #
        #################################################################################################
        from_celsium = Radiobutton(self, text = u'Цельсия', font = ('Arial', 10), variable = self.id_from, value = "0", command = self.change)       #
        from_celsium.grid(row = 2, column = 2, sticky = W)                                              # Init Celsium
        to_celsium = Radiobutton(self, text = u'Цельсия', font = ('Arial', 10), variable = self.id_to, value = "0")           #
        to_celsium.grid(row = 2, column = 8, sticky = W)                                                #
        #################################################################################################
        from_farengeit = Radiobutton(self, text = u'Фаренгейта', font = ('Arial', 10), variable = self.id_from, value = '1', command = self.change)  #
        from_farengeit.grid(row = 3, column = 2, sticky = W)                                            # Init Farengeit
        to_farengeit = Radiobutton(self, text = u'Фаренгейта', font = ('Arial', 10), variable = self.id_to, value = '1')      #
        to_farengeit.grid(row = 3, column = 8, sticky = W)                                              #
        #################################################################################################
        from_kelvin = Radiobutton(self, text = u'Кельвина', font = ('Arial', 10), variable = self.id_from, value = '2', command = self.change)       #
        from_kelvin.grid(row = 4, column = 2, sticky = W)                                               #
        to_kelvin = Radiobutton(self, text = u'Кельвина', font = ('Arial', 10), variable = self.id_to, value = '2')           # Init Kelvin
        to_kelvin.grid(row = 4, column = 8, sticky = W)                                                 #
        #################################################################################################
        from_reamyur = Radiobutton(self, text = u'Реамюра', font = ('Arial', 10), variable = self.id_from, value = '3', command = self.change)       #
        from_reamyur.grid(row = 5, column = 2, sticky = W)                                              #
        to_reamyur = Radiobutton(self, text = u'Реамюра', font = ('Arial', 10), variable = self.id_to, value = '3')           # Init Reamyur
        to_reamyur.grid(row = 5, column = 8, sticky = W)                                                #
        #################################################################################################
        #                               END INIT RADIOBUTTONS                                           #
        #################################################################################################

        Label(self, text = u'Введите количество градусов',font = ('Arial', 10)).grid(row = 6, column = 2, sticky =W)
        self.convert_button = Button(self)
        self.convert_button["text"] = u'Перевести'
        self.enter = Entry(self)
        self.enter.grid(row = 7, column = 2, sticky = W)
        self.degree = Label(self, text = ' °C',font = ('Courier'))
        self.degree.grid(row = 7, column = 4, sticky = E)
        self.convert_button["command"] = self.convert
        self.convert_button.grid(row = 7, column = 5, sticky = W)
        self.result = Label(self, text = '', font = ('Arial', 10))
        self.result.grid(row = 7, column = 8, sticky = W)

    def make_menu(self):
        self.top = Menu(self.master)
        self.master.config(menu = self.top)

        about = Menu(self.top)
        about.add_command(label = u'Исходный код приложения', underline = 0, command = show_code)
        about.add_command(label = u'О программе', underline = 0)
        self.top.add_cascade(label = u'О программе', menu = about, underline = 0)

    def convert(self):
        #############################################
        def convert_C_to_F(start_temp):
            finish_temp = 1.8 * start_temp + 32
            return finish_temp

        def convert_C_to_K(start_temp):
            return start_temp + 273

        def convert_C_to_Re(start_temp):
            return start_temp * 0.8
        ###############################################
        def convert_F_to_C(start_temp):
            return (start_temp - 32) / 1.8

        def convert_F_to_K(start_temp):
            return (start_temp - 32) / 1.8 + 273

        def convert_F_to_Re(start_temp):
            return (start_temp - 32) / 1.8 * 0.8
        ##############################################
        def convert_K_to_C(start_temp):
            return start_temp - 273

        def convert_K_to_F(start_temp):
            return 1.8 * (start_temp - 273) + 32

        def convert_K_to_Re(start_temp):
            return (start_temp - 273) * 0.8
        ##############################################
        def convert_Re_to_C(start_temp):
            return start_temp * 1.25

        def convert_Re_to_F(start_temp):
            return (start_temp * 1.25)*1.8 + 32

        def convert_Re_to_K(start_temp):
            return start_temp*1.25 + 273
        ##############################################

        id = str(self.id_from.get()) + str(self.id_to.get())
        try:
            start_temp = float(self.enter.get())
            if self.id_from.get() == self.id_to.get():
                finish_temp = str(start_temp) + ' ' + self.degree["text"]
            if id == '01':
                finish_temp = str(convert_C_to_F(start_temp)) + ' °F'
            if id == '02':
                finish_temp = str(convert_C_to_K(start_temp)) + ' K'
            if id == '03':
                finish_temp = str(convert_C_to_Re(start_temp)) + ' °Re'
            if id == '10':
                finish_temp = str(convert_F_to_C(start_temp)) + ' °C'
            if id == '12':
                finish_temp = str(convert_F_to_K(start_temp)) + ' K'
            if id == '13':
                finish_temp = str(convert_F_to_Re(start_temp)) + ' °Re'
            if id == '20':
                finish_temp = str(convert_K_to_C(start_temp)) + ' °C'
            if id == '21':
                finish_temp = str(convert_K_to_F(start_temp)) + ' °F'
            if id == '23':
                finish_temp = str(convert_K_to_Re(start_temp)) + ' °Re'
            if id == '30':
                finish_temp = str(convert_Re_to_C(start_temp)) + ' °C'
            if id == '31':
                finish_temp = str(convert_Re_to_F(start_temp)) + ' °F'
            if id == '32':
                finish_temp = str(convert_Re_to_K(start_temp)) + ' K'
        except ValueError:
            finish_temp = u'Введите корректное число'
        self.result["text"] = finish_temp

    def change(self):
        if self.id_from.get() == '0':
            self.degree["text"] = ' °C'
        if self.id_from.get() == '1':
            self.degree["text"] = ' °F'
        if self.id_from.get() == '2':
            self.degree["text"] = '  K'
        if self.id_from.get() == '3':
            self.degree["text"] = '°Re'


def show_code():
      show = Tk()
      show.title('Исходный код')
      a = open('Converter.py', 'r', encoding = 'utf-8')
      text = a.readlines()
      lbl = Label(show, text = text)
      lbl.grid()
      show.mainloop()


if __name__ == '__main__':
    app = Tk()
    app.title(u'Конвертер температур')
    frame = Converter(app)
    app.mainloop()