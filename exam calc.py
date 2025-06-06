def print_ascii_art():
    green_text = "\033[92m"
    reset_text = "\033[0m"
    
    ascii_art = r"""
  
    ______                        ______      __           __      __            
   / ____/  ______ _____ ___     / ____/___ _/ /______  __/ /___ _/ /_____  _____
  / __/ | |/_/ __ `/ __ `__ \   / /   / __ `/ / ___/ / / / / __ `/ __/ __ \/ ___/
 / /____>  </ /_/ / / / / / /  / /___/ /_/ / / /__/ /_/ / / /_/ / /_/ /_/ / /    
/_____/_/|_|\__,_/_/ /_/ /_/   \____/\__,_/_/\___/\__,_/_/\__,_/\__/\____/_/     
                                                                                 
  
    """
    dashed_line = "=" * 64
    print(green_text + dashed_line + reset_text)
    print(green_text + ascii_art + reset_text)
    print(green_text + dashed_line + reset_text)


def input_data(test1_results, test2_results, assignment_results, project_results, percentages, passed):
    green_text = "\033[92m"
    reset_text = "\033[0m"

    print(green_text + "Please input the students' respective marks (Percentages)" + reset_text)

    test1_mark = float(input("Test 1 Mark = "))
    test2_mark = float(input("Test 2 Mark = "))
    assignment_mark = float(input("Assignment Mark = "))
    project_mark = float(input("Project Mark = "))

    percentage = ((test1_mark * 30) + (test2_mark * 50) + (assignment_mark * 10) + (project_mark * 10)) / 100.0
    percentage = round(percentage)

    pass_status = percentage >= 50

    test1_results.append(test1_mark)
    test2_results.append(test2_mark)
    assignment_results.append(assignment_mark)
    project_results.append(project_mark)
    percentages.append(percentage)
    passed.append(pass_status)

    print("=" * 64 + reset_text)


def view_data(test1_results, test2_results, assignment_results, project_results, percentages, passed):
    green_text = "\033[92m"
    reset_text = "\033[0m"

    if not test1_results:
        print(green_text + "No results have been added" + reset_text)
    else:
        for idx in range(len(test1_results)):
            print(f"{green_text}Student {idx + 1} | Test 1: {test1_results[idx]} | Test 2: {test2_results[idx]} | Assignment: {assignment_results[idx]} | Project: {project_results[idx]}{reset_text}")
    print(green_text + "=" * 64 + reset_text)


def results_view(test1_results, test2_results, assignment_results, project_results, percentages, passed):
    green_text = "\033[92m"
    reset_text = "\033[0m"

    if not test1_results:
        print(green_text + "No results have been added" + reset_text)
    else:
        for idx in range(len(test1_results)):
            print(f"{green_text}Student {idx + 1} | Average: {percentages[idx]} | Passed: {passed[idx]}{reset_text}")
    print(green_text + "=" * 64 + reset_text)


def main():
    test1_results = []
    test2_results = []
    assignment_results = []
    project_results = []
    percentages = []
    passed = []

    print_ascii_art()
    
    green_text = "\033[92m"
    reset_text = "\033[0m"

    print(green_text + "Welcome to my results calculator app" + reset_text)

    while True:
        print(green_text + "Select an option from below")
        print("1. Input your data")
        print("2. View your inputted data")
        print("3. View results")
        print("4. Delete all data")
        print("5. Exit program" + reset_text)

        try:
            option = int(input("Choice: "))
        except ValueError:
            print(green_text + "Invalid input. Please enter a number between 1 and 5." + reset_text)
            continue

        print(green_text + "=" * 64 + reset_text)

        if option == 1:
            input_data(test1_results, test2_results, assignment_results, project_results, percentages, passed)
        elif option == 2:
            view_data(test1_results, test2_results, assignment_results, project_results, percentages, passed)
        elif option == 3:
            results_view(test1_results, test2_results, assignment_results, project_results, percentages, passed)
        elif option == 4:
            print(green_text + "Delete all data option selected." + reset_text)
            test1_results.clear()
            test2_results.clear()
            assignment_results.clear()
            project_results.clear()
            percentages.clear()
            passed.clear()
            print(green_text + "=" * 64 + reset_text)
        elif option == 5:
            break
        else:
            print(green_text + "Invalid option selected." + reset_text)


if __name__ == "__main__":
    main()
