import os, sys
from scripts import Scripts
from cli_logic import Commands
from data_handler import DataHandler
from table_format import TableFormat

if __name__ == '__main__':
    data = DataHandler(f'{os.path.expanduser("~")}/.dshman')
    command = Commands()
    format = TableFormat()

    data.main()
    command.main_check()
    
    if command.if_list():
        data.load_data()
        format.print_title()
        if data.DATA:
            for script in data.DATA:
                format.print_item(data.DATA[script])

    elif command.if_help():
        command.parser.print_help()

    elif command.if_add():
        new_script = Scripts(*command.script_add())
        data.load_data()
        data.add_data(new_script.name, new_script)
        data.write_data()

    elif command.if_delete():
        data.load_data()
        data.delete_data(command.script_delete())
        data.write_data()

    elif command.if_launch():
        data.load_data()
        for script in data.DATA:
            data.DATA[script].launch()

    elif command.if_enable():
        data.load_data()
        data.DATA[command.script_enable_disable()].status = 'enabled'
        data.write_data()

    elif command.if_disable():
        data.load_data()
        data.DATA[command.script_enable_disable()].status = 'disabled'
        data.write_data()

    elif command.if_change():
        data.load_data()
        data.change_data(command.script_change())
        data.write_data()

    elif command.if_enable_all():
        data.create_desk()
        
    elif command.if_disable_all():
        data.remove_desk()

    else:
        command.unknown_command()
    
    sys.exit(0)
