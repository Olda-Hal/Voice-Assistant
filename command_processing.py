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

def open_action(command):
    print(f"Opening {command[0]}")

def close_action(command):
    print("Closing {command[0]}")

def turn_on_action(command):
    print("Turning {command[0]} on")

def turn_off_action(command):
    print("Turning {command[0]} off")

def change_action(command):
    print("Changing {command[0]}")

action_dispatch = {
    Actions.OPEN: open_action,
    Actions.CLOSE: close_action,
    Actions.TURNON: turn_on_action,
    Actions.TURNOFF: turn_off_action,
    Actions.CHANGE: change_action
}


command = ["OPEN", "door"]
parser(command)