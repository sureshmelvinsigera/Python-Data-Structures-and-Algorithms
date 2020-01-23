## Author: Suresh Melvin Sigera

### What is Stack?
* A stack is a simple data structure used for storing data (similar to Linked Lists). In a stack, the order in which the data arrives is important.
* A stack is an ordered list in which insertion and deletion are done at one end, called top. The last element inserted is the first one to be deleted. Hence, it is called the Last in First out (LIFO) or First in Last out(FILO) list.

### Applications of Stack:
* Balancing of symbols
* lnfix-to-postfix conversion
* Evaluation of postfix expression
* Implementing function calls (including recursion)
* Page-visited history in a Web browser
* Undo sequence in a text editor
* Matching Tags in HTML and XML
* Used in many algorithms like Tower of Hanoi, tree traversals, stock span problem, histogram problem.

### Time Complexities:

* Push: O(1)
* Pop: O(1)
* Peek: O(1)
* isEmpty: O(1)
* Size: O(1)

### Limitations:

* Stack size is to be defined first and cannot be changed.
* Trying to push a new element into a full stack causes an implementation-specific exception.