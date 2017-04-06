import MySQLdb

class Connector():

    def __init__(self):
        self.connection = connection= MySQLdb.connect(
        host='localhost',
        port=3306,
        user= admin,
        passwd= password,
        db= db_name,
        charset='utf8')

        self.cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)

    def select_all(self):
        try:
            self.cursor.execute("select * from score")
            result = self.cursor.fetchall()
            return(result)
        except:
            print('an error have occurs')

    def select_top(self):
        try:
            self.cursor.execute("select name, a.score, a.class from score a, (select max(score) as max_score, class from score group by class) temp where score=temp.max_score and a.class = temp.class")
            result = self.cursor.fetchall()
            return(result)
        except:
            print('an error have occurs')
    def select_top_student(self):
        try:
            self.cursor.execute("Select temp.name, temp.sum_score From (select sum(score) as sum_score, name from score group by name) temp where temp.sum_score = (Select max(temp.cum_score) as max_cum_score from (Select Sum(score) as cum_score, Name from score group by name) temp)")
            result = self.cursor.fetchall()
            return(result)
        except:
            print('an error have occurs')
    def create_table(self):
        try:
            self.cursor.execute("DROP TABLE IF EXISTS class")
            self.cursor.execute("Create table class(id int not null AUTO_INCREMENT, class_name varchar(255), students_number int, average float, max float, min float, SD float, Primary Key(id));")
            result = True
            return(result)
        except:
            return('an error have occurs')

    def populate_class_table(self):
        try:
            self.cursor.execute("Insert into class (class_name, students_number, average, `max`, `min`, SD) Select class, count(name) as student_number, avg(score) as average, max(score) as max, min(score) as min, stddev(score) as standard From score Group By class;")
            self.connection.commit()
            result = 'Success'
            return(result)
        except:
            print('an error have occurs')

    def terminate(self):
        self.connection.close()

    def find_status(self):
        try:
            self.cursor.execute("Select name, score.class From score, (Select avg(score) as average, STDDEV(score) as standard, class from score group by class) temp Where (score.score + standard) < average and score.class = temp.class; ")
            result = self.cursor.fetchall()
            return(result)
        except:
            print('an error have occurs')
