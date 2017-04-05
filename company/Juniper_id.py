import unittest


class IDManager():
    def __init__(self, n):
        """
        :param pool: integer to create pool from 1 to n
        :return: IDManager for managing pool of ids
        """
        if not isinstance(n, int):
            raise Exception('N must be an int, got type {}'.format(type(n)))
        self.id_dict = {i: True for i in range(1, n + 1)}
        self.stack = [i for i in range(1, n + 1)]

    def get_id(self):
        """
        :return: a freed integer id
        """
        if not self.stack:
            raise Exception('All ids are currently in use, use free_id to free ids')
        return_id = self.stack.pop()
        self.id_dict[return_id] = False
        return return_id

    def free_id(self, id):
        """
        :param id: integer id to be freed
        """
        if id not in self.id_dict:
            raise Exception('id {} is not a valid id'.format(id))
        if self.id_dict[id]:
            raise Exception('id {} is already free'.format(id))
        self.id_dict[id] = True
        self.stack.append(id)


class TestIDManager(unittest.TestCase):
    def setUp(self):
        self.manager = IDManager(100)

    def test_free_id(self):
        """
        test that IDManager.free_id(id) puts the id back on the stack and marks the id as free in id_dict
        """
        mid = self.manager.get_id()
        length = len(self.manager.stack)
        self.manager.free_id(mid)
        assert len(self.manager.stack) == length + 1
        assert self.manager.id_dict[mid]

    def test_get_id(self):
        """
        test that IDManager.get_id() returns an id that is an integer and marks the id as in use in id_dict
        and removes it from the stack
        """
        previous_length = len(self.manager.stack)
        mid = self.manager.get_id()
        self.assertIsInstance(mid, int)
        assert not self.manager.id_dict[mid]
        assert len(self.manager.stack) == previous_length - 1

    def test_wrong_value(self):
        """
        tests that an exception is thrown if IDManager() is created with a non integer value
        """
        self.assertRaises(Exception, lambda: IDManager('string'))

    def test_free_free_id(self):
        """
        tests that an exception is thrown if an id is freed that is already free
        """
        fid = self.manager.get_id()
        self.manager.free_id(fid)
        self.assertRaises(Exception, lambda: self.manager.free_id(fid))

    def test_no_ids(self):
        """
        tests to make sure an exception is thrown if get_id() is called with no free ids
        """
        for i in range(100):
            self.manager.get_id()
        self.assertRaises(Exception, lambda: self.manager.get_id())

    def test_bad_id(self):
        """
        tests to make sure an exception is thrown if get_id() is called with an invalid id
        """
        self.assertRaises(Exception, lambda: self.manager.free_id(10001))