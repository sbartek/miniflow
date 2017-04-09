from hamcrest import *
import unittest
import numpy as np


from miniflow import Input, Add, Mul, Linear, Sigmoid\
     , topological_sort, forward_pass

class AddTest(unittest.TestCase):

    def test_add_two(self):

        x, y = Input(), Input()

        f = Add(x, y)

        feed_dict = {x: 10, y: 5}

        sorted_nodes = topological_sort(feed_dict)
        forward_pass(sorted_nodes)
        output = f.value

        # NOTE: because topological_sort set the values for the `Input` nodes we could also access
        # the value for x with x.value (same goes for y).
        assert_that(output, equal_to(15))

    def test_add_three(self):

        x, y, z = Input(), Input(), Input()

        f = Add(x, y, z)

        feed_dict = {x: 4, y: 5, z: 10}

        graph = topological_sort(feed_dict)
        forward_pass(graph)
        output = f.value

        # should output 19
        assert_that(output, equal_to(19))

    def test_mul_four(self):

        w, x, y, z = Input(), Input(), Input(), Input()

        f = Mul(w, x, y, z)

        feed_dict = {w: 2, x: 4, y: 5, z: 10}

        graph = topological_sort(feed_dict)
        forward_pass(graph)
        output = f.value
        # should output 400
        assert_that(output, equal_to(400))

    def test_linear(self):
        """
        NOTE: Here we're using an Input node for more than a scalar.
        In the case of weights and inputs the value of the Input node is
        actually a python list!

        In general, there's no restriction on the values that can be passed to an Input node.
        """


        inputs, weights, bias = Input(), Input(), Input()

        f = Linear(inputs, weights, bias)

        feed_dict = {
            inputs: np.array([6, 14, 3]),
            weights: np.array([0.5, 0.25, 1.4]),
            bias: 2
        }

        graph = topological_sort(feed_dict)
        forward_pass(graph)
        output = f.value

        # should be 12.7 with this example
        assert_that(output, equal_to(12.7))


    def test_multilinear(self):
        X, W, b = Input(), Input(), Input()

        f = Linear(X, W, b)

        X_ = np.array([[-1., -2.], [-1, -2]])
        W_ = np.array([[2., -3], [2., -3]])
        b_ = np.array([-3., -5])

        feed_dict = {X: X_, W: W_, b: b_}

        graph = topological_sort(feed_dict)
        forward_pass(graph)
        output = f. value

        out = np.array([[-9., 4.], [-9., 4.]])
        ##assert_that(output, equal_to(out))
        assert_that(output[1, 1], equal_to(out[1, 1]))
        assert_that(output[1, 0], equal_to(out[1, 0]))

    def test_sigmoid(self):

        X, W, b = Input(), Input(), Input()

        f = Linear(X, W, b)
        g = Sigmoid(f)

        X_ = np.array([[-1., -2.], [-1, -2]])
        W_ = np.array([[2., -3], [2., -3]])
        b_ = np.array([-3., -5])

        feed_dict = {X: X_, W: W_, b: b_}

        graph = topological_sort(feed_dict)
        forward_pass(graph)
        output = g.value

        out = np.array(
            [[  1.23394576e-04,   9.82013790e-01],
             [  1.23394576e-04,   9.82013790e-01]])
        assert_that(output[1,1], close_to(out[1,1], 0.00001))
        assert_that(output[0,0], close_to(out[0,0], 0.00001))

    
