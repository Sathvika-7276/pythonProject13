def main():
    print("- (L)oad projects", end="\n")
    print("- (S)ave projects", end="\n")
    print("- (D)isplay projects", end="\n")
    print("- (F)ilter projects by date", end="\n")
    print("- (A)dd new project", end="\n")
    print("- (U)pdate project", end="\n")
    print("- (Q)uit", end="\n")
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "L":
            text_file = input("Enter your text file:")
            load_file(text_file)
    print("Thank you for using custom-built project management software.")


def load_file(text_file):
    with open(text_file) as f:
        contents = f.read()
    print(contents)


def set_limit(low):
    """Set high limit to new value from user input."""
    print("Set new limit")
    new_high = int(input(f"Enter a new high value, above {low}: "))
    while new_high <= low:
        new_high = int(input(f"Enter a new high value, above {low}: "))
    return new_high


def display_range(low, high):
    value = 0
    for value in range(low, high):
        print(value, end=" ")
        value += 1
    return value


main()