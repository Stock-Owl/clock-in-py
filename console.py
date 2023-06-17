from rich.console import Console
from rich.text import Text
from re import findall
from json import dumps, loads
    
# TODO: make this stuff using rich console and text

NAME: str = "terminal"

def foo(x, y):
    print(x*y)

def get_input(display_string: str | None = None) -> list:
    if display_string is None: display_string = NAME
    line_in: str = input(f"{display_string}>")
    line_in = line_in.split(' ')
    flags: list[str] = []
    print(type(line_in))
    return line_in

def execute(inputs: list[str]) -> None:
    command = inputs[0]
    attributes = list(inputs[1:])
    globals()[command](*attributes)
    """
    try:
        command = inputs[0]
        attributes = list(inputs[1:])
        globals()[command](*attributes)
    except TypeError:
        print(f"Type Error")   
        # missing argument / too many arguments / incorrect tpye
    except ValueError:
        print("ValueError")
    except KeyError:
        print(f"{command} is not a vlaid command")"""

def config(console: Console) -> None:
    pass    
     
def main() -> None:
    execute(get_input())

while __name__ == "__main__":
    main()

