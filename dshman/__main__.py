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
        data.load_data()
        format.print_title()
        if data.data:
            for script in data.data:
                format.print_item(data.data[script])

    elif command.help():
        command.parser.print_help()

    elif command.add():
        new_script = Scripts(*command.script_add())
        data.load_data()
        data.add_data(new_script.name, new_script)
        data.write_data()

    elif command.delete():
        data.load_data()
        data.delete_data(command.script_delete())
        data.write_data()

    elif command.launch():
        data.load_data()
        for script in data.data:
            data.data[script].launch()

    elif command.enable():
        data.load_data()
        data.data[command.script_enable_disable()].status = 'enabled'
        data.write_data()

    elif command.disable():
        data.load_data()
        data.data[command.script_enable_disable()].status = 'disabled'
        data.write_data()

    elif command.change():
        data.load_data()
        data.change_data(command.script_change())
        data.write_data()

    elif command.enable_all():
        data.create_desk()
        
    elif command.disable_all():
        data.remove_desk()

    else:
        command.unknown_command()

if __name__ == '__main__':
    main()
    sys.exit(0)
