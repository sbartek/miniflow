from hamcrest import *
import unittest

from miniflow import Input, Add, Mul, topological_sort, forward_pass

class AddTest(unittest.TestCase):

    def test_add_two(self):

        x, y = Input(), Input()

        f = Add(x, y)

        feed_dict = {x: 10, y: 5}

        sorted_nodes = topological_sort(feed_dict)
        output = forward_pass(f, sorted_nodes)

        # NOTE: because topological_sort set the values for the `Input` nodes we could also access
        # the value for x with x.value (same goes for y).
        assert_that(output, equal_to(15))

    def test_add_three(self):

        x, y, z = Input(), Input(), Input()

        f = Add(x, y, z)

        feed_dict = {x: 4, y: 5, z: 10}

        graph = topological_sort(feed_dict)
        output = forward_pass(f, graph)

        # should output 19
        assert_that(output, equal_to(19))

    def test_mul_four(self):

        w, x, y, z = Input(), Input(), Input(), Input()

        f = Mul(w, x, y, z)

        feed_dict = {w: 2, x: 4, y: 5, z: 10}

        graph = topological_sort(feed_dict)
        output = forward_pass(f, graph)

        # should output 400
        assert_that(output, equal_to(400))


    
