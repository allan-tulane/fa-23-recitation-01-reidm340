"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###

def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1


def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
	"""
	Recursive implementation of binary search.

	Params:
	  mylist....list to search
	  key.......search key
	  left......left index into list to search
	  right.....right index into list to search

	Returns:
	  index of key in mylist, or -1 if not present.
	"""
	### TODO
	cur_index = (right + left)//2
	#print(cur_index)
	#print(mylist[left:right])
	if mylist[cur_index] == key:
		return cur_index
	if mylist[left:right] == []:
		return -1
	elif mylist[cur_index] > key:
		return _binary_search(mylist, key, left, cur_index)
	elif mylist[cur_index] < key:
		return _binary_search(mylist, key, cur_index + 1, right)
	###

def time_search(search_fn, mylist, key):
	"""
	Return the number of milliseconds to run this
	search function on this list.

	Note 1: `sort_fn` parameter is a function.
	Note 2: time.time() returns the current time in seconds. 
	You'll have to multiple by 1000 to get milliseconds.

	Params:
	  sort_fn.....the search function
	  mylist......the list to search
	  key.........the search key 

	Returns:
	  the number of milliseconds it takes to run this
	  search function on this input.
	"""
	### TODO
	start_time = time.time()
	search_fn(mylist, key)
	end_time = time.time()
	return (end_time - start_time) * 1000
	###

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
	"""
	Compare the running time of linear_search and binary_search
	for input sizes as given. The key for each search should be
	-1. The list to search for each size contains the numbers from 0 to n-1,
	sorted in ascending order. 

	You'll use the time_search function to time each call.

	Returns:
	  A list of tuples of the form
	  (n, linear_search_time, binary_search_time)
	  indicating the number of milliseconds it takes
	  for each method to run on each value of n
	"""
	### TODO
	tuple_list = []
	for n in sizes:
		n_list = []
		i = 1
		while i <= n:
			n_list.append(i)
			i += 1
		lin_time = time_search(linear_search, n_list, -1)
		bin_time = time_search(binary_search, n_list, -1)
		n_tuple = (n, lin_time, bin_time)
		tuple_list.append(n_tuple)
	return tuple_list

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'linear', 'binary'],
							floatfmt=".3f",
							tablefmt="github"))

print_results(compare_search())
