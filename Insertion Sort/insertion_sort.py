from typing import List
import logging

logger = logging.getLogger("Insertion Sort")
logging.basicConfig(
    format="%(asctime)s %(message)s", datefmt="%Y-%M-%d %I:%M:%S-%p", level=1
)

# Worst case scenario: ALl the items are in descendind order
# in which case all the
# items need to be looked at and moved until i-1


def insertion_sort(iterable: List):

    for i in range(1, len(iterable)):

        # This is the current key
        key = iterable[i]

        # This is the previous key
        j = i - 1

        while j > 0 and key < iterable[j]:

            iterable[j + 1] = iterable[j]
            # Decrease the j index by one to see
            # compare with the left side
            j -= 1

        # Keep going until the left side is not longer smaller

        # If the right side is not smaller than the left hand side then assign the the left side the key
        iterable[j + 1] = key


logger.info("Operation Started")
iterable = [1, 2, 12, 4, 5]
logger.info(f"Before Sort {iterable}")
insertion_sort(iterable)
logger.info(f"After Sort {iterable}")
logger.info("Operation End")
