# OOP

self: a reference to the new object (can be called by other name)
dot: reference field name inside object.

def __str__(self)

when decide class, consider the content and what you can do(method) with that class or its behaviours.

good design: hidden details and can reuse directly. For example, card class should not have value field, as value is just used for blackjet game, it can be different for other game.

python does not support overloading

when initializing objects, if a list is used as param. use list() in __init__ to avoid ref. to the same list for two objects.

Uppercase capital for class name.

do not mistaking return and pass.