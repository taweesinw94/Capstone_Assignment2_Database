import Model

class Controller():

    def __init__(self):
        self.connector = Model.Connector()

    def select_all_value(self):
        result = self.connector.select_all()
        return result

    def select_top(self):
        result =self.connector.select_top()
        return result

    def select_top_student(self):
        result = self.connector.select_top_student()
        return result

    def create_table(self):
        createTable = self.connector.create_table()
        if(createTable):
            result = self.connector.populate_class_table()
        else:
            return createTable
        return result

    def find_status(self):
        student_query = self.select_all_value()
        student_list = [{'name': rows['name'], 'class': rows['class']} for rows in student_query]
        failed_student_query = self.connector.find_status()
        failed_student = [{'name': rows['name'], 'class': rows['class']} for rows in failed_student_query]
        grade_list = []
        for student in student_list:
            if(student in failed_student):
                grade_list.append({'name': student['name'], 'class': student['class'], 'status': 'Fail'})
            else:
                grade_list.append({'name': student['name'], 'class': student['class'], 'status': 'Pass'})
        return grade_list

    def terminate(self):
        self.connector.terminate()
