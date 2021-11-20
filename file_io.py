import json, copy
from os.path import isfile

class DataTypeError(Exception):
    def __init__(self, *args: object):
        super().__init__(*args)
    def __str__(self) -> str:
        return "file_io.py: Wrong data values type."

class SampleFileError(Exception):
    def __init__(self, *args: object):
        super().__init__(*args)
    def __str__(self) -> str:
        return "file_io.py: Sample file doesn't exist"

class New_File():
    def __init__(self, file_name: str, init_data=None):
        self.file_name = file_name
        if init_data != None:
            self.sample_data = init_data
            self.save(sample_data=True)
        else:
            self.read(sample_data=True)
        self.read()

    def __call__(self):
        return self.data

    def save(self, sample_data: bool=False):
        if sample_data:
            try:
                temp_data = json.dump(self.sample_data, indent=4, separators=(',', ': '), sort_keys=False)
                with open(f'sample-{self.file_name}', mode='w', encoding='utf-8') as output_file:
                    output_file.write(temp_data)
                    output_file.close()
            except:
                raise DataTypeError
        else:
            try:
                temp_data = json.dump(self.data, indent=4, separators=(',', ': '), sort_keys=False)
                with open(self.file_name, mode='w', encoding='utf-8') as output_file:
                    output_file.write(temp_data)
                    output_file.close()
            except:
                raise DataTypeError

    def read(self, sample_data: bool=False):
        if sample_data:
            if isfile(f'sample-{self.file_name}'):
                try:
                    with open(f'sample-{self.file_name}', mode='r', encoding='utf-8') as input_file:
                        temp_data = json.load(input_file)
                        input_file.close()
                    self.sample_data = copy.deepcopy(temp_data)
                except:
                    raise DataTypeError
            else:
                raise SampleFileError
        else:
            if isfile(self.file_name):
                try:
                    with open(self.file_name, mode='r', encoding='utf-8') as input_file:
                        temp_data = json.load(input_file)
                        input_file.close()
                    self.data = copy.deepcopy(temp_data)
                except:
                    raise DataTypeError
            else:
                self.data = copy.deepcopy(self.sample_data)
                self.save()