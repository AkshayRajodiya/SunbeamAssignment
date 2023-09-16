# #1) Given a dictionary of students and their favourite colours:
# people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'}
# A. Find out how many students are in the list
# B. Change Lisa’s favourite colour
# C. Remove 'Jenny' and her favourite colour
# D. Sort and print students and their favourite colours alphabetically by name
def dictionary_of_stud():
    people = {'Arham': 'Blue', 'Lisa': 'Yellow', 'Vinod': 'Purple', 'Jenny': 'Pink'}
    # list_stud = list(people.keys())
    # list_stud.sort()
    # list_color = list(people.values())
    # print(len(people))   # A. Find out how many students are in the list
    # print(list_stud)
    # list_color.sort()       # D. Sort and print students and their favourite colours alphabetically by name
    # for key in people.keys():
    #     if key == 'Lisa':
    #         people[key] = 'red'  # B. Change Lisa’s favourite colour
    #     if key == 'Jenny':
    #         people[key] = None   # C. Remove 'Jenny' and her favourite colour
    #
    # print(list_color)
    # print(people)

    print(len(people))  # A. Find out how many students are in the list
    if "Lisa" in people:
        people['Lisa'] = 'White'  # B. Change Lisa’s favourite colour
    if "Jenny" in people:
        people["Jenny"] = None  # C. Remove 'Jenny' and her favourite colour
    sorted_dict = dict(
        sorted(people.items()))  # D. Sort and print students and their favourite colours alphabetically by name

    print(sorted_dict)
    print(people)


dictionary_of_stud()
