from unittest import TestCase
from Solver import Solver


class TestSolver(TestCase):
    test1_called = False
    test2_called = False
    test2_2_called = False

    def test_triangle_area(self):
        s = Solver()
        TestSolver.test1_called = True
        self.assertEqual(6, s.triangle_area(4, 3))

    def test_triangle_area2(self):
        s = Solver()
        TestSolver.test2_called = True
        self.assertEqual(7, s.triangle_area(4, 3))

    #######
    # NOTE: This redefines area2 and as such the first one will never be called
    #######
    def test_triangle_area2(self):
        s = Solver()
        TestSolver.test2_2_called = True
        self.assertEqual(6, s.triangle_area(4, 3))

    def test_triangle_area_ones(self):
        s = Solver()
        self.assertEqual(.5, s.triangle_area(1, 1))

    def test_triangle_area_zero(self):
        s = Solver()
        self.assertEqual(0, s.triangle_area(0, 10))

    @classmethod
    def tearDownClass(cls):
        tc = TestCase()
        tc.assertTrue(TestSolver.test1_called)
        tc.assertTrue(TestSolver.test2_2_called)

        # NOTE: test2 is never called as it is re-defined
        tc.assertFalse(TestSolver.test2_called)
