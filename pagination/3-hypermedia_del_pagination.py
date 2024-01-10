#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ get hypermedia index of dataset based on index and page_size args

        Args:
            index (int, optional): index of dataset to start page.
            Defaults to None.
            page_size (int, optional): number of items per page.
            Defaults to 10.

        Returns:
            Dict: dictionary of dataset items with key-value pairs of:
            index: current start index of the return page
            next_index: index of next dataset item
            page_size: number of items per page
            data: actual page of dataset
        """
        # check if index and page_size are valid integers > 0
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        # get indexed dataset
        indexed_dataset = self.indexed_dataset()
        # get dataset keys
        dataset_keys = list(indexed_dataset.keys())
        # get dataset length
        dataset_size = len(dataset_keys)

        # Adjust the index if it is out of the range
        if index >= dataset_size:
            return {
                "index": None,
                "next_index": None,
                "page_size": page_size,
                "data": []
            }

        # get start and end index for pagination using index_range
        start_index = dataset_keys.index(index) if index in dataset_keys else 0

        # get next index using start_index and page_size
        next_index = start_index + page_size

        # next_index should be less than dataset_size
        # to avoid index out of range error
        # if True, set next_index to dataset_size
        # to get the next page of dataset or None
        next_index_value = (dataset_keys[next_index]
                            if next_index < dataset_size else None)

        # get data for the current page
        # Get the data for the current page
        current_page_data = [
            indexed_dataset[dataset_keys[i]]
            for i in range(start_index, min(next_index, dataset_size))
        ]

        # return hypermedia index
        return {
            'index': index,
            'data': current_page_data,
            'page_size': page_size,
            'next_index': next_index_value
        }
# end hypermedia index function
