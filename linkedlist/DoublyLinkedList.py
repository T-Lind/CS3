from typing import Any

from Item import Item


class NoneTypeException(Exception):
    """
    Create an exception type for referring to a None value when you shouldn't be
    """
    pass


class DoublyLinkedList:
    """
    A class to represent a doubly-linked list, so you can traverse it forwards as well as back
    """

    def __init__(self, value=None):
        """
        Create a linkedlist object which has elements which store a pointer to the previous and next object.
        The default of all of these values is None, which can throw errors
        """
        self.top = Item(value=value, prev_pointer=None, next_pointer=None)

    def push(self, value) -> None:
        """
        Push a value to the end of the list
        :param value: The value to push
        """
        if self.top.value is None and self.top.prev_pointer is None and self.top.next_pointer is None:
            self.top.value = value
            return

        new_item = Item(value=value, prev_pointer=self.top, next_pointer=None)

        self.__check_none_exception(self.top)

        self.top.next_pointer = new_item
        self.top = new_item

    def push_front(self, value) -> None:
        """
        Push a value to the front ot the list
        :param value: the value to push
        """
        if self.top.value is None and self.top.prev_pointer is None and self.top.next_pointer is None:
            self.top.value = value
            return

        insert_item = Item(value=value, prev_pointer=None, next_pointer=None)
        first_item = self.get_first_item()

        self.__check_none_exception(first_item)

        insert_item.next_pointer = first_item
        first_item.prev_pointer = insert_item

        # return first_item.value

    def pop(self) -> Any:
        """
        Pop an element from the END of the list
        :return: The popped item's value
        """
        popped_item = self.top

        self.__check_none_exception(popped_item)

        if self.top.prev_pointer is not None:
            self.top = self.top.prev_pointer
            return popped_item.value

    def pop_front(self) -> Any:
        """
        Pop an element from the FRONT of the list
        :return: The popped item's value
        """
        first_item = self.get_first_item()

        self.__check_none_exception(first_item)

        first_item.next_pointer.prev_pointer = None
        return first_item.value

    def peek(self) -> Any:
        """
        Look at the last element's value but don't remove it
        :return: The last element's value
        """

        self.__check_none_exception(self.top)

        return self.top.value

    def peek_front(self) -> Any:
        """
        Look at the front element's value but don't remove it
        :return: The front element's value
        """
        first_item = self.get_first_item()

        self.__check_none_exception(first_item)

        return first_item.value

    def get_front(self, index) -> Any:
        """
        A function to get the index pushed, from the front: NOTE: computation is O(nmp) as it must go back through the
        list to the front as well as check for an index exception
        :param index:
        :return:
        """
        self.check_index_exception(index)

        get_item = self.get_first_item()

        for i in range(index):
            get_item = get_item.next_pointer

        self.__check_none_exception(get_item)

        return get_item.value

    def get(self, index) -> Any:
        """
        Return an item's VALUE at the given index.
        :param index: The item to return
        :return: the value at the given location
        """
        self.check_index_exception(index)

        get_item = self.top

        for i in range(index):
            get_item = get_item.prev_pointer

        self.__check_none_exception(get_item)

        return get_item.value

    def get_object(self, index):
        """
        Return the object in the linked list at the certain index
        :param index: The index of the object to retreive
        :return: The object at the given index
        """
        self.check_index_exception(index)

        get_item = self.top

        for i in range(index):
            get_item = get_item.prev_pointer

        self.__check_none_exception(get_item)

        return get_item

    def remove(self, index) -> None:
        """
        Take out an index and patch the list
        :param index: The index to remove
        """
        self.check_index_exception(index)

        get_item = self.get_object(index)

        prev_item = get_item.prev_pointer
        next_item = get_item.next_pointer

        if prev_item is None:
            next_item.prev_pointer = None
            get_item.next_pointer = None
            get_item.prev_pointer = None
            return

        if next_item is None:
            prev_item.next_pointer = None
            get_item.next_pointer = None
            get_item.prev_pointer = None
            return

        prev_item.next_pointer = next_item.prev_pointer
        next_item.prev_pointer = prev_item.next_pointer

    def get_first_item(self) -> Any:
        """
        Get the first item in the list
        :return: the top item
        """
        first_item = self.top

        self.__check_none_exception(first_item)

        while first_item.prev_pointer is not None:
            first_item = first_item.prev_pointer
        return first_item

    def __check_none_exception(self, item):
        """
        Perform basic check to make sure the list is functioning properly
        :param item: The item to check
        """
        if item.value is None and item.prev_pointer is None and item.next_pointer is None:
            raise NoneTypeException("Cannot acces a none type item!")

    def check_index_exception(self, index):
        """
        Determine if an index exists
        :param index: The index to check
        """
        if index >= len(self) or index < 0:
            raise IndexError(f"Incorrectly accessing index {index} in {__name__}")

    def __len__(self):
        count = 1
        first_item = self.top

        # Return 0 if nothing is in the List
        if first_item.value is None and first_item.prev_pointer is None and first_item.next_pointer is None:
            return 0

        while first_item.prev_pointer is not None:
            first_item = first_item.prev_pointer
            count += 1
        return count
