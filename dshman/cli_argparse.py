import argparse

class cli_args():
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('command', help='Insert command', nargs='*')
        self.parser.add_argument('-a', '--add', metavar='DIR', help='Add .sh file from directory')
        self.parser.add_argument('-n', '--name', help='Custom name for shell script')
        self.parser.add_argument('-i', '--info', help='(Optional)Add description for scripts')
        self.parser.add_argument('-c', '--change', metavar='', help='Change script content')
        self.parser.add_argument('-d', '--delete', metavar='', help= '[Command]Delete scripts by name')
        self.parser.add_argument('--launch', help='[Command]Launch all enabled shell script', action='store_true')
        self.parser.add_argument('--enable', help='[Command]Enable dshman at launch or enable sh by name', action='store_true')
        self.parser.add_argument('--disable', help='[Command]Disable dshman at launch or disable sh by name', action='store_true')
        self.parser.add_argument('-l','--list', help='[Command]Show list of shell scripts', action='store_true')
        self.args = self.parser.parse_args()
