#!/usr/bin/python3
""" Algotithm to find the peak in a list """


def find_peak(list_of_integers):
    """ find the peak in a list of list_of_integers """
    # Check if the list is empty
    if not list_of_integers:
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return list_of_integers[left]
