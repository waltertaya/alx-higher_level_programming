#!/usr/bin/python3
""" Find the peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ Find a peak in list_of_integers """

    if list_of_integers is None or list_of_integers == []:
        return None

    list_len = len(list_of_integers)
    if list_len == 1:
        return list_of_integers[0]

    if list_len == 2:
        return max(list_of_integers)

    mid = list_len // 2

    if list_of_integers[mid] > list_of_integers[mid - 1] and \
            list_of_integers[mid] > list_of_integers[mid + 1]:
        return list_of_integers[mid]

    if list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid + 1:])
    else:
        return find_peak(list_of_integers[:mid])
