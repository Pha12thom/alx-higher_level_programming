#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for search in my_list:
        search, replace = replace, search
    return (my_list[search], my_list[replace])
