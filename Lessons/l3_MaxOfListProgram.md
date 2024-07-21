# The Maximum of a List Program

We are now going to recycle our ``maximum()`` function.
```python
def maximum(x, y):
    if x > y:
        return x
    else:
        return y
```

## 1. Planning the Program

Here is an outline of the program in pseudocode.

```
Given a list 
Store the first value of the list as current_max
for each element x in the list (not including the first)
    current_max = max(current_max, x)

print out current_max as the result
        
```

## 2. Program - Maximum of a list

Let's now implement this and use our ``maximum()`` function in a program to loop through a list of numbers and print out the maximum.

```python
def maximum(x, y):
    if x > y:
        return x
    else:
        return y

if __name__ == "__main__":
    num_list = [3,6,2,1,8,4,4,2,7]
    
    # set the current max to the first element in the list
    current_max = num_list[0]
    
    # loop through the list (start at the second element)
    for x in num_list[1:]:
        # store result of current_max and x
        current_max = maximum(current_max, x)
    
    print(f"Maximum number is {current_max}")
```

Hopefully, you can see that we didn't really care how ``maximum()`` worked, we just knew that ``maximum()`` takes in an ``x`` and ``y`` and returns the larger.

## 3. Program - Maximum of a list (Function)

I now want to take this opportunity to rewrite this. Let's create a function that can take in a list of numbers and outputs the maximum.

```python
def maximum(x, y):
    if x > y:
        return x
    else:
        return y

def max_list(num_list):
    current_max = num_list[0]
    for x in num_list[1:]:
        current_max = maximum(current_max, x)
    return current_max

if __name__ == "__main__":
    list_one = [3,6,2,1,8,4,4,2,7]
    list_two = [30,16,4,45,27,84]
    list_three = [-10,-4,-3,-2]
    
    print(f"Maximum of list 1 is {max_list(list_one)}")
    print(f"Maximum of list 2 is {max_list(list_two)}")
    print(f"Maximum of list 3 is {max_list(list_three)}")
```

Congratulations, you have just written a function ``max_list()`` that takes in a ``list`` of numbers and returns the maximum. 

This is a reusable function that we don't really care how it works, we just know it works! This is the essence of what we call **decomposition** and **abstraction** which we will look at in unit 7.

Interestingly Python provides such a function for us. Try typing this into the Python Interactive Shell.

```python
max([5,2,4,7])
```

Again let me stress, ``max()`` is a built-in function that we do not know how it works. We just know it takes ``list`` and returns the maximum.

You can type the following into the Python Interactive Shell to get help information about the ``max()`` function.

```python
help(max)
```
  
You can pass the tests by copying and pasting the program in Section 3 into **main.py**.