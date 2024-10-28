#!/usr/bin/env python3
""" pagination """


def index_range(
        page: int, page_size: int):
    """ start and end index """
    start = page_size * (page - 1)
    end = start + page_size
    return (start, end)
