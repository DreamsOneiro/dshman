import pickle
import os
import sys
from directory import Directory


class DataHandler(Directory):
    def __init__(self, DIR):
        Directory.__init__(self, DIR)
        self.data = {}

    def load(self):
        if os.path.getsize(self.datfile) > 0:
            # Check to make sure file is not empty
            with open(self.datfile, 'rb') as f:
                self.data = pickle.load(f)

    def sort(self):
        self.data = dict(sorted(self.data.items()))

    def write(self):
        self.sort()
        with open(self.datfile, 'wb') as f:
            pickle.dump(self.data, f)

    def add(self, KEY, VALUE):
        if KEY in self.data:
            print(f'\033[1;31mERROR: Script name: "{KEY}"\
                    alreay exist in list\033[0m')
            sys.exit(1)
        self.data[KEY] = VALUE

    def delete(self, KEY):
        if KEY in self.data:
            while True:
                try:
                    CONFIRM = input(f'Confirm delete script {KEY}? [y/n]: ')
                    if CONFIRM == 'y':
                        del self.data[KEY]
                    elif CONFIRM == 'n':
                        print('Aborted')
                    break
                except KeyboardInterrupt:
                    print('Aborted')
                    break
        else:
            print(f'Script name: "{KEY}" not in list')

    def change(self, NAME):
        if NAME in self.data:
            print('Leave empty for default')

            while True:
                try:
                    new_name = input(f'Please input new name [Default] = \
                                        "{self.data[NAME].name}"]: ')
                    if new_name in self.data:
                        print('Name already exist')
                    elif new_name == '':
                        new_name = NAME
                        break
                    else:
                        self.data[NAME].name = new_name
                        break
                except KeyboardInterrupt:
                    print('\n')
                    sys.exit(0)

            try:
                new_info = input('Please input new info: ')
                if new_info != '':
                    self.data[NAME].info = new_info
            except KeyboardInterrupt:
                print('\n')
                sys.exit(0)

            if new_name is not NAME:
                self.data[new_name] = self.data[NAME]
                del self.data[NAME]

        else:
            print(f'No script with name: "{NAME}"')
            sys.exit(0)


if __name__ == '__main__':
    test = DataHandler('/home/dreams/Programming/dshman/test')
    test.main()
    test.load()
    test_name = 'script1'
    print(test.DATA[test_name].name)
    print(test.DATA[test_name].info)
    test.change(test_name)
    print(test.DATA['script'].name)
    print(test.DATA['script'].info)
