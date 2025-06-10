#!/usr/bin/env python3
""" pagination """
import csv
import math
from typing import Tuple, List, Dict


def index_range(page: int, page_size: int
                ) -> Tuple[int, int]:
    """ return start and end index for a page """

    start_index = page_size * (page - 1)

    end_index = start_index + page_size

    return (start_index, end_index)


class Server:
    """ server class to paginate baby names database """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ cached dataset """

        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [
                    row for row in reader
                ]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(
        self, page: int = 1, page_size: int = 10
    ) -> List[List]:
        """ return data for the page """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = (index_range(page, page_size))
        return self.dataset()[start: end]

    def get_hyper(
            self, page: int = 1, page_size: int = 10
    ) -> Dict:
        """ hypermedia pagination """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(
            len(self.__dataset) / page_size
        )
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
