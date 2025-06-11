#!/usr/bin/env python3
""" deletion-resilient hypermedia pagination """

import csv
import math
from typing import List, Dict


class Server:
    """ server class to paginate baby names database """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """ cached dataset """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """ dataset indexed by sorted position, starting at 0 """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(
        self, index: int = None, page_size: int = 10
    ) -> Dict:
        """  """
        if index is None:
            index = 0
        assert 0 <= index < len(self.__indexed_dataset)

        data = []

        while len(data) < page_size:
            try:
                row = self.__indexed_dataset[index]
            except Exception:
                row = None
            data.append(row)
            index += 1

        return {
            'index': index - page_size,
            'next_index': index,
            'page_size': page_size,
            'data': list(filter(None, data))
        }
