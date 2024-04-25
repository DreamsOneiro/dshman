import os
import sys

class Directory:
    def __init__(self, DIR):
        self.dir = DIR
        self.datfile = f'{DIR}/script.dat'

    def check_kde_desktop(self):
        try:
            if os.environ.get('XDG_CURRENT_DESKTOP') == 'KDE':
                return True
            else:
                return False
        except:
            print('Error occured, check $XDG_CURRENT_DESKTOP')

    def check_dir(self):
        if not os.path.exists(self.dir):
            os.mkdir(self.dir)

    def check_dat(self):
        if not os.path.isfile(self.datfile):
            with open(self.datfile, 'x') as f:
                pass

    def create_desk(self):
        DESK_FILE = f'{os.path.expanduser("~")}/.config/autostart/dshman.desktop'
        with open(DESK_FILE, 'w') as f:
            f.write('[Desktop Entry]\n')
            f.write('Encoding=UTF-8\n')
            f.write('Type=Application\n')
            f.write('Terminal=false\n')
            f.write(f'Exec=/usr/local/bin/dshman launch\n')
            f.write('Name=Dreams Shell Manager\n')
        print('Shell Manager enabled')

    def remove_desk(self):
        DESK_FILE = f'{os.path.expanduser("~")}/.config/autostart/dshman.desktop'
        if os.path.isfile(DESK_FILE):
            os.remove(DESK_FILE)
        print('Shell Manager disabled')

    def main(self):
        if self.check_kde_desktop():
            self.check_dir()
            self.check_dat()
        else:
            print('dshman currently only wroks with KDE Plasma')
            sys.exit(0)

if __name__ == '__main__':
    test = directory('/home/dreams/Programming/python/dshman/code/test')
    test.main()
