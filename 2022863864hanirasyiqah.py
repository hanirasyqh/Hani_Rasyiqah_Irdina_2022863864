import tkinter as tk
import mysql.connector

class StudentMarkCalculationSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Student's Mark Calculation System")
        self.name = tk.Entry(master)
        self.e1 = tk.Entry(master)
        self.e2 = tk.Entry(master)
        self.e3 = tk.Entry(master)
        self.totText = tk.StringVar()
        self.avgText = tk.StringVar()
        self.gradeText = tk.StringVar()

        tk.Label(master, text="Name", fg="firebrick4", bg="light blue").place(x=60, y=60)
        tk.Label(master, text="Math Marks",  fg="firebrick4", bg="light blue").place(x=60, y=90)
        tk.Label(master, text="English Marks",  fg="firebrick4", bg="light blue").place(x=60, y=120)
        tk.Label(master, text="History Marks",  fg="firebrick4", bg="light blue").place(x=60, y=150)
        tk.Label(master, text="Total Marks:",  fg="firebrick4", bg="light blue").place(x=60, y=180)
        tk.Label(master, text="Avg:",  fg="firebrick4", bg="light blue").place(x=60, y=210)
        tk.Label(master, text="Grade:",  fg="firebrick4", bg="light blue").place(x=60, y=240)

        self.name.place(x=150, y=60)
        self.e1.place(x=150, y=90)
        self.e2.place(x=150, y=120)
        self.e3.place(x=150, y=150)

        result = tk.Label(master, text="", textvariable=self.totText).place(x=150, y=180)
        average = tk.Label(master, text="", textvariable=self.avgText).place(x=150, y=210)
        grade = tk.Label(master, text="", textvariable=self.gradeText).place(x=150, y=240)

        tk.Button(master, text="Calc", height=1, width=3, command=self.Ok).place(x=150, y=270)

    def Ok(self):
        result = int(self.e1.get()) + int(self.e2.get()) + int(self.e3.get())

        self.totText.set(result)

        average = result/3
        self.avgText.set(average)

        if (average > 50):
            grade = "pass!"
        else:
            grade = "fail"

        self.gradeText.set(grade)

        # Establish a connection to the MySQL server
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="student_marks"
        )

        # Create a cursor object to interact with the database
        cursor = mydb.cursor()

        # Inserting data into a table
        sql = "INSERT INTO `stud_score` (stud_name, math_score, english_score, history_score, total_marks, average, grade) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (self.name.get(), self.e1.get(), self.e2.get(), self.e3.get(), self.totText.get(), self.avgText.get(), self.gradeText.get())

        try:
            cursor.execute(sql, val)
            mydb.commit()
            print("Data inserted successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            mydb.rollback()
            
        cursor.close()
        mydb.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentMarkCalculationSystem(root)
    root.geometry("300x300")
    label= tk.Label(root,text= "STUDENT'S MARK CALCULATION SYSTEM",font=("Cambria", 12, "italic"), bg= "navy blue", 
                fg="light blue", bd=3, relief="groove")
    label.pack(ipadx=400)
    root.mainloop()

