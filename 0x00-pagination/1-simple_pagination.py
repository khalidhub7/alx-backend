#!/usr/bin/env python3
""" pagination """
import csv
from typing import List


def index_range(
        page: int, page_size: int):
    """ start and end index """
    start = page_size * (page - 1)
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate
a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ initializing ... """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [
                    row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(
        self, page: int = 1,
        page_size: int = 10
    ) -> List[List]:
        """ get page """
        assert isinstance(
            page, int) and page > 0
        assert isinstance(
            page_size, int) and page_size > 0

        page_len = index_range(
            page, page_size)
        data = self.dataset()
        if page_len[0] >= len(data):
            return []
        return data[
            page_len[0]:min(page_len[1],
                            len(data))]
