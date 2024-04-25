import sys
import os
from cli_argparse import CLIArgs

class Commands(CLIArgs):
    def debug(self):
        print(self.args)

    def printError(self, message):
        print(f'\033[1;31m{message}\033[0m')
        sys.exit(1)

    """Main checks
    Prevent user input error.
    """
    def check_non_command(self):
        if (self.args.launch 
                or self.args.enable 
                or self.args.disable):
            # Prevent user from using some of the command as flag
            self.printError('[launch], [enable], and [disable] will not work as flag, please use [Command]')

    def check_flag_command(self):
        if self.args.command:
            if (self.args.add 
                    or self.args.name 
                    or self.args.info 
                    or self.args.list):
                # Prevent user from using both command and flag
                self.printError('Does not support use of both [Command] and [-flag], please check your input')

    def check_flag(self):
        flags = (bool(self.args.list), 
                 bool(self.args.delete), 
                 bool(self.args.add or self.args.name or self.args.info))
        if not sum(flags) <= 1:
            # A very specific Xor check
            self.printError('Too many flags, please check your input')

    def check_add_logic(self):
        if (bool(self.args.add) ^ 
            bool(self.args.name)):
            # Xor check to make sure script is given a name
            self.printError('Both [-a] and [-n] are needed to add new script')

    def check_command(self):
        def command_error():
            self.printError('Too many [commands], please check your input')

        if self.args.command:
            if len(self.args.command) > 2:
                command_error()

            elif len(self.args.command) == 2:
                commands = ('delete',
                            'enable', 
                            'disable')
                if not self.args.command[0].lower() in commands:
                # Return error if the command is not in the tuple above
                    command_error()

            elif len(self.args.command) == 1:
                if self.args.command[0].lower() == 'delete':
                    self.printError('Unkown command, please check your input. Do you mean "[delete] [name]"')

    def check_no_args(self):
        if not (self.args.command 
                or self.args.list 
                or self.args.add 
                or self.args.name 
                or self.args.info 
                or self.args.delete 
                or self.args.change):
            # Print welcome script when no input detected
            print('Welcome to Dreams Script Manager (v4.2)')
            sys.exit(0)

    def main_check(self):
        self.check_non_command()
        self.check_flag_command()
        self.check_flag()
        self.check_add_logic()
        self.check_command()
        self.check_no_args()

    """If statements
    Basic if statements to return True/False.
    """
    def if_list(self):
        if self.args.list:
            return True
        elif self.args.command:
            if self.args.command[0].lower() == 'list':
                return True

    def if_help(self):
        if self.args.command:
            if self.args.command[0] == 'help':
                return True

    def if_add(self):
        if self.args.add:
            return True

    def if_delete(self):
        if self.args.delete:
            return True
        elif self.args.command:
            if self.args.command[0].lower() == 'delete':
                return True

    def if_launch(self):
        if self.args.command:
            if self.args.command[0].lower() == 'launch':
                return True

    def if_enable(self):
        if len(self.args.command) == 2:
            if self.args.command[0].lower() == 'enable':
                return True

    def if_disable(self):
        if len(self.args.command) == 2:
            if self.args.command[0].lower() == 'disable':
                return True

    def if_enable_all(self):
        if len(self.args.command) == 1:
            if self.args.command[0].lower() == 'enable':
                return True

    def if_disable_all(self):
        if len(self.args.command) == 1:
            if self.args.command[0].lower() == 'disable':
                return True

    def if_change(self):
        if self.args.change:
            return True

    """Other functions
    Deliver data for dictionary modification
    """
    def script_add(self):
        self.args.add = os.path.abspath(self.args.add)
        if os.path.isfile(self.args.add):
            return  (self.args.add, 
                     self.args.name, 
                     self.args.info, 
                     "enabled")
        else:
            self.printError(f'File not found, please check directory "{self.args.add}"')

    def script_delete(self):
        if self.args.delete:
            return self.args.delete
        elif self.args.command:
            if self.args.command[0].lower() == 'delete':
                return self.args.command[1]

    def script_enable_disable(self):
        if self.args.command:
            return self.args.command[1]

    def script_change(self):
        return self.args.change

    def unknown_command(self):
        self.printError('Unknown command, please check your input')

if __name__ == '__main__':
    command = commands()
    command.debug()
    command.main_check()
