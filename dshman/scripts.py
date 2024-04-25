import os, subprocess

class Scripts:
    def __init__(self, fileDIR, name, info, status):
        self.fileDIR = fileDIR
        self.name = name
        self.info = info
        self.status = status

    def launch(self):
        if (os.path.isfile(self.fileDIR)) and (self.status == 'enabled'):
            subprocess.Popen(self.fileDIR, shell=False, stdin=None, stdout=None, stderr=None)
        if not os.path.isfile(self.fileDIR):
            print(f'\033[1;31mFailed to launch {self.name}, could not find {self.fileDIR}\033[0m')

if __name__ == '__main__':
    test = Scripts('/home/dreams/Programming/python/scripts/script1.sh', 'Script1', 'None', 'enabled')
    test.print_title()
    test.print_item()
