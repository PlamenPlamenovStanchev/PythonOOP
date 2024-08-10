from collections import Iterable


def read_next(*collections: Iterable):
    for collection in collections:
        for element in collection:
            yield element
            # yield from collection

