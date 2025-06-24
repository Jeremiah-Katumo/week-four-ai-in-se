def sort_dicts_in_place(data_list, key):
    """
    Sorts a list of dictionaries in place by a specified key.

    Args:
        data_list: A list of dictionaries.
        key: The key to sort the dictionaries by.

    Returns:
        None. The list is sorted in place.
    """
    try:
        data_list.sort(key=lambda x: x[key])
    except KeyError:
        print(f"Key '{key}' not found in one or more dictionaries.")
    except TypeError:
        print("Invalid input. Please pass a list of dictionaries.")
sample_data = [
    {"name": "Naomi", "age": 29},
    {"name": "Cate", "age": 22},
    {"name": "Zuri", "age": 31}
]

sort_dicts_in_place(sample_data, "age")
print(sample_data)
