import math

def length(lst):
    """Returns the number of elements in the list."""
    return len(lst)

def mean(lst):
    """Calculates the arithmetic mean of the list."""
    if not lst:  # Handle empty list
        return None
    return sum(lst) / len(lst)

def range_of_list(lst):
    """Returns the difference between the maximum and minimum values in the list."""
    if not lst:  # Handle empty list
        return None
    return max(lst) - min(lst)

def median(lst):
    """Calculates the median of the list."""
    if not lst:  # Handle empty list
        return None
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

def standard_deviation(lst):
    """Calculates the standard deviation of the list."""
    if not lst:
        return None
    m = mean(lst)
    variance = sum((x - m) ** 2 for x in lst) / len(lst)
    return math.sqrt(variance)

def list_statistics(lst):
    """Returns a dictionary containing various statistics of the list."""
    if not lst:
        return {
            "length": 0,
            "mean": None,
            "range": None,
            "median": None,
            "standard_deviation": None
        }
    return {
        "length": length(lst),
        "mean": mean(lst),
        "range": range_of_list(lst),
        "median": median(lst),
        "standard_deviation": standard_deviation(lst)
    }

# Example usage
if __name__ == "__main__":
    # Test cases
    numbers = [1, 2, 3, 4, 5]

    print("Length:", length(numbers))
    print("Mean:", mean(numbers))
    print("Range:", range_of_list(numbers))
    print("Median:", median(numbers))
    print("Standard Deviation:", standard_deviation(numbers))
    print("Statistics:", list_statistics(numbers))

    # Edge cases
    empty_list = []
    print("Empty List Statistics:", list_statistics(empty_list))

    single_element = [10]
    print("Single Element Statistics:", list_statistics(single_element))

    negative_numbers = [-5, -2, -3, -8, -1]
    print("Negative Numbers Statistics:", list_statistics(negative_numbers))

    float_numbers = [1.5, 2.8, 3.1, 4.6, 5.0]
    print("Float Numbers Statistics:", list_statistics(float_numbers))
