import pickle, os, sys
from directory_manager import manageDIR

class DataHandler(manageDIR):
    def __init__(self, DIR):
        manageDIR.__init__(self, DIR)
        self.DATA = {}

    def load_data(self):
        if os.path.getsize(self.DAT) > 0:
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

if __name__ == '__main__':
    test = DataHandler('/home/dreams/Programming/python/dshman/code/test')
    test.main()
    test.load_data()
    test.add_data(dict_test)
