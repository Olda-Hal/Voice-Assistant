import enum

def process(command):
    if "COMMAND" in command:
        parser(command.split(" "))
        print("Command executed")
    else:
        raise Exception("Invalid command")

def parser(command):
    action_enum = Actions[command[0]]
    action_function = action_dispatch.get(action_enum)
    
    if action_function:
        arguments = command[1:]
        action_function(*arguments)
    else:
        raise Exception("Invalid action")


class Actions(enum.Enum):
    OPEN = 1
    CLOSE = 2
    TURNON = 3
    TURNOFF = 4
    CHANGE = 5

def open_action():
    print("Opening something")

def close_action():
    print("Closing something")

def turn_on_action():
    print("Turning something on")

def turn_off_action():
    print("Turning something off")

def change_action():
    print("Changing something")

# Dispatch tabulka pro spojení akcí a funkcí
action_dispatch = {
    Actions.OPEN: open_action,
    Actions.CLOSE: close_action,
    Actions.TURNON: turn_on_action,
    Actions.TURNOFF: turn_off_action,
    Actions.CHANGE: change_action
}


# Příklad použití
command = ["OPEN", "door"]
parser(command)

command = ["TURNON", "light", "switch"]
parser(command)