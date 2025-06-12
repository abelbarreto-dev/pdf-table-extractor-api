from numpy import nan
from pandas import DataFrame

data_frame_fruits = DataFrame(
    data=(
        ("Banana", "Fruit", 12, "A dozen"),
        ("Orange", 'Fruit', 8, nan)
    ),
    columns=("Name", "Category", "Quantity", "Observation")
)


data_frame_teams = DataFrame(
    data=(
        ("Kansas City Chiefs", 12, 3),
        ("New England Patriots", 10, 5)
    ),
    columns=("Teams", "Wins", "Lost")
)
