def get_mark(points: int, bonus: int = 0) -> int:
    # Bonus - docstring jako napoveda k funkci:
    """
    Calculate the mark based on points and an optional bonus.

    Args:
        points (int): The base number of points earned by the student.
        bonus (int, optional): The additional points to be added. Defaults to 0.

    Returns:
        int: The calculated mark based on the total points and bonus.
    """
    # Optimalizace oproti 03: ulozeni souctu do promenne
    points_total = points + bonus
    if points_total <= 60:
        mark = 5
    elif points_total <= 70:
        mark = 4
    elif points_total <= 80:
        mark = 3
    elif points_total <= 90:
        mark = 2
    else:
        mark = 1
    return mark


result = get_mark(50, 30)
print(result)


# Typovani lze aplikovat i na promenne
cislo: int = 10
retezec: str = "string"