import json

class New_Dict_File():
    def __init__(self, file_name):
        with open(file_name, mode='r', encoding='utf-8') as input_file:
            self.data = json.load(input_file)
            input_file.close()

    def __call__(self):
        return self.data