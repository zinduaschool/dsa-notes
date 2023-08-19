# Linked Lists
A **[linked List]()** is used to represent sequential data. It is a data structure where each element is a separate object, called a [node](#node), that stores a reference  ([pointer](#pointer))to the next node in the list.<br>The node represented by value and a pointer commonly referred to as next. In js, linked lists can be implemented using objects and arrays.

<hr>

<img src="../../assets/Linked-List-Data-Structure.png" alt="Linked List example image"/>

## Types of Linked Lists
1. **Singly Linked List** : <br>Each node in the list contains a reference or a pointer to the the next node in the list. <br>The last node in the list (tail) contains a reference to null, indicating the end of the list. <br>The main disadvantage of this, is that you can only traverse the list in one direction, from the first node(head) to the last node(tail)
2. **Doubly Linked List** : <br> A doubly linked list is similar to a singly linked list, but in a ddition to a next reference(pointer), each node also has a prev pointer, which points to the previous node. <br>This allows for easier traversal in both directions and can be useful in certain types of algorithms 
3. **Circular Linked Lists** : <br> This is a variation of a singly linked list where the last node points back to the first node(head), forming a circular loop. <br>The main advantage of a circular linked list is that it allows for efficient implementation of certain algorithms such as traversing through a loop

<hr>

### Time Complexity

| Access | Lookup | Insert(at) | Deletion |
|:------:|:------:|:----------:|:--------:|
|  O(n)  |  O(n)  |    O(1)    |   O(n)   |


Access time is linear (and difficult to pipeline). Faster access, such as random access, is not feasible. Arrays have better cache locality as compared to linked lists.

<hr>

### **Basic Operations**
1. **Traverse** : 

    ```jsx
    function traverse_list(head)
    //first node of the linked list
      current = head
      //loop to iterate through the list as long as "current" is not null
      while current != null
        //print the stored in the current node using "current.data"
        print current.data
        //move current pointer to the next node by assigning "current.next" to current and the loop continues
        current = current.next
    end function
    ```

2. **Prepend** : <br> will add new node at the start of the list and the head of the list will now point to the new node.

    ```jsx
    function Prepend(head, data)
    //create node and pass data parameter
      new_node = create_node(data)
      //set "next" pointer of the new node to point to the current head
      new_node.next = head
        //update head of the list to be the new node
        head = new_node
        //move current pointer to the next node by assigning "current.next" to current and the loop continues
    end function
    ```

3. **Append** : <br> will add the new node at the end of the list, and the last node's next pointer will point to the new node

    ```jsx
    function append(head, data)
    //create new node
        newNode = create_node(data)
        //init var current and initialize it to equal to head
        current = head
        //check if the head of the list is null, 
        if (current = null)
            //set head to equal new node
            head = newNode
        else 
           //if head does not equal to null, loop to iterate till the last node(tail)
            while current.next != null
                current = current.next
                //set next pointer of the last node to point to the new node(adding the new node to the end)
            current.next = newNode
        end if
      end function
    ```
<hr>

## Constraints
  * Empty linked list (head is null)
  * Single node
  * Two nodes
  * Linked list has cycles.

<br>

![](https://img.shields.io/static/v1?label=&message=💡Tip:&color=orange): Clarify beforehand with the interviewer whether there can be a cycle in the list. Usually the answer is no and you don't have to handle it in the code

To see how a linked list is implemented see [here]()

<hr>

## Related Questions
| No | Problem Statement                                                         |
|----|---------------------------------------------------------------------------|
| 1. | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) |
|    |                                                                           |

<hr>

## References

# Articles

1.  [Medium](https://medium.com/basecs/whats-a-linked-list-anyway-part-1-d8b7e6508b9d)

# Videos

2.  [Coursera](https://www.coursera.org/lecture/data-structures/singly-linked-lists-kHhgK)
