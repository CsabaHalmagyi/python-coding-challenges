
def get_combined_list_no_repetition(list1, list2):
    print("")


def get_unique_elements_from_lists(list1, list2):
    unique_list = []
    for item in list1:
        if item not in list2:
            unique_list.append(item)
    for item in list2:
        if item not in list1:
            unique_list.append(item)
    return unique_list


def compare_shopping_lists():
    week_a = ["bread", "milk", "tea", "chocolate"]
    week_b = ["tea", "biscuits", "fanta", "cheese", "milk"]
    unique_list = get_unique_elements_from_lists(week_a, week_b)
    print(unique_list)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    compare_shopping_lists()

