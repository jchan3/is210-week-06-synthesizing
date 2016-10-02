#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for task_02."""


def prepare_email(appointments):
    """This function creates a new list with just the clients email body.

    Args:
        appointments(list): A list of two-item tuples with names and appointment
        time.

    Returns:
        list: List with the client's email body.

    Examples:

        >>> prepare_email([('Jen','2015'),('Max','March 3')])
        ['Dear Jen,\nI look forward to meeting with you on 2015.\nBest,\nMe',
        'Dear Max,\nI look forward to meeting with you on March 3.\nBest,\nMe']

    """
    email = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'
    new_list = []
    for list_item in appointments:
        name = list_item[0]
        date = list_item[1]
        new_list.append(email.format(name, date))

    return new_list
