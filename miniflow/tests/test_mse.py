import unittest
from hamcrest import *
import numpy as np

from miniflow import Input, MSE, topological_sort, forward_pass

class MSETest(unittest.TestCase):

    def test_mse(self):
        y, a = Input(), Input()
        cost = MSE(y, a)

        y_ = np.array([1, 2, 3])
        a_ = np.array([4.5, 5, 10])

        feed_dict = {y: y_, a: a_}
        graph = topological_sort(feed_dict)
        #forward pass
        forward_pass(graph)


        assert_that(cost.value, close_to(23.4166667, 0.0001))
