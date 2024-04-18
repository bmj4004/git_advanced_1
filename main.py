from typing import List

# Skeleton code for even_list
def even_list(int_list: List[int]) -> List[int]:
    """
    Determines if a number is even and return an even list.
    Args:
        int_list: A list of integer.
    Returns:
        A list of even integers.
    """
    # TODO: Implement even_list
    return_list = []
    for element in int_list:
        if element % 2 == 0:
            return_list.append(element)
    
    return return_list

# Skeleton code for sum_of_squares_of_even
def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    """
    Computes the sum of the squares of all even numbers in a li
    Args:
        even_int_list: A list of even integers.
    Returns:
        The sum of the squares of all even numbers in the list.
    """
    # TODO: Implement sum_of_squares_of_even
    sqaure_sum = 0
    for element in even_int_list:
        sqaure_sum += element ** 2
    
    return sqaure_sum


# Main function
def main():
    # Example list
    int_list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    int_list_2 = [7, 0, 8, 7, 9]
    int_list_3 = [58, 6, -22, 91, 33, 49, 44, 63, -79, 12]
    all_list = [int_list_1, int_list_2, int_list_3]

    for num, int_list in enumerate(all_list):
        print('list', num, ':', int_list)
        even_int_list = even_list(int_list)
        output = sum_of_squares_of_even(even_int_list)
        print('output: ',output, end="\n\n")

# Boilerplate code
if __name__ == "__main__":
    main()