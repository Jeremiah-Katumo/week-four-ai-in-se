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

# Faith's part
def sort_dicts_by_key(data_list, sort_key):
    """
    Sorts a list of dictionaries by a specified key.
    
    Parameters:
    - data_list: List[Dict] — a list of dictionaries
    - sort_key: str — the key to sort by

    Returns:
    - List[Dict]: the sorted list of dictionaries
    """
    if not all(isinstance(item, dict) for item in data_list):
        raise ValueError("All items in the list must be dictionaries.")

    if not all(sort_key in item for item in data_list):
        raise KeyError(f"Not all dictionaries contain the key '{sort_key}'.")

    return sorted(data_list, key=lambda x: x[sort_key])

    """
Comparison with GitHub Copilot Version:

When I wrote the manual version, I focused on making it safe and reliable.
I added checks to ensure every item in the list is a dictionary and that each
one has the key I want to sort by. If something is missing or incorrect, the
function raises clear errors, which would help me catch issues early when
dealing with uncertain or messy input data.

The GitHub Copilot version was surprisingly efficient and neat. It came up
with a shorter function that also includes a reverse parameter, making it
more flexible for sorting in both ascending and descending order. However,
it doesn't have any built-in checks, so if I passed in incomplete or invalid
data, it might break or behave unpredictably.

Both versions use Python's sorted() function, so they're equally fast in
terms of performance. What really sets them apart is how much safety and
flexibility they offer. I'd choose my manual version for cautious scenarios
where the data might not be perfect. Copilot's version is great when I'm
working with clean, consistent input and want something lightweight.

This comparison helped me understand the value of balancing error handling
with concise code.
"""


