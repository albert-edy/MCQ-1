import sqlite3
from os import path

class EdyodaMCQ:
    def __init__(self):
        self.path = "mcq_sqlite3.db"
        if not path.exists(self.path):
            self.dbconn = sqlite3.connect(self.path)
            self.cursor = self.dbconn.cursor()
            self.create_tables()
        else:
            self.dbconn = sqlite3.connect(self.path)
            self.cursor = self.dbconn.cursor()

    def create_tables(self):
        self.cursor.execute("""CREATE TABLE users(email text unique, super text)""")
        self.dbconn.commit()
        self.cursor.execute("""CREATE TABLE questions(subject text, difficulty text, q text, optiona text, optionb text, optionc text, answer text)""")
        self.dbconn.commit()
        

    def add_users(self):
        # Add dummy users
        self.cursor.execute("""INSERT INTO users(email, super) VALUES('superuser@mcq.com', 'y')""")
        self.cursor.execute("""INSERT INTO users(email, super) VALUES('user101@mcq.com', 'n')""")
        self.dbconn.commit()

    def add_qsn(self):
        print("Add questions")
        hs = ["subject: ", "difficulty: ", "q: ", "optiona: ", "optionb: ", "optionc: ", "answer: "]
        vs = []
        for i, h in enumerate(hs):
            print(h, end="")
            v = input()
            vs.append(v)
        self.cursor.execute("""INSERT INTO questions(subject, difficulty, q, optiona, optionb, optionc, answer) VALUES(?, ?, ?, ?, ?, ?, ?)""", tuple(vs))
        self.dbconn.commit()

    def attempt_mcq(self):
        print("Edyoda MCQ")
        print("enter subject: ", end='')
        subject = input()
        print("enter difficulty: ",end='')
        difficulty = input()
        self.cursor.execute("""SELECT * FROM questions WHERE subject=? AND difficulty=?""", (subject, difficulty))
        qsns = self.cursor.fetchall()
        score = 0
        for i,item in enumerate(qsns):
            v = ['a','b','c']

            print(i+1, item[2])
            print("option"+str(v[0])+":"+str(item[3]))
            print("option"+str(v[1])+":"+str(item[4]))
            print("option"+str(v[2])+":"+str(item[5]))
            print("Enter your option")
            ans = input()
            if ans == item[6]:
                score += 1
                print("correct ans and your score is", score)
    
            else:
                print("wrong ans and score is ", score)
        return score

    