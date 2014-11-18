__author__ = 'Dark-Knight'

import copy


class Foo():
    notagoodidea = 'what am I now?'

object1 = Foo()
object1.notagoodidea = "who Knows"

object2 = object1
object2.notagoodidea = "Who's on first"
print('Class Variable :', Foo.notagoodidea,id(Foo.notagoodidea))
print('Instance variable 1 :', object1.notagoodidea)
print('Instance variable 2 :', object2.notagoodidea)
print('\n')


object3 = copy.copy(object1)
object3.notagoodidea = "I'm lost"
print('Instance variable 1 :', object1.notagoodidea, id(object1), id(object1.notagoodidea))
print('Instance variable 2 :', object2.notagoodidea, id(object2), id(object2.notagoodidea))
print('Instance variable 3 :', object3.notagoodidea, id(object3.notagoodidea))

# The value of objects can be interchanged, but they are still pointing to the same pieces of memory which makes them mutable.
