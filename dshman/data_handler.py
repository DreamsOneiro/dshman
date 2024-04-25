import pickle
import os
import sys
from directory import Directory

class DataHandler(Directory):
    def __init__(self, DIR):
        Directory.__init__(self, DIR)
        self.DATA = {}

    def load_data(self):
        if os.path.getsize(self.DAT) > 0:
            # Check to make sure file is not empty
            with open(self.DAT, 'rb') as f:
                self.DATA = pickle.load(f)
            
    def sort_data(self):
        self.DATA = dict(sorted(self.DATA.items()))

    def write_data(self):
        self.sort_data()
        with open(self.DAT, 'wb') as f:
            pickle.dump(self.DATA, f)

    def add_data(self, KEY, VALUE):
        if KEY in self.DATA:
            print(f'\033[1;31mERROR: Script name: "{KEY}" alreay exist in list\033[0m')
            sys.exit(1)
        self.DATA[KEY] = VALUE

    def delete_data(self, KEY):
        if KEY in self.DATA:
            while True:
                try:
                    CONFIRM = input(f'Confirm delete script {KEY}? [y/n]: ')
                    if CONFIRM == 'y':
                        del self.DATA[KEY]
                    elif CONFIRM == 'n':
                        print('Aborted')
                    break
                except KeyboardInterrupt:
                    print('Aborted')
                    break
        else:
            print(f'Script name: "{KEY}" not in list')

    def change_data(self, NAME):
        if NAME in self.DATA:
            print('Leave empty for default')

            while True:
                try:
                    new_name = input(f'Please input new name [Default = "{self.DATA[NAME].name}"]: ')
                    if new_name in self.DATA:
                        print('Name already exist')
                    elif new_name == '':
                        new_name = NAME
                        break
                    else:
                        self.DATA[NAME].name = new_name
                        break
                except KeyboardInterrupt:
                    print('\n')
                    sys.exit(0)

            try:
                new_info = input('Please input new info: ')
                if new_info != '':
                    self.DATA[NAME].info = new_info
            except KeyboardInterrupt:
                print('\n')
                sys.exit(0)

            if not new_name is NAME:
                self.DATA[new_name] = self.DATA[NAME]
                del self.DATA[NAME]

        else:
            print(f'No script with name: "{NAME}"')
            sys.exit(0)

if __name__ == '__main__':
    test = DataHandler('/home/dreams/Programming/dshman/test')
    test.main()
    test.load_data()
    test_name = 'script1'
    print(test.DATA[test_name].name)
    print(test.DATA[test_name].info)
    test.change_data(test_name)
    print(test.DATA['script'].name)
    print(test.DATA['script'].info)
