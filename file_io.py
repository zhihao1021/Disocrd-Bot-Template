import json

class DataTypeError(Exception):
    def __init__(self, *args: object):
        super().__init__(*args)
    def __str__(self) -> str:
        return 'file_io.py: Wrong Data Values Type.'

class New_Dict_File():
    def __init__(self, file_name, init_data=None):
        self.file_name = file_name
        self.read()

    def __call__(self):
        return self.data

    def save(self):
        try:
            temp_data = json.dump(self.data)
            with open(self.file_name, mode='w', encoding='utf-8') as input_file:
                input_file.write(temp_data)
                input_file.close()
        except:
            raise DataTypeError

    def read(self):
        try:
            with open(self.file_name, mode='r', encoding='utf-8') as input_file:
                temp_data = json.load(input_file)
                input_file.close()
            self.data = temp_data
        except:
            raise DataTypeError