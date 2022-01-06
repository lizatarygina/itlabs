import sys
import psycopg2
from PyQt5.QtWidgets import (QApplication, QWidget, QTabWidget, QAbstractScrollArea, QVBoxLayout, QHBoxLayout,
                             QTableWidget, QGroupBox, QTableWidget, QGroupBox, QTableWidgetItem, QPushButton,
                             QMessageBox)


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Расписание")

        self._connect_to_db()

        self.tabs = QTabWidget(self)

        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(self.tabs)
        self._create_shedule_tab()

    def _connect_to_db(self):
        self.conn = psycopg2.connect(database="telebot",
                                     user="postgres",
                                     password="1234",
                                     host="localhost",
                                     port="5432")
        self.cursor = self.conn.cursor()

    def _create_shedule_tab(self):
        self.shedule_tab = QWidget()
        self.tabs.addTab(self.shedule_tab, "Расписание")
        self.teacher_tab = QWidget()
        self.tabs.addTab(self.teacher_tab, "Преподаватели")
        self.subject_tab = QWidget()
        self.tabs.addTab(self.subject_tab, "Предметы")

        self.monday_gbox = QGroupBox("Понедельник")
        self.tuesday_gbox = QGroupBox("Вторник")
        self.wednesday_gbox = QGroupBox("Среда")
        self.thursday_gbox = QGroupBox("Четверг")
        self.friday_gbox = QGroupBox("Пятница")
        self.teacher_gbox = QGroupBox("Перподаватели")
        self.subject_gbox = QGroupBox("Предметы")

        self.svbox = QVBoxLayout()
        self.shbox1 = QVBoxLayout()
        self.shbox2 = QHBoxLayout()
        self.svbox2 = QVBoxLayout()
        self.shbox21 = QVBoxLayout()
        self.shbox22 = QHBoxLayout()
        self.svbox3 = QVBoxLayout()
        self.shbox31 = QVBoxLayout()
        self.shbox32 = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)
        self.svbox2.addLayout(self.shbox21)
        self.svbox2.addLayout(self.shbox22)
        self.svbox3.addLayout(self.shbox31)
        self.svbox3.addLayout(self.shbox32)

        self.shbox1.addWidget(self.monday_gbox)
        self.shbox1.addWidget(self.tuesday_gbox)
        self.shbox1.addWidget(self.wednesday_gbox)
        self.shbox1.addWidget(self.thursday_gbox)
        self.shbox1.addWidget(self.friday_gbox)
        self.shbox21.addWidget(self.teacher_gbox)
        self.shbox31.addWidget(self.subject_gbox)

        self._create_monday_table()
        self._create_tuesday_table()
        self._create_wednesday_table()
        self._create_thursday_table()
        self._create_friday_table()
        self._create_teacher_table()
        self._create_subject_table()

        self.update_shedule_btn = QPushButton("Update")
        self.update_teacher_btn = QPushButton("Update")
        self.update_subject_btn = QPushButton("Update")
        self.shbox2.addWidget(self.update_shedule_btn)
        self.shbox22.addWidget(self.update_teacher_btn)
        self.shbox32.addWidget(self.update_subject_btn)
        self.update_shedule_btn.clicked.connect(self._update_shedule)
        self.update_teacher_btn.clicked.connect(self._update_teacher)
        self.update_subject_btn.clicked.connect(self._update_subject)

        self.shedule_tab.setLayout(self.svbox)
        self.teacher_tab.setLayout(self.svbox2)
        self.subject_tab.setLayout(self.svbox3)

    def _create_monday_table(self):
        self.monday_table = QTableWidget()

        self.monday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.monday_table.setColumnCount(6)
        self.monday_table.setHorizontalHeaderLabels(["Позиция", "Предмет", "Время", "ID", "", ""])
        self.monday_table.hideColumn(3)

        self._update_monday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.monday_table)
        self.monday_gbox.setLayout(self.mvbox)

    def _create_tuesday_table(self):
        self.tuesday_table = QTableWidget()

        self.tuesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.tuesday_table.setColumnCount(6)
        self.tuesday_table.setHorizontalHeaderLabels(["Позиция", "Предмет", "Время", "ID", "", ""])
        self.tuesday_table.hideColumn(3)

        self._update_tuesday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.tuesday_table)
        self.tuesday_gbox.setLayout(self.mvbox)

    def _create_wednesday_table(self):
        self.wednesday_table = QTableWidget()

        self.wednesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.wednesday_table.setColumnCount(6)
        self.wednesday_table.setHorizontalHeaderLabels(["Позиция", "Предмет", "Время", "ID", "", ""])
        self.wednesday_table.hideColumn(3)

        self._update_wednesday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.wednesday_table)
        self.wednesday_gbox.setLayout(self.mvbox)

    def _create_thursday_table(self):
        self.thursday_table = QTableWidget()

        self.thursday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.thursday_table.setColumnCount(6)
        self.thursday_table.setHorizontalHeaderLabels(["Позиция", "Предмет", "Время", "ID", "", ""])
        self.thursday_table.hideColumn(3)

        self._update_thursday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.thursday_table)
        self.thursday_gbox.setLayout(self.mvbox)

    def _create_friday_table(self):
        self.friday_table = QTableWidget()

        self.friday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.friday_table.setColumnCount(6)
        self.friday_table.setHorizontalHeaderLabels(["Позиция", "Предмет", "Время", "ID", "", ""])
        self.friday_table.hideColumn(3)

        self._update_friday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.friday_table)
        self.friday_gbox.setLayout(self.mvbox)

    def _create_teacher_table(self):
        self.teacher_table = QTableWidget()

        self.teacher_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.teacher_table.setColumnCount(5)
        self.teacher_table.setHorizontalHeaderLabels(["Имя", "Предмет", "ID", "", ""])
        self.teacher_table.hideColumn(2)

        self._update_teacher_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.teacher_table)
        self.teacher_gbox.setLayout(self.mvbox)

    def _create_subject_table(self):
        self.subject_table = QTableWidget()

        self.subject_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.subject_table.setColumnCount(2)
        self.subject_table.setHorizontalHeaderLabels(["Предмет", ""])

        self._update_subject_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.subject_table)
        self.subject_gbox.setLayout(self.mvbox)

    def _update_monday_table(self):
        self.cursor.execute(
            "select pos, subject, start_time, id from time_table where day = 'Пн' order by start_time;")
        records = list(self.cursor.fetchall())

        self.monday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            self.monday_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.monday_table.setItem(i, 1, QTableWidgetItem(str(r[1])))
            self.monday_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.monday_table.setItem(i, 3, QTableWidgetItem(str(r[3])))
            joinbtn = QPushButton("Изменить")
            self.monday_table.setCellWidget(i, 4, joinbtn)
            joinbtn.clicked.connect(lambda checked=None, j=i: self._change_day_from_table(j, self.monday_table))
            delbtn = QPushButton("Удалить")
            self.monday_table.setCellWidget(i, 5, delbtn)
            delbtn.clicked.connect(lambda checked=None, j=i: self._del_from_time_table(j, self.monday_table))
            addbtn = QPushButton("Добавить")
            self.monday_table.setItem(i + 1, 0, QTableWidgetItem(''))
            self.monday_table.setItem(i + 1, 1, QTableWidgetItem(''))
            self.monday_table.setItem(i + 1, 2, QTableWidgetItem(''))
            self.monday_table.setItem(i + 1, 3, QTableWidgetItem(''))
            self.monday_table.removeCellWidget(i + 1, 4)
            self.monday_table.removeCellWidget(i + 1, 5)
            self.monday_table.setCellWidget(i + 1, 4, addbtn)
            addbtn.clicked.connect(lambda checked=None, j=i + 1: self._add_time_table(j, self.monday_table))

        self.monday_table.resizeRowsToContents()

    def _update_tuesday_table(self):
        self.cursor.execute(
            "select pos, subject, start_time, id from time_table where day = 'Вт' order by start_time;")
        records = list(self.cursor.fetchall())

        self.tuesday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            self.tuesday_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.tuesday_table.setItem(i, 1, QTableWidgetItem(str(r[1])))
            self.tuesday_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.tuesday_table.setItem(i, 3, QTableWidgetItem(str(r[3])))
            joinbtn = QPushButton("Изменить")
            self.tuesday_table.setCellWidget(i, 4, joinbtn)
            joinbtn.clicked.connect(lambda checked=None, j=i: self._change_day_from_table(j, self.tuesday_table))
            delbtn = QPushButton("Удалить")
            self.tuesday_table.setCellWidget(i, 5, delbtn)
            delbtn.clicked.connect(lambda checked=None, j=i: self._del_from_time_table(j, self.tuesday_table))
            self.tuesday_table.setItem(i + 1, 0, QTableWidgetItem(''))
            self.tuesday_table.setItem(i + 1, 1, QTableWidgetItem(''))
            self.tuesday_table.setItem(i + 1, 2, QTableWidgetItem(''))
            self.tuesday_table.setItem(i + 1, 3, QTableWidgetItem(''))
            self.tuesday_table.removeCellWidget(i + 1, 4)
            self.tuesday_table.removeCellWidget(i + 1, 5)
            addbtn = QPushButton("Добавить")
            self.tuesday_table.setCellWidget(i + 1, 4, addbtn)
            addbtn.clicked.connect(lambda checked=None, j=i + 1: self._add_time_table(j, self.tuesday_table))
        self.tuesday_table.resizeRowsToContents()

    def _update_wednesday_table(self):
        self.cursor.execute(
            "select pos, subject, start_time, id from time_table where day = 'Ср' order by start_time;")
        records = list(self.cursor.fetchall())

        self.wednesday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            self.wednesday_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.wednesday_table.setItem(i, 1, QTableWidgetItem(str(r[1])))
            self.wednesday_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.wednesday_table.setItem(i, 3, QTableWidgetItem(str(r[3])))
            joinbtn = QPushButton("Изменить")
            self.wednesday_table.setCellWidget(i, 4, joinbtn)
            joinbtn.clicked.connect(lambda checked=None, j=i: self._change_day_from_table(j, self.wednesday_table))
            delbtn = QPushButton("Удалить")
            self.wednesday_table.setCellWidget(i, 5, delbtn)
            delbtn.clicked.connect(lambda checked=None, j=i: self._del_from_time_table(j, self.wednesday_table))
            self.wednesday_table.setItem(i + 1, 0, QTableWidgetItem(''))
            self.wednesday_table.setItem(i + 1, 1, QTableWidgetItem(''))
            self.wednesday_table.setItem(i + 1, 2, QTableWidgetItem(''))
            self.wednesday_table.setItem(i + 1, 3, QTableWidgetItem(''))
            self.wednesday_table.removeCellWidget(i + 1, 4)
            self.wednesday_table.removeCellWidget(i + 1, 5)
            addbtn = QPushButton("Добавить")
            self.wednesday_table.setCellWidget(i + 1, 4, addbtn)
            addbtn.clicked.connect(lambda checked=None, j=i + 1: self._add_time_table(j, self.wednesday_table))

        self.wednesday_table.resizeRowsToContents()

    def _update_thursday_table(self):
        self.cursor.execute(
            "select pos, subject, start_time, id from time_table where day = 'Чт' order by start_time;")
        records = list(self.cursor.fetchall())

        self.thursday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            self.thursday_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.thursday_table.setItem(i, 1, QTableWidgetItem(str(r[1])))
            self.thursday_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.thursday_table.setItem(i, 3, QTableWidgetItem(str(r[3])))
            joinbtn = QPushButton("Изменить")
            self.thursday_table.setCellWidget(i, 4, joinbtn)
            joinbtn.clicked.connect(lambda checked=None, j=i: self._change_day_from_table(j, self.thursday_table))
            delbtn = QPushButton("Удалить")
            self.thursday_table.setCellWidget(i, 5, delbtn)
            delbtn.clicked.connect(lambda checked=None, j=i: self._del_from_time_table(j, self.thursday_table))
            self.thursday_table.setItem(i + 1, 0, QTableWidgetItem(''))
            self.thursday_table.setItem(i + 1, 1, QTableWidgetItem(''))
            self.thursday_table.setItem(i + 1, 2, QTableWidgetItem(''))
            self.thursday_table.setItem(i + 1, 3, QTableWidgetItem(''))
            self.thursday_table.removeCellWidget(i + 1, 4)
            self.thursday_table.removeCellWidget(i + 1, 5)
            addbtn = QPushButton("Добавить")
            self.thursday_table.setCellWidget(i + 1, 4, addbtn)
            addbtn.clicked.connect(lambda checked=None, j=i + 1: self._add_time_table(j, self.thursday_table))

        self.thursday_table.resizeRowsToContents()

    def _update_friday_table(self):
        self.cursor.execute(
            "select pos, subject, start_time, id from time_table where day = 'Пт' order by start_time;")
        records = list(self.cursor.fetchall())

        self.friday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            self.friday_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.friday_table.setItem(i, 1, QTableWidgetItem(str(r[1])))
            self.friday_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.friday_table.setItem(i, 3, QTableWidgetItem(str(r[3])))
            joinbtn = QPushButton("Изменить")
            self.friday_table.setCellWidget(i, 4, joinbtn)
            joinbtn.clicked.connect(lambda checked=None, j=i: self._change_day_from_table(j, self.friday_table))
            delbtn = QPushButton("Удалить")
            self.friday_table.setCellWidget(i, 5, delbtn)
            delbtn.clicked.connect(lambda checked=None, j=i: self._del_from_time_table(j, self.friday_table))
            self.friday_table.setItem(i + 1, 0, QTableWidgetItem(''))
            self.friday_table.setItem(i + 1, 1, QTableWidgetItem(''))
            self.friday_table.setItem(i + 1, 2, QTableWidgetItem(''))
            self.friday_table.setItem(i + 1, 3, QTableWidgetItem(''))
            self.friday_table.removeCellWidget(i + 1, 4)
            self.friday_table.removeCellWidget(i + 1, 5)
            addbtn = QPushButton("Добавить")
            self.friday_table.setCellWidget(i + 1, 4, addbtn)
            addbtn.clicked.connect(lambda checked=None, j=i + 1: self._add_time_table(j, self.friday_table))

        self.friday_table.resizeRowsToContents()

    def _update_teacher_table(self):
        self.cursor.execute(
            "select full_name, subject, id from teacher;")
        records = list(self.cursor.fetchall())

        self.teacher_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            self.teacher_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.teacher_table.setItem(i, 1, QTableWidgetItem(str(r[1])))
            self.teacher_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
            joinbtn = QPushButton("Изменить")
            self.teacher_table.setCellWidget(i, 3, joinbtn)
            joinbtn.clicked.connect(lambda checked=None, j=i: self._change_teacher_table(j, self.teacher_table))
            delbtn = QPushButton("Удалить")
            self.teacher_table.setCellWidget(i, 4, delbtn)
            delbtn.clicked.connect(lambda checked=None, j=i: self._del_from_teacher(j, self.teacher_table))
            self.teacher_table.setItem(i + 1, 0, QTableWidgetItem(''))
            self.teacher_table.setItem(i + 1, 1, QTableWidgetItem(''))
            self.teacher_table.setItem(i + 1, 2, QTableWidgetItem(''))
            self.teacher_table.setItem(i + 1, 3, QTableWidgetItem(''))
            self.teacher_table.removeCellWidget(i + 1, 4)
            self.teacher_table.removeCellWidget(i + 1, 5)
            addbtn = QPushButton("Добавить")
            self.teacher_table.setItem(i + 1, 0, QTableWidgetItem(''))
            self.teacher_table.setCellWidget(i + 1, 3, addbtn)
            addbtn.clicked.connect(lambda checked=None, j=i + 1: self._add_teacher(j, self.teacher_table))

    def _update_subject_table(self):
        self.cursor.execute(
            "select name from subject;")
        records = list(self.cursor.fetchall())

        self.subject_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            self.subject_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            delbtn = QPushButton("Удалить")
            self.subject_table.setCellWidget(i, 1, delbtn)
            delbtn.clicked.connect(lambda checked=None, j=i: self._del_from_subject(j, self.subject_table))
            self.subject_table.setItem(i + 1, 0, QTableWidgetItem(''))
            self.subject_table.setItem(i + 1, 1, QTableWidgetItem(''))
            self.subject_table.setItem(i + 1, 2, QTableWidgetItem(''))
            self.subject_table.setItem(i + 1, 3, QTableWidgetItem(''))
            self.subject_table.removeCellWidget(i + 1, 4)
            self.subject_table.removeCellWidget(i + 1, 5)
            addbtn = QPushButton("Добавить")
            self.subject_table.setCellWidget(i + 1, 1, addbtn)
            addbtn.clicked.connect(lambda checked=None, j=i + 1: self._add_subject(j, self.subject_table))

    def _change_day_from_table(self, rown, a):
        row = list()
        for i in range(a.columnCount()):
            try:
                row.append(a.item(rown, i).text())
            except:
                row.append(None)
        if row[0] == '-' or row[0] == 'н' or row[0] == 'в':
            if row[2] == '9:30' or row[2] == '11:20' or row[2] == '13:10' or row[2] == '15:25' or row[2] == '17:15':
                try:
                    self.cursor.execute("update time_table set pos = '" + row[0] + "' where id = " + row[3] + ";")
                    self.cursor.execute("update time_table set subject = '" + row[1] + "' where id = " + row[3] + "")
                    self.cursor.execute("update time_table set start_time = '" + row[2] + "' where id = " + row[3] + ";")
                    self.conn.commit()
                except:
                    QMessageBox.about(self, "Error", "Enter all fields")
            else:
                QMessageBox.about(self, "Error", "Введите стандартизированое время")
        else: QMessageBox.about(self, "Error", "Введите положение недели 'в' - верхняя 'н' - няжняя  '-' - любая")
        self._update_monday_table()
        self._update_tuesday_table()
        self._update_wednesday_table()
        self._update_thursday_table()
        self._update_friday_table()

    def _change_teacher_table(self, rown, a):
        row = list()
        for i in range(a.columnCount()):
            try:
                row.append(a.item(rown, i).text())
            except:
                row.append(None)
            try:
                self.cursor.execute("update teacher set full_name = '" + row[0] + "' where id = " + row[2] + ";")
                self.conn.commit()
            except:
                QMessageBox.about(self, "Error", "Enter all fields")

    def _del_from_time_table(self, rown, a):
        row = list()
        for i in range(a.columnCount()):
            try:
                row.append(a.item(rown, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("delete from time_table where id = " + row[3] + ";")
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")
        self._update_monday_table()
        self._update_tuesday_table()
        self._update_wednesday_table()
        self._update_thursday_table()
        self._update_friday_table()

    def _del_from_teacher(self, rown, a):
        row = list()
        for i in range(a.columnCount()):
            try:
                row.append(a.item(rown, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("delete from teacher where id = " + row[2] + ";")
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")
        self._update_teacher_table()

    def _del_from_subject(self, rown, a):
        row = list()
        A = list()
        B = list()
        for i in range(a.columnCount()):
            try:
                row.append(a.item(rown, i).text())
            except:
                row.append(None)
        for i in range(self.teacher_table.rowCount()):
            try:
                A.append(self.teacher_table.item(i, 1).text())
            except:
                row.append(None)
        if row[0] in A:
            QMessageBox.about(self, "Error",
                              "Нельзя удалить предмет, пока он находится в расписании или в преподавателях")
        else:
            try:
                self.cursor.execute("delete from subject where name = '" + row[0] + "';")
                self.conn.commit()
            except:
                QMessageBox.about(self, "Error", "Нельзя удалить предмет, пока он находится в расписании или в преподавателях")
        self._update_subject_table()

    def _add_time_table(self, rown, a):
        row = list()
        A = list()
        for i in range(a.columnCount()):
            try:
                row.append(a.item(rown, i).text())
            except:
                row.append(None)
        for i in range(self.subject_table.rowCount()):
            try:
                A.append(self.subject_table.item(i, 0).text())
            except:
                row.append(None)
        if row[1] in A and row[1] != '':
            if row[0] == '-' or row[0] == 'н' or row[0] == 'в':
                if row[2] == '9:30' or row[2] == '11:20' or row[2] == '13:10' or row[2] == '15:25' or row[2] == '17:15':
                    try:
                        if a == self.monday_table:
                            self.cursor.execute(
                                "insert into time_table(day, pos, subject, start_time) values('Пн', '" + row[0] + "', '" + row[
                                    1] + "', '" + row[2] + "');")
                            self.conn.commit()
                        elif a == self.tuesday_table:
                            self.cursor.execute(
                                "insert into time_table(day, pos, subject, start_time) values('Вт', '" + row[0] + "', '" + row[
                                    1] + "', '" + row[2] + "');")
                            self.conn.commit()
                        elif a == self.wednesday_table:
                            self.cursor.execute(
                                "insert into time_table(day, pos, subject, start_time) values('Ср', '" + row[0] + "', '" + row[
                                    1] + "', '" + row[2] + "');")
                            self.conn.commit()
                        elif a == self.thursday_table:
                            self.cursor.execute(
                                "insert into time_table(day, pos, subject, start_time) values('Чт', '" + row[0] + "', '" + row[
                                    1] + "', '" + row[2] + "');")
                            self.conn.commit()
                        elif a == self.friday_table:
                            self.cursor.execute(
                                "insert into time_table(day, pos, subject, start_time) values('Пт', '" + row[0] + "', '" + row[
                                    1] + "', '" + row[2] + "');")
                            self.conn.commit()
                    except:
                        QMessageBox.about(self, "Error", "Enter all fields")
                    self._update_monday_table()
                    self._update_tuesday_table()
                    self._update_wednesday_table()
                    self._update_thursday_table()
                    self._update_friday_table()
                else: QMessageBox.about(self, "Error", "Введите стандартизированое время")
            else: QMessageBox.about(self, "Error", "Введите положение недели 'в' - верхняя 'н' - няжняя  '-' - любая")
        else: QMessageBox.about(self, "Error", "Такого предмета нет в БД")

    def _add_teacher(self, rown, a):
        A = list()
        row = list()
        for i in range(self.subject_table.rowCount()):
            try:
                A.append(self.subject_table.item(i, 0).text())
            except:
                row.append(None)
        for i in range(a.columnCount()):
            try:
                row.append(a.item(rown, i).text())
            except:
                row.append(None)
        if row[1] in A:
            try:
                self.cursor.execute("insert into teacher(full_name, subject) values('" + row[0] + "', '" + row[1] + "');")
                self.conn.commit()
            except:
                QMessageBox.about(self, "Error", "Enter all fields")
            self._update_teacher_table()
        else: QMessageBox.about(self, "Error", "Такого предмета нет в БД")

    def _add_subject(self, rown, a):
        row = list()
        for i in range(a.columnCount()):
            try:
                row.append(a.item(rown, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("insert into subject(name) values('" + row[0] + "');")
            self.conn.commit()
        except:
            QMessageBox(self, "Error", "Enter all fields")
        self._update_subject_table()

    def _update_shedule(self):
        self._update_monday_table()
        self._update_tuesday_table()
        self._update_wednesday_table()
        self._update_thursday_table()
        self._update_friday_table()

    def _update_teacher(self):
        self._update_teacher_table()

    def _update_subject(self):
        self._update_subject_table()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())