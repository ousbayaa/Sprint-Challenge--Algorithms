#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
``` 
It is O(n) because as the size of the input is bigger, the time it takes grows linearly

```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```
It is a O(n^2) because the space grows exponentialy. For each addition in the outer loop, the inner loop must iterate through the whole thing.

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
It is O(n) because for each increase in bunnies, there is only 1 additional operation ran, therefore it is linear.

## Exercise II

We can use binary search. We start out by going to n/2 floors and seeing if the egg breaks, if it does, we then move on to n=n/2 and run the test again until we reach the point where we cant divide anymore.

The complexity of this is O(log n)