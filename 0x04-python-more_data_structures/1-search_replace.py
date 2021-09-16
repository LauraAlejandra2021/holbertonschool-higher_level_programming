#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    dicc= {search: replace}

    return([dicc.get(n, n) for n in new_list])