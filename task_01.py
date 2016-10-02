#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for task_01."""


def get_party_stats(families, table_size=6):
    """This function determines the total number of guests and tables needed.

    Args:
        families(list): List of families that are list of members.
        table_size(int, optional): Maximum number of seats at each table.
        Default: Six

    Returns:
        tuple: Total number of guests and Total number of tables.

    Examples:

        >>> get_party_stats([['Jan'],['Jen', 'Jess']])
        (3, 2)

    """
    guests = 0
    tables = 0
    for list_item in families:
        guests = guests + len(list_item)
        tables = tables + (-(-(len(list_item))//table_size))

    return (guests, tables)
