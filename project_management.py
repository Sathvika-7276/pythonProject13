import datetime


class ProjectManagement:
    def _init_(self, name, start_date, priority, cost_estimate=0.0, completion=0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion = completion

    def _repr_(self):
        return f"Project(name='{self.name}', start_date='{self.start_date}', priority={self.priority}," \
               f" cost_estimate={self.cost_estimate}, completion={self.completion})"


def load_projects(filename):
    """ Load projects from a file and return data """
    projects = []
    with open(filename, 'r') as f:
        # skip the header line
        next(f)
        for line in f:
            name, start_date, priority, cost_estimate, completion = line.strip().split('\t')
            start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
            priority = int(priority)
            cost_estimate = int(cost_estimate)
            completion = int(completion)
            project = ProjectManagement(name, start_date, priority, cost_estimate, completion)
            projects.append(project)
    return projects


def save_projects(filename, projects):
    """ Save a list of Project to a file """
    with open(filename, 'w') as f:
        f.write("name\tstart_date\tpriority\tcost_estimate\tcompletion\n")
        for project in projects:
            f.write(f"{project.name}\t{project.start_date}\t{project.priority}"
                    f"\t{project.cost_estimate}\t{project.completion}\n")


def display_projects(projects):
    incomplete_projects = []
    complete_projects = []
    for project in projects:
        if project.completion < 100:
            incomplete_projects.append(project)
        else:
            complete_projects.append(project)

    # sort both lists by priority
    incomplete_projects.sort(key=lambda x: x.priority)
    complete_projects.sort(key=lambda x: x.priority)

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(project)
    print("Completed projects:")
    for project in complete_projects:
        print(project)


def filter_projects_by_date(projects, date):
    filtered_projects = []
    for project in projects:
        if project.start_date > date:
            filtered_projects.append(project)
    # sort the list by start date
    filtered_projects.sort(key=lambda x: x.start_date)
    for project in filtered_projects:
        print(project)


def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name:")
    start_date = input("Start date (dd/mm/yy):")
    priority = input("Priority:")
    cost_estimate = int(input("Cost estimate: $"))
    completion = int(input("Percent complete:"))
    new_project = ProjectManagement(name, start_date, priority, cost_estimate, completion)
    projects.append(new_project)


def update_project(projects):
    name = input("Enter the name of the project to update: ")
    for project in projects:
        if project.name == name:
            completion = input("Enter the new completion % (leave blank to retain existing value): ")
            if completion:
                project.completion = int(completion)
            priority = input("Enter the new priority (leave blank to retain existing value): ")
            if priority:
                project.priority = int(priority)
            print(f"Project {project.name} has been updated.")
            break
    else:
        print("Project not found.")


def main():
    projects = []
    while True:
        print("Menu:")
        print("(L)oad projects")
        print("(S)ave projects")
        print("(D)isplay projects")
        print("(F)ilter projects by date")
        print("(A)dd new project")
        print("(U)pdate project")
        print("(Q)uit")
        choice = input("Enter your choice: ").lower()

        if choice == "l":
            filename = input("Enter the filename to load projects from: ")
            projects = load_projects(filename)
            print("Projects loaded.")
        elif choice == "s":
            filename = input("Enter the filename to save projects to: ")
            save_projects(filename, projects)
            print("Projects saved.")
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            date_str = input("Show projects that start after date (dd/mm/yy):")
            date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
            filter_projects_by_date(projects, date)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            print("Thank you for using custom-built project management software.")
            break


if __name__ == "_main_":
    main()
