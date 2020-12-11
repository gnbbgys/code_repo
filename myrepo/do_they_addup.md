## Problem Description  

Given two arrays of integers, `A` and `B`, and a single integer value `v`, determine if it is possible to take exactly one element from each array (`a` from `A`, `b` from `B`), so that if we add them together, we get the given value (`a + b = v`).

Return true if it is possible to find a solution; false if it is not.
  
## Expected Completion Time 

Simple naive solution - 5 minutes; optimal solution 15-20 minutes.

## Problem Complexity Level

  Coding Fluency: Easy
  
  Problem Solving: Medium
  
## Questions the candidate might ask

* Can any of the values be negative? -> Yes
* Do I need to care about integer overflows? -> Good question but no.
* Can I pick the same value from `A` and from `B`? -> Yes
* Can there be multiple pairs of values that add up to `v`? -> Yes, we only care if there exists any solution or not.
* Can the arrays have different lengths? -> Yes
* Are the arrays sorted? -> Generally no
  
## Sample inputs - Expected outputs

```
v = 10
A = [1,2,3]
B = [8,6,12]
result -> true (2 + 8 == 10)
```

```
v = 10
A = [1,3,5]
B = [5,7,8]
result -> true (either 5+5 or 7+3)
```

```
v = 10
A = [-2,5,8,4]
B = [11,-6]
result -> false
```
  
## Input corner cases

Either one or even both of the arrays can be empty. Then the result is `false`.
  
## Solution

Assuming length of `A` is `m` and length of `B` is `n`.

### Simple, quadratic

Two nested for loops, checking every pair of values from `A` and from `B`.

```c++
bool doTheyAddUp (std::vector<int> const& A, std::vector<int> const& B, int const v)
{
  for (auto const a: A) {
    for (auto const b: B) {
      if (a + b == v) {
        return true;
      }
    }
  }
  return false;
}
```

* time: O(n * m) which can be equivalent to O(n * n)
* memory: O(1)

### Balanced tree set - logarithmic

Iterate over one array and make a tree structure (`std::set`) of remainders. Iterate over the second array and as soon as the value is in the map, return `true`.

```c++
bool doTheyAddUp (std::vector<int> const& A, std::vector<int> const& B, int const v)
{
  std::set<int> remainders;
  for (auto const a: A) {
    remainders.insert(v - a);
  }
  for (auto const b: B) {
    if (remainders.find(b) != remainders.end()) {
      return true;
    }
  }
  return false;
}
```

* time: O(m * log(n)) which can be equivalent to O(n * log(n)) 
* memory: O(n)

### Hash set - linear

Same as above but use `std::unordered_set` instead of `std::set`.

* time: O(n) (considering m & n to ne of similar order)
* memory: O(n)

### Sorting the arrays - logarithmic

Sort both arrays and do some sort of binary search over both arrays. More complex code and worse performance than the above two solutions.

### Data structures

* Balanced tree set
* Hash set
      
## Test Driver

```c++
assert( doTheyAddUp( {1,2,3}, {8,6,12}, 10 ) == true );
assert( doTheyAddUp( {1,3,5}, {5,7,6}, 10 ) == true );
assert( doTheyAddUp( {-2,5,8,4}, {11,-6}, 10 ) == false );
```
  
## Follow up questions

1. Does it matter over which array do we iterate first?
   * If the candidate used a tree-set structure; not hashmap: Yes - for the worst case complexity (big O) - we first want to go over the **longer** of the two arrays and construct the set from it. If `m` < `n` then `m * log(n)` is better than `n * log(m)`.
   * If the candidate used a hashmap: No, it doesn't matter.
1. (potentially tricky) What if we guarantee that the values in both arrays are non-negative and the target value `v` is a compile time constant?
   * Asymptotic complexity will be the same, O(n + m), but we could use a fixed sized array instead of hashmap.
1. (potentially tricky) Would there be some general issue if we wanted to extend the problem to floating point numbers instead of integers?
   * Yes - some floating point numbers are not represented exactly, and we cannot check that `a + b == v`; we would need to check that `a + b - v` is less than some tolerance `epsilon` .
