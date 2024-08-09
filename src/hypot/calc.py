
def squared_hypot(opp, adj):
    """_summary_

    Args:
        opp (_type_): _description_
        adj (_type_): _description_

    Returns:
        _type_: _description_
    """
    return (opp**2) + (adj**2)


def hypot_length(square_hypot):
    """_summary_

    Args:
        square_hypot (_type_): _description_

    Returns:
        _type_: _description_
    """
    return square_hypot**(0.5)

def pythag(opp: float, adj:float) -> float:
    """_summary_

    Args:
        opp (float): _description_
        adj (float): _description_

    Returns:
        float: _description_
    """
    square_hypot = squared_hypot(opp, adj)
    return hypot_length(square_hypot)
