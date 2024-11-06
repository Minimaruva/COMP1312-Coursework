directions_turns: dict = {"N":["W", "E"], "W":["S", "N"], "S":["E", "W"], "E":["N", "S"]}
forward_directions:dict = {"N":["+", 1], "W":["-", 0], "S":["-", 1], "E":["+", 0]}

"""Make a main function to separate testing from actual functions"""

def create_runner(x: int = 0, y: int = 0, orientation: str = "N"): 
    global runner
    runner = {"Position": [x,y], "Direction": orientation}

def get_x(runner: dict) -> int:
    return runner["Position"][0]

def get_y(runner: dict) -> int:
    return runner["Position"][1]

def get_orientation(runner: dict) -> str:
    return runner["Direction"]

def turn(runner: dict, direction: str, direction_turns: dict =directions_turns) -> dict:
    """direction_turns is a dictionary where current direction is a key, 
    which gives a list in form [left_direction, right_direction]"""
    
    direction = direction.lower()

    if direction == 'left':
        runner["Direction"] = direction_turns[runner["Direction"]][0] 
    elif direction == 'right':
        runner["Direction"] = direction_turns[runner["Direction"]][1]
    return runner

def forward(runner: dict, forward_directions:dict = forward_directions):
    direction: str = runner["Direction"]
    operation: list[str,int] = forward_directions[direction]
    if operation[0] == '+':
        runner["Position"][operation[1]] += 1
    elif operation[0] == '-':
        runner["Position"][operation[1]] -= 1


create_runner(1,3,"N")
turn(runner, "Left")
forward(runner)
print(runner)