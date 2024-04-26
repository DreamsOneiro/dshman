import os
import sys
from scripts import Scripts
from cli_logic import Commands
from data_handler import DataHandler
from table_format import TableFormat

def main():
    data = DataHandler(f'{os.path.expanduser("~")}/.dshman')
    command = Commands()
    format = TableFormat()

    data.main()
    command.main_check()
    
    if command.list():
        data.load()
        format.print_title()
        if data.data:
            for script in data.data.values():
                format.print_item(script)

    elif command.help():
        command.parser.print_help()

    elif command.add():
        new_script = Scripts(*command.script_add())
        data.load()
        data.add(new_script.name, new_script)
        data.write()

    elif command.delete():
        data.load()
        data.delete(command.script_delete())
        data.write()

    elif command.launch():
        data.load()
        for script in data.data.values():
            script.launch()

    elif command.enable():
        data.load()
        data.data[command.script_status()].status = 'enabled'
        print(f'{command.script_status()} is enabled')
        data.write()

    elif command.disable():
        data.load()
        data.data[command.script_status()].status = 'disabled'
        print(f'{command.script_status()} is disabled')
        data.write()

    elif command.change():
        data.load()
        data.change(command.script_change())
        data.write()

    elif command.enable_all():
        data.create_desk()
        
    elif command.disable_all():
        data.remove_desk()

    else:
        command.unknown_command()

if __name__ == '__main__':
    main()
    sys.exit(0)
