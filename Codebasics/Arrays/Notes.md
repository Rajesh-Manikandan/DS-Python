# Arrays

There are two types of Array available in most of the progrmming languages.

- **Static Array** - Fixed number of nodes/ values
- **Dynamic Array** - Size grows dynamically based on the values gets added. 

Usually Array are stored in the linear positions in memory.


### Scenario 1: Array with 4 integers
Stock Prices = [298, 305, 320, 301]

Memory allocation will be 
| Memory | Value |
| ----------- | ----------- |
| 0x00500 | 298 |
| 0x00504 | 305 |
| 0x00508 | 320 |
| 0x0050A | 301 |

If memory address of stock_prices[0] is 0x00500
Then memory address of stock_prices[1] will be 0x00500 + (2 * sizeof(integer))

So, Lookup by index is O(1)

### Scenario 2: On What day price was 301?

```python
for i in range(len(stock_prices)):
    if stock_prices[i] == 301:
        return i
```

Lookup by value is O(n)

### Scenario 3: Print all Prices

```python
for price in stock_prices:
    print(price)
```

Array Traversal is O(n)


### Scenario 4: Insert new price 284 at index 1

```python
stock_prices.insert(1, 284)
```

Once the value gets inserted, the other values has to be shifted downwards in the memory

Due to the swaps, Array Insertion is O(n)


### Scenario 5: Delete an Element at Index 1

```python
stock_prices.pop(1)
```

Requires same swapping

Array Deletion is also O(n)


## Dynamic Arrays
Programming languages like JAVA, C++... supports for both static and dynamic arrays. Where as size of the array is fixed.

Will get ArrayOutOfBoundException error if tried to use index more than intitally specified.

```` java
//Static Array in JAVA
int[] stockPrices = new int[5];
// Dynamic Array in JAVA
ArrayList<Integer> stockPrices = new ArrayList<Integer>();
````

For Dynamic arrays, the initial capacity will be the size for 10 elements.

Once the new element is added after the size is reached. the new capacity of 20 memory space will be identified and all the first 10 elements will be copied to this new location and the new element will be added in the 11th position.

This is overhead comes with dynamic array.


The problem with python is it can store multiple data types in a array whereas other languages only support specific type of data in a array.

Python also supports for 2-dimesional and multi-dimensional arrays.

## Excercise
https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md