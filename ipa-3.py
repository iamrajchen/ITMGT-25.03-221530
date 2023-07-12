'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
def relationship_status(from_member, to_member, social_graph):
    if to_member in social_graph[from_member]['following'] and from_member in social_graph[to_member]['following']:
        return "friends"
    elif from_member in social_graph[to_member]['following']:
        return "followed by"
    elif to_member in social_graph[from_member]['following']:
        return "follower"
    else:
        return "no relationship"


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
def tic_tac_toe(board):
    size = len(board[0])

    diagonal = [[board[i][i] for i in range(size)], [board[i][size - i - 1] for i in range(size)]]
    column = []
    for row_num in range(size):
        column.append([board[i][row_num] for i in range(size)])

    dimensions = [diagonal, column, board]

    for dimension in dimensions:
        for _ in dimension:
            win_cn = 0
            square_checker = _[0]
            for square in _:
                if square == square_checker:
                    win_cn += 1
            if win_cn == size and win_cn != 0:
                return square_checker

    return "NO WINNER"



def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
def eta(first_stop, second_stop, route_map):
    if (first_stop, second_stop) in route_map:
        return route_map[(first_stop, second_stop)]["time_mins"]
    
    total_time = 0
    current_stop = first_stop

    while current_stop != second_stop:
        found_key = next((key for key in route_map if key[0] == current_stop), None)
        if found_key:
            total_time += route_map[found_key]["time_mins"]
            current_stop = found_key[1]
        else:
            break

    return total_time
    


   