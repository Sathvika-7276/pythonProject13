"""
Guitar
Estimate: 30 minutes
Actual:   15 minutes
"""

CURRENT_YEAR = 2022
VINTAGE_YEAR = 50


class Guitar:
    """ Storing details of guitar """

    def __init__(self, name="", year=0, cost=0.0):
        """ Construct guitar type from the given values."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """ Return string representation of a guitar."""
        return f"{self.name}, {self.year}, {self.cost}"

    def get_age(self):
        """ Get the age of guitar using the current year"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """ Check if guitar is older than vintage year """
        return self.get_age() >= VINTAGE_YEAR

    def __lt__(self, other):
        """ Sorting guitars by year released """
        return self.year < other.year


def main():
    guitars_list = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        add_guitar = Guitar(name, year, cost)
        guitars_list.append([add_guitar])
        print(add_guitar)
        name = input("Name: ")

    from csv import writer, QUOTE_NONE
    with open('guitars.csv', 'a', newline='') as f_object:
        writer_object = writer(f_object, quoting=QUOTE_NONE, escapechar=" ")
        f_object.write("\n")
        writer_object.writerows(guitars_list)
        f_object.close()


if __name__ == "__main__":
    main()
