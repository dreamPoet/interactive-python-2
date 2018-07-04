list(tuple) can also get a copy of tuple.
str[-1] can be the last elem of string; str[-2], the second last lem.
str[-1] = str[len(str)-1]
len(str) (no \0 etc, just the number of elem of the str)
str[0:3] from 0 up to 3 but not include 3.
str[:3] from beginning
str[2:] to end



list = [1, 2, 3]

3 in list == True;
4 in list == False;
list.index(2) == 1

append, pop
list.append(632)
last_item = list.pop().
list.pop(4) can remove the elem. in index 4.
list.remove(1); remove element 1.


instead of delete elements you want delete in the original list, create a new remove list and appending things you want to move to it.


cannot change the list when you iterate it. error may happen like skip some elements/ deal with some elements twice etc.

remember after pop(), index changes. sometimes create a new list will be better.

## Dictionary

mapping: key -> values

dict.items()

**mapping the computation**:


def square(numbers):
    return [n**2 for n in numbers]


list.append(list) use same reference, do not copy a list., filtering, based on original list.


def ballInRange(balls):
    returen [ball for ball in balls if is_in_range(ball)]


there is no last elements in dict; we cannot slice dict; when print dict, the order may not be what we expect. we can emutate list and dist.

dict can map tuple to other value, but cannot map list or dict, as they are emutable(can be changed)

empty dict:
dict()
{}