Create a function that takes a list of numbers and returns the sum of the two lowest positive numbers.
Examples
def sum_two_smallest_nums(lst):
	return sum(sorted([x for x in lst if x > 0])[:2])
