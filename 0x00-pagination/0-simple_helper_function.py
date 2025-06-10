#!/usr/bin/env python3
""" pagination """
from typing import Tuple


def index_range(page: int, page_size: int
                ) -> Tuple[int, int]:
    """ return start and end index for a page """

    start_index = page_size * (page - 1)

    end_index = start_index + page_size

    return (start_index, end_index)
