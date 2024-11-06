directions_turns: dict = {"N":["W", "E"], }

def create_runner(x: int = 0, y: int = 0, orientation: str = "N"): 
    global runner
    runner = {"Position": [x,y], "Direction": orientation}

def get_x(runner: dict) -> int:
    return runner["Position"][0]

def get_y(runner: dict) -> int:
    return runner["Position"][1]

def get_orientation(runner: dict) -> str:
    return runner["Direction"]

def turn(runner: dict, direction: str) -> dict:

    return runner


create_runner(1,3,"W")
print(get_orientation(runner))