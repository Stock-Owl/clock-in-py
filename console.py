from re import findall
from json import dumps, loads
from os import system
from inspect import signature
from log import Log
# TODO: make this stuff using rich console and text

name_: str
log_project_: str
log_user_: str
log_state: str
log_type_: str

def get_input(display_string: str | None = None) -> list:
    if display_string is None: display_string = name_
    line_in: str = input(f"{display_string}>")
    line_in = line_in.strip().lower().split(' ')
    return line_in

def execute(inputs: list[str]) -> None:
    command = inputs[0]
    attributes = list(inputs[1:])
    try:
        cmd_exec = globals()[command]
        cmd_exec(*attributes)
    except TypeError:
        attributes = get_input(display_string = f"{name_} {command}")
        try:
            cmd_exec(attributes)
        except TypeError:
            if attributes[0] == "exit":
                pass
            else:
                print(f"Fatal error: {command} takes {len(signature(cmd_exec).parameters)} arguments but {len(attributes)} were given")
                execute(inputs)
    except KeyError:
        print(f"Command \"{command}\" not found")

def config(prop: str, value: str) -> None:
    with open("./config.json", mode = 'r', encoding="utf8") as f:
        cfg = loads(f.read())    
        print(f"{prop}: {cfg[prop]} -> {value}")
        cfg[prop] = value
    with open("./config.json", mode = 'w', encoding="utf8") as f:
        f.write(dumps(cfg, indent = 2))

def cls() -> None:
    system("cls")

def load_config() -> None:
    try:
        with open("./config.json", mode="r", encoding="utf8") as f:
            cfg =  loads(f.read())
        global name_, log_project_, log_user_, log_state, log_type_
        name_ = cfg["name"]
        log_project_ = cfg["project"]
        log_user_ = cfg["user"]
        log_state = cfg["state"]
        log_type_ = cfg["type"]
        with open("./config.json", mode="w+", encoding="utf8") as f:
            if log_state == "START":
                cfg["state"] = "END"
            elif log_state == "END":
                cfg["state"] = "START"
            f.write(dumps(cfg, indent = 2))

    except FileNotFoundError:
        print("Couldn't find config file. Restoring to defaults")
        name_ = "terminal"
        log_project_, log_user_ = "", ""
        log_state = "START"

# 
# 
# 

# STARTUP block
if __name__ == "__main__":
    load_config()
    instance = Log(user = log_user_, project = log_project_, state = log_state, log_type = log_type_)
    
    def log(*args, **kwargs) -> None:
        instance.log(*args, **kwargs)
        # if log_state == "START":
        # config()
    def time_sum(*args, **kwargs) -> None:
        print(instance.time_sum(*args, **kwargs))

# MAIN block
while __name__ == "__main__":
    load_config()
    instance = Log(user = log_user_, project = log_project_, state = log_state, log_type = log_type_)
    lin = get_input()
    if lin[0] == "exit":
        break
    execute(lin)
    del instance
