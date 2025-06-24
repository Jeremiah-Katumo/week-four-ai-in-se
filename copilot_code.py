def sort_list_of_dictionaries(data_list: list, key: str) -> list:
    """
    Sorts a list of dictionaries by a specified key.

    Args:
        data_list: A list of dictionaries.
        key: The string key to sort the dictionaries by.

    Returns:
        A new list of dictionaries, sorted by the specified key.
    """
    return sorted(data_list, key=lambda x: x[key])
# Example usage:
if __name__ == "__main__":
    sample_data = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35}
    ]
    sorted_data = sort_list_of_dictionaries(sample_data, "age")
    print(sorted_data)
# Output: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]
# This code defines a function to sort a list of dictionaries by a specified key.
# It uses a lambda function to extract the value associated with the key for sorting.
# The example usage demonstrates how to use the function with a sample list of dictionaries.
# The sorted function is used to return a new list that is sorted based on the specified key
# without modifying the original list.
# The function is generic and can handle any list of dictionaries as long as the specified key exists.

# Faith's part
data = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Carol', 'age': 27}
]

sorted_data = sort_dicts_by_key(data, 'age')
print(sorted_data)
# Output: [{'name': 'Bob', 'age': 25}, {'name': 'Carol', 'age': 27}, {'name': 'Alice', 'age': 30}]

# Usage Example
data = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Carol', 'age': 27}
]

sorted_data = sort_dicts_by_key(data, 'age')
print(sorted_data)
# Output: [{'name': 'Bob', 'age': 25}, {'name': 'Carol', 'age': 27}, {'name': 'Alice', 'age': 30}]