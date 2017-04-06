import Controller

class View():

    def __init__(self):
        self.result = None
        self.controller = Controller.Controller()

    def select_all(self):
        self.result = self.controller.select_all_value()
        self.controller.terminate()

    def select_top(self):
        self.result = self.controller.select_top()
        self.controller.terminate()

    def select_top_student(self):
        self.result = self.controller.select_top_student()
        self.controller.terminate()

    def create_table(self):
        self.result = self.controller.create_table()
        self.controller.terminate()

    def find_status(self):
        self.result = self.controller.find_status()
        self.controller.terminate()

    def render(self, attribute):
        if(attribute == 1):
            for row in self.result:
                print(row["name"], row["score"], row["class"])
        if(attribute == 2):
            for row in self.result:
                print(row["name"], row["score"], row["class"])
        if(attribute == 3):
            for row in self.result:
                print(row["name"], row["sum_score"])
        if(attribute == 4):
            print(self.result)
        if(attribute == 5):
            for row in self.result:
                print(row["name"], row["class"], row["status"])
