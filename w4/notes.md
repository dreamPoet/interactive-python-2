List: ordered sequence
Dictionary: key value mapping
Set: unordered collection of data with no duplicates


a_set = set([])
a_set = set()

the input order is not the exact stored order

a_set.add()
a_set.remove()
a_set.difference_update(removed_elem_set)

for item in a_set

print "special_item" in a_set #True/False


another way to avoid removing elements when looping it:
1. create a remove_list and add elem to it and finally remove elem. in this list
2. for s in list(original_list): original_list.remove(s): loop in the copy of the list and remove in the original list. For set, it should be set(original_set) to get a copy


python 2.7/3.0 support using {} to define set.


a_set.intersection(b_set) return intersection part
a_set.intersection_update(b_set) return s as intersection part
contains update equals update the a_set

b_set in fact can be list, dict, etc, str.