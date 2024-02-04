#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary is None:
        print("Error: Dictionary is None.")
        return

    if not isinstance(a_dictionary, dict):
        print("Error: Input is not a dictionary.")
        return

    if key in a_dictionary:
        del a_dictionary[key]
