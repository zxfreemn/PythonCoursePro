import sqlite3
import datetime
import json
import os.path
import task1_db_configure


class SQLiteWrapper:
    def __init__(self, dbname):
        self._dbname = dbname

    def __enter__(self):
        self._conn = sqlite3.connect(self._dbname)
        self._conn.row_factory = sqlite3.Row
        self._cur = self._conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._conn.close()

    def execute(self, query, params=None):
        if query.split()[0].lower() == 'select':
            return self.select(query, params)

        try:
            if params:
                self._cur.execute(query, params)
            else:
                self._cur.execute(query)
            self._conn.commit()
        except sqlite3.IntegrityError as exception:
            print(f'Exception {exception} has occurred while {query} execution')

    def select(self, query, params=None):
        result = dict()
        result["query"] = f"{query}, {params}" if params else query
        result["records"] = dict()
        item = 1
        if params:
            self._cur.execute(query, params)
        else:
            self._cur.execute(query)
        for row in self._cur.fetchall():
            result["records"][item] = dict(row)
            item += 1
        return json.dumps(result)


if __name__ == '__main__':
    dbname = 'students.db'
    db = SQLiteWrapper(dbname)
    if not os.path.exists(dbname):
        task1_db_configure.db_scheme_creation(db)
        task1_db_configure.db_initial_content(db)

    with db:
        # find all students grades
        all_students_grades = db.select(
            "SELECT St.Name, St.Surname, C.Course, Sb.Subject, SG.Date, SG.Grade"
            " FROM Students AS St, Courses AS C, Subjects AS Sb, StudentGrades AS SG"
            " WHERE SG.StudentID = St.Id AND SG.SubjectID = Sb.Id AND St.CourseID = C.Id")
        print(all_students_grades)

        # find Management course students grades
        manag_students_grades = db.select(
            "SELECT St.Name, St.Surname, C.Course, Sb.Subject, SG.Date, SG.Grade"
            " FROM Students AS St, Courses AS C, Subjects AS Sb, StudentGrades AS SG"
            " WHERE SG.StudentID = St.Id AND SG.SubjectID = Sb.Id AND St.CourseID = C.Id"
            " AND C.Course = 'Management'")
        print(manag_students_grades)

        # find Electric Power Engineering students grades from October
        oct_elec_students_grades = db.select(
            "SELECT St.Name, St.Surname, C.Course, Sb.Subject, SG.Date, SG.Grade"
            " FROM Students AS St, Courses AS C, Subjects AS Sb, StudentGrades AS SG"
            " WHERE SG.StudentID = St.Id AND SG.SubjectID = Sb.Id AND St.CourseID = C.Id"
            " AND C.Course = 'Electric Power Engineering'"
            " AND SG.Date BETWEEN '2021-10-01' AND '2021-10-31'")
        print(oct_elec_students_grades)

        date_exam1 = datetime.date(2021, 10, 1)
        db.execute("INSERT INTO StudentGrades (StudentID, SubjectID, Date, Grade) "
                   "VALUES (5, 1, (:date_exam1), 5)", {'date_exam1': date_exam1})
        db.execute("INSERT INTO StudentGrades (StudentID, SubjectID, Date, Grade) "
                   "VALUES (5, 2, (:date_exam1), 3)", {'date_exam1': date_exam1})

        # find Electric Power Engineering students grades from October
        date_exam2 = datetime.date(2021, 10, 31)
        oct_elec_students_grades = db.select(
            "SELECT St.Name, St.Surname, C.Course, Sb.Subject, SG.Date, SG.Grade"
            " FROM Students AS St, Courses AS C, Subjects AS Sb, StudentGrades AS SG"
            " WHERE SG.StudentID = St.Id AND SG.SubjectID = Sb.Id AND St.CourseID = C.Id"
            " AND C.Course = 'Electric Power Engineering'"
            " AND SG.Date BETWEEN (:date_exam1) AND (:date_exam2)",
            {'date_exam1': date_exam1, 'date_exam2': date_exam2})
        print(oct_elec_students_grades)

        # find Electric Power Engineering students grades < 4 from October
        oct_elec_students_grades = db.execute(
            "SELECT St.Name, St.Surname, C.Course, Sb.Subject, SG.Date, SG.Grade"
            " FROM Students AS St, Courses AS C, Subjects AS Sb, StudentGrades AS SG"
            " WHERE SG.StudentID = St.Id AND SG.SubjectID = Sb.Id AND St.CourseID = C.Id"
            " AND C.Course = 'Electric Power Engineering'"
            " AND SG.Date BETWEEN (:date_exam1) AND (:date_exam2)"
            " AND SG.Grade < 4",
            {'date_exam1': date_exam1, 'date_exam2': date_exam2})
        print(oct_elec_students_grades)
