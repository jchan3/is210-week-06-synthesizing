#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for task_01."""


def get_party_stats(families, table_size=6):
    """This function determines the total number of guest and tables needed.

    Args:
        families(list): List of families that are list of members.
        table_size(int, optional): Maximum number of seats at each table. Default: Six

    Returns:
        tuple: Total number of guests and Total number of tables.

    Examples:

        >>> get_party_stats([['Jan'],['Jen', 'Jess']])
        (3, 2)

    """
    guests = 0
    tables = 0
    members = 0
    for list_item in families:
        for x in list_item:
            guests += 1
            members += 1
            if members > table_size:
                tables += 1
                members = 1
        tables += 1
        members = 0
        
    return (guests, tables)
