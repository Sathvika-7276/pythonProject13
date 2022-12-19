"""
Guitar
Estimate: 30 minutes
Actual:   15 minutes
"""

CURRENT_YEAR = 2022
VINTAGE_YEAR = 50


class Guitar:
    """ Storing details of guitar """

    def __init__(self, name="", year=0, cost=0):
        """ Construct guitar type from the given values."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """ Return string representation of a guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """ Get the age of guitar using the current year"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """ Check if guitar is older than vintage year """
        return self.get_age() >= VINTAGE_YEAR
