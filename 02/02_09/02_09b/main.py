def find_second_smallest(my_list):
    if len(my_list) > 2:
        sorted_list = sorted(my_list)
        return sorted_list[1]
    return None

def find_second_smallest_search(my_list):
    smallest = float("inf")
    second_smallest = float("inf")
    if len(my_list) > 2:
        for ele in my_list:
            if ele < smallest:
                second_smallest = smallest
                smallest = ele
            elif ele < second_smallest:
                second_smallest = ele
        return second_smallest
    return None

print(find_second_smallest_search([5, 8, 3, 2, 6]))
