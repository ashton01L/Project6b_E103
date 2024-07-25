# Author: Ashton Lee
# Github User: ashton01L
# Date: 7/25/2024
# Description: Define a function named 'add_surname' that takes
# as a parameter a list of first names.

def add_surname(first_names):
    """
    Adds surname of Kardashian to all names within a given List
    that begin with the letter K and concatenates the two names

    :return: List of strings of concatenated names wherein the
        first letter of both bthe first name and the last name
        start with K and the last name is specifically
        "Kardashian"

    :param: first_names, which is List of strings of first names
    """

    # Return each of the concatenated strings wherein the first
    #     names that begin with the letter K are added to the last
    #     name Kardashian
    return [name + " Kardashian" for name in first_names if name.startswith('K')]

# Example usage:
# first_names = ["Kiki", "Krystal", "Pavel", "MaryKay", "Annie", "Koala"]
# print(add_surname(first_names))
