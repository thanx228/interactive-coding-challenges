from random import randint
import unittest


class TestSortStack(unittest.TestCase):

    def get_sorted_stack(self, stack, numbers):
        for x in numbers:
            stack.push(x)
        return stack.sort()

    def test_sort_stack(self, stack):
        print('Test: Empty stack')
        sorted_stack = self.get_sorted_stack(stack, [])
        self.assertEqual(sorted_stack.pop(), None)

        print('Test: One element stack')
        sorted_stack = self.get_sorted_stack(stack, [1])
        self.assertEqual(sorted_stack.pop(), 1)

        print('Test: Two or more element stack (general case)')
        num_items = 10
        numbers = [randint(0, 10) for _ in range(num_items)]
        sorted_stack = self.get_sorted_stack(stack, numbers)
        sorted_numbers = [sorted_stack.pop() for _ in range(num_items)]
        self.assertEqual(sorted_numbers, sorted(numbers, reverse=True))

        print('Success: test_sort_stack')


def main():
    test = TestSortStack()
    test.test_sort_stack(MyStack())
    test.test_sort_stack(MyStackSimplified())


if __name__ == '__main__':
    main()
