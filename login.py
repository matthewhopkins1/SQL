import tkinter as t
import pyodbc

class pythonSQL:
    def __init__(self):
        self.main_window = t.Tk()
        self.main_window.geometry("300x200")
        self.main_window.title("SQL Server Login")

        self.label_frame = t.Frame(self.main_window)
        self.entry_frame = t.Frame(self.main_window)
        self.bottom_frame = t.Frame(self.main_window)

        self.login_label = t.Label(self.label_frame, text="Login:")
        self.password_label = t.Label(self.label_frame, text="Password:")

        self.login_entry = t.Entry(self.entry_frame)
        self.password_entry = t.Entry(self.entry_frame, show="*")

        self.login_button = t.Button(self.bottom_frame, text="Login", command = self.access_database)

        self.login_label.pack(side="top")
        self.password_label.pack(side="top")
        self.login_entry.pack(side="top")
        self.password_entry.pack(side="top")
        self.login_button.pack(side="bottom")

        self.label_frame.pack(side="left")
        self.entry_frame.pack(side="right")
        self.bottom_frame.pack(side="bottom")

        t.mainloop()

    def access_database(self):
        login = self.login_entry.get()
        pw = self.password_entry.get()

        self.main_window.destroy()

        login = "matthew_hopkins1"
        pw = "MIS4322student"

        preList = {}
        courseList = []
        cn_str = (
        
    'Driver={SQL Server Native Client 11.0};'

    'Server=MIS-SQLJB;'

    'Database=School;'

    'UID='+login+';'

    'PWD='+pw+';'

    )

        cn = pyodbc.connect(cn_str)

        cursor = cn.cursor()
        cursor.execute('select * from School.dbo.Course')

        data = cursor.fetchall()
        for i in data:
            courseID= i[0]
            title = i[1]
            credits = i[2]
            deptID = i[3]
            
            preList = {'CourseID':courseID, 'Title':title, 'Credits':credits, 'DeptID':deptID}
            courseList.append(preList)
            print(courseList)

        a = int(input('Enter Course ID: '))

        for dictionary in courseList:
            if a == dictionary['CourseID']:
                print(f'Title: {dictionary["Title"]}')
                print(f'Credits: {dictionary["Credits"]}')
                print(f'Dept ID: {dictionary["DeptID"]}')

myinstance = pythonSQL()
