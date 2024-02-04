#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        print("Error: Dictionary is None.")
        return

    if not isinstance(a_dictionary, dict):
        print("Error: Input is not a dictionary.")
        return

    sorted_keys = sorted(a_dictionary.keys())

    for key in sorted_keys:
        value = a_dictionary[key]
        print(f'{key}: {value}')
