#!/usr/bin/env python3
"""
simple helper funcion
"""


def index_range(page, page_size):
    """
    return a tuple of size two containing a start index and an end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
