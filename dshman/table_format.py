class TableFormat:
    def __init__(self):
        self.format = '{:<12}{:<10}{:<45}{:<}'

    def print_title(self):
        print(f'{self.format}'.format('Name:', 'Status:', 'Description', 'File:'))

if __name__ == '__main__':
    test = TableFormat()
    test.print_title()
