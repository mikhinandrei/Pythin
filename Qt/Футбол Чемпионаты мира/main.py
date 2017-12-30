import sqlite3
import sys

from PyQt4 import QtGui, QtCore

NUM_OF_COLUMNS = 9
HEADERS = ["Место", "Страна", "Побед", "Ничьих", "Поражений", "ГЗ", "ГП", "Разница", "Очки"]

connection = sqlite3.connect('databases/world_cups/2014.db')

curs = connection.cursor()

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.resize(1280, 768)
        self.setWindowTitle('История футбола')

        self.group = QtGui.QGroupBox()
        self.scroll = QtGui.QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.group.setStyleSheet("QGroupBox {background-color: #5083E2;}"
                                 "QComboBox {font-size: 16px;"
                                            "border-radius: 5px; "
                                            "background-color: #96C9FF}")
        self.setCentralWidget(self.scroll)

        self.layout = QtGui.QGridLayout()
        self.group.setLayout(self.layout)

        self.tournament_combo = QtGui.QComboBox()
        self.tournament_combo.addItem("Чемпионат мира")

        year_list = ['1930', '1934', '1938']
        year = 1950
        while year <= 2014:
            year_list.append(str(year))
            year += 4

        year_list.reverse()
        print(year_list)
        self.year_combo = QtGui.QComboBox()
        self.year_combo.addItems(year_list)
        self.year_combo.setCurrentIndex(0)

        self.layout.addWidget(self.tournament_combo, 0, 0)
        self.layout.addWidget(self.year_combo, 0, 1)

        self.counter = 0

        self.show_groups()
        self.show_group_matches()

        self.scroll.setWidget(self.group)

    def show_groups(self):
        curs.execute('SELECT group_name FROM groups')
        letters = []
        for letter in curs.fetchall():
            if letter not in letters:
                letters.append(letter)
        k = 0
        for item in letters:
            query = 'SELECT position, country, wins, draws, loses, goals, missed, difference, points FROM groups WHERE group_name="' + str(item[0]) + '"'
            curs.execute(query)
            array = curs.fetchall()
            mini_layout = QtGui.QGridLayout()
            mini_layout.setSpacing(0)
            for i in range(9):
                label = QtGui.QLabel(HEADERS[i])
                label.setStyleSheet("QLabel {"
                             "border-style: solid;"
                             "border-width: 1px;"
                             "border-color: black; "
                                    "font-size: 12px;"
                                    "font-weight: bold;"
                             "}")
                mini_layout.addWidget(label, 0, i)
            i = 1
            for line in array:
                for x in range(NUM_OF_COLUMNS):
                    if x == 1:
                        link = QtGui.QPixmap('flags/' + str(line[x]) + '.png')
                        label = QtGui.QGroupBox()
                        img = QtGui.QLabel()
                        img.setPixmap(link)
                        ll = QtGui.QGridLayout()
                        lbl = QtGui.QLabel(str(line[x]))
                        ll.addWidget(img, 0, 0)
                        ll.addWidget(lbl, 0, 1)
                        label.setLayout(ll)
                        label.setStyleSheet("QGroupBox {"
                                 "border-style: solid;"
                                 "border-width: 1px;"
                                 "border-color: black; "
                                 "}")
                        if i < 3:
                            label.setStyleSheet("QGroupBox {background-color: #99cc99; border-style: solid;"
                                 "border-width: 1px;"
                                 "border-color: black; }")
                    else:
                        label = QtGui.QLabel (str(line[x]))
                        label.setStyleSheet("QLabel {"
                                 "border-style: solid;"
                                 "border-width: 1px;"
                                 "border-color: black; "
                                 "text-align: center; "
                                 "}")
                        if i < 3:
                            label.setStyleSheet("QLabel {background-color: #99cc99; border-style: solid;"
                                 "border-width: 1px;"
                                 "border-color: black; }")
                    label.setMinimumHeight(33)
                    mini_layout.addWidget(label, i, x)

                i += 1
            name = "Группа " + item[0]
            acc = QtGui.QTreeWidget()
            inside_widget = QtGui.QTreeWidgetItem(acc)
            inside_widget.setText(0, "Показать матчи группы")
            v = QtGui.QTreeWidgetItem(inside_widget)
            v.setText(0, "авапт\nhdfgc\nrgfds\nhtrgfd\nhtrgfdsa\njyuugdrefds\nkiukjhgfd\n")
            acc.setHeaderHidden(True)
            acc.set
            mini_layout.addWidget(acc, i+1, 0, 1, NUM_OF_COLUMNS)
            widget = QtGui.QGroupBox(name)
            widget.setLayout(mini_layout)
            self.layout.addWidget(widget, (k//2)+1, k%2)
            del widget
            k += 1
        self.counter = k

    def show_group_matches(self):
        curs.execute('SELECT flag FROM flag')

        flag = int(curs.fetchall()[0][0])

        curs.execute('SELECT * from matches')
        array = curs.fetchall()[:flag]
        for (id, team1, team2, team1goals, team2goals, stadium, viewers, referee) in array:
            group_box = QtGui.QGroupBox()
            mini_layout = QtGui.QGridLayout()

            team_1_flag_link = QtGui.QPixmap('flags/' + str(team1) + '.png')
            team_2_flag_link = QtGui.QPixmap('flags/' + str(team2) + '.png')

            team_1_flag = QtGui.QLabel()
            team_1_flag.setPixmap(team_1_flag_link)
            team_2_flag = QtGui.QLabel()
            team_2_flag.setPixmap(team_2_flag_link)

            team_1_label = QtGui.QLabel(str(team1))
            team_2_label = QtGui.QLabel(str(team2))

            score_text = str(team1goals) + ":" + str(team2goals)

            score = QtGui.QLabel(score_text)

            mini_layout.addWidget(team_1_flag, 0, 0)
            mini_layout.addWidget(team_1_label, 0, 1)
            mini_layout.addWidget(score, 0, 2)
            mini_layout.addWidget(team_2_label, 0, 3)
            mini_layout.addWidget(team_2_flag, 0, 4)

            group_box.setLayout(mini_layout)
            group_box.setMinimumHeight(33)

            self.layout.addWidget(group_box, (self.counter//2)+1, self.counter%2)

            self.counter += 1


if __name__ == '__main__':
    connection.commit()
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    app.exec()