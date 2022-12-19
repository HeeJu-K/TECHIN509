from typing import List

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]


def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """

    # Implement your code here.

    #when entered coordinates does not contain character to be replaced with
    if input_board[x][y] != old:
        return input_board
    #when entered coordinate is outside boundary
    if x<0 and y<0 or x>=len(input_board) or y>=len(input_board[0]):
        return input_board
    #replace row with old str with row with new str 
    output_board = input_board
    output_board[x] = input_board[x][:y] + new + input_board[x][y+1:]
    
    #recurse if next coordinate is in range 
    if x < len(input_board)-1:
        output_board = flood_fill(output_board, old, new, x+1, y)
    if x > 0:
        output_board = flood_fill(output_board, old, new, x-1, y)
    if y < len(input_board[0])-1:
        output_board = flood_fill(output_board, old, new, x, y+1)
    if y > 0:
        output_board = flood_fill(output_board, old, new, x, y-1)

    return output_board


modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)

# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....