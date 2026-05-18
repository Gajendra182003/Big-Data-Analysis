# =============================================================================
#         NumPy Arrays - Day 01 | Advanced Analytics Using Statistics
#         Full Code with Line-by-Line Comments
# =============================================================================

import numpy as np      # Import NumPy library and alias it as 'np'
import pandas as pd     # Import Pandas library and alias it as 'pd' (used later)


# =============================================================================
# SECTION 1: Creating Arrays from Lists
# =============================================================================

# Create a plain Python list with 9 elements
x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(x1)               # Prints: [1, 2, 3, 4, 5, 6, 7, 8, 9]
type(x1)                # Returns: list  — confirms x1 is a Python list

# Convert the Python list to a NumPy 1D array (ndarray)
a1 = np.array(x1)
print(a1)               # Prints: [1 2 3 4 5 6 7 8 9]  (no commas — NumPy format)
type(a1)                # Returns: numpy.ndarray

# ❌ ERROR EXAMPLE — 'array' alone is not defined; must use 'np.array'
# a1 = array(x1)        → NameError: name 'array' is not defined


# =============================================================================
# SECTION 2: Creating 2D Arrays (Matrix)
# =============================================================================

x2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]       # Another list (same length as x1 = 9 items)

# Stack x1 and x2 as rows → creates a 2×9 matrix
a2 = np.array([x1, x2])
# Output:
# array([[1, 2, 3, 4, 5, 6, 7, 8, 9],
#        [9, 8, 7, 6, 5, 4, 3, 2, 1]])

x3 = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]    # List with 10 elements (different length!)

# ❌ ERROR: x1 has 9 elements, x3 has 10 → rows must be equal length for a 2D array
# a3 = np.array([x1, x2, x3])           → ValueError: inhomogeneous shape

# ❌ ERROR: x2 has 9, x3 has 10 — same issue
# a3 = np.array([x2, x3])               → ValueError: inhomogeneous shape


# =============================================================================
# SECTION 3: np.arange() — Range-Based Array Creation
# =============================================================================

# np.arange(stop): creates array from 0 up to (not including) stop
a1 = np.arange(11)          # array([ 0,  1,  2, ..., 10])

# np.arange(start, stop): from 3 up to (not including) 14
a2 = np.arange(3, 14)       # array([ 3,  4,  5, ..., 13])

# np.arange(start, stop, step): every 2nd number from 5 to 19
arr1 = np.arange(5, 20, 2)  # array([ 5,  7,  9, 11, 13, 15, 17, 19])

# np.arange with negative step: counts DOWN from 24 to 7 (step -2)
arr2 = np.arange(24, 5, -2) # array([24, 22, 20, 18, 16, 14, 12, 10,  8,  6])

# Even numbers from 2 to 24
arr3 = np.arange(2, 26, 2)  # array([ 2,  4,  6,  8, ..., 24])


# =============================================================================
# SECTION 4: np.linspace() — Evenly Spaced Numbers
# =============================================================================

# np.linspace(start, stop, num): num evenly spaced points INCLUSIVE of both ends
ls1 = np.linspace(10, 30, 7)
# array([10.  , 13.33, 16.67, 20.  , 23.33, 26.67, 30.  ])

# Without endpoint (endpoint=False): 7 points NOT including stop value
ls2 = np.linspace(10, 30, 7, endpoint=False)
# array([10.  , 12.86, 15.71, 18.57, 21.43, 24.29, 27.14])


# =============================================================================
# SECTION 5: Append & Concatenate
# =============================================================================

a1 = np.arange(11)           # array([ 0,  1, ..., 10])

# np.append(arr, value): adds 11 at the END — returns a NEW array (not in-place)
a1 = np.append(a1, 11)       # array([ 0,  1, ..., 10, 11])

# np.append(arr1, arr2): joins two arrays end-to-end (flattened)
apnd1 = np.append(a1, a2)   # combines a1 and a2 into one long 1D array

# np.concatenate((arr1, arr2)): same as append for 1D; works with axis for 2D
con1 = np.concatenate((a1, a2))

# ❌ ERROR: NumPy arrays don't have a .remove() method (that's for Python lists)
# a1.remove(4)               → AttributeError


# =============================================================================
# SECTION 6: Insert & Delete
# =============================================================================

c1 = np.array([3, 6, 5, 7, 8])

# ❌ ERROR: Typo — 'aaray' doesn't exist in numpy
# c1 = np.aaray([3,6,5,7,8]) → AttributeError

# ❌ ERROR: np.array() only accepts 1–2 positional args, not 3
# c2 = np.array(a1, 3, 9)    → TypeError

# np.insert(arr, index, value): inserts 9 at position index=3
c2 = np.insert(c1, 3, 9)    # array([3, 6, 5, 9, 7, 8])

# np.delete(arr, index): removes element at index 2 — returns NEW array
np.delete(c2, 2)            # array([3, 6, 9, 7, 8])  — c2 itself is UNCHANGED
# c2 is still: array([3, 6, 5, 9, 7, 8])

len(c1)     # 5 — number of elements
len(c2)     # 6 — c2 has one extra element (the inserted 9)


# =============================================================================
# SECTION 7: Reshape — Changing Array Dimensions
# =============================================================================

a1 = np.array([3, 2, 6, 7, 8, 5, 4, 6])   # 8-element 1D array
len(a1)     # 8

# reshape(rows, cols): total elements must equal rows × cols
a2 = a1.reshape(4, 2)   # 4×2 = 8 ✅ — becomes 4 rows, 2 columns
# array([[3, 2],
#        [6, 7],
#        [8, 5],
#        [4, 6]])

# ❌ ERROR: 4×4=16 ≠ 8
# a3 = a1.reshape(4, 4)  → ValueError

# ❌ ERROR: 4×1=4 ≠ 8
# a3 = a1.reshape(4, 1)  → ValueError

a3 = a1.reshape(2, 4)   # 2×4 = 8 ✅

# Using -1: NumPy auto-calculates that dimension
a4 = a1.reshape(-1, 1)  # 8 rows × 1 col  → column vector (8, 1)
a5 = a1.reshape(-1, 2)  # 4 rows × 2 cols → (-1 auto = 4)
a6 = a1.reshape(2, -1)  # 2 rows × 4 cols → (-1 auto = 4)


# =============================================================================
# SECTION 8: Indexing & Slicing 2D Arrays
# =============================================================================

# a2 = [[3,2], [6,7], [8,5], [4,6]]

a2[1]           # Row at index 1 → array([6, 7])

# ❌ ERROR: Wrong syntax — parentheses used instead of brackets
# a2([2,:])      → SyntaxError

a2[2, :]        # All columns of row 2 → array([8, 5])
a2[:, 1]        # All rows, column 1 → array([2, 7, 5, 6])
a2[:, -1]       # All rows, LAST column → array([2, 7, 5, 6])  (same as col 1 here)

a2[[2, 3], :]   # Rows 2 AND 3 → array([[8,5],[4,6]])
a2[[0, 3], :]   # Rows 0 AND 3 → array([[3,2],[4,6]])


# =============================================================================
# SECTION 9: hstack & vstack — Adding Rows/Columns
# =============================================================================

newcol = np.array([3, 1, 7, 9])
newcol = newcol.reshape(-1, 1)  # Reshape to column vector: shape (4,1)

# ❌ ERROR: hstack takes only ONE positional argument (a list/tuple of arrays)
# a2 = np.hstack([a2], newcol)  → TypeError

# np.hstack: stack arrays SIDE BY SIDE (horizontally, axis=1)
a2 = np.hstack([a2, newcol])    # Adds newcol as 3rd column → shape (4,3)

newrow = np.array([0, 1, 0, 1]) # 4 elements, but a2 has 3 columns now!

# ❌ ERROR: newrow has 4 elements but a2 has 3 columns — must match
# a2 = np.vstack([a2, newrow])  → ValueError: dimension 1 mismatch

newrow = np.array([0, 1, 0])    # 3 elements — matches a2's 3 columns ✅

# np.vstack: stack arrays ON TOP OF EACH OTHER (vertically, axis=0)
a2 = np.vstack([a2, newrow])    # Adds newrow as 5th row → shape (5,3)

# np.insert with axis=0: insert a row at position 3
r1 = np.insert(a2, 3, [10, 15, 17], axis=0)
# Inserts [10,15,17] as a new row between index 2 and 3

# ❌ NumPy arrays have no .pop() or .delete() methods
# newcol1.pop()    → AttributeError
# newcol1.delete() → AttributeError

# np.delete(arr, index, axis): delete along an axis
# np.delete(newcol1, 5, axis=1) → IndexError (axis 1 only has 1 column, no index 5)
newcol1 = np.delete(newcol1, 5)     # Removes element at flat index 5 → array([1,2,3,4,5])
newcol1 = newcol1.reshape(-1, 1)    # Reshape back to column vector (5,1)

a2 = np.hstack([a2, newcol1])       # Now a2 is (5,4): added newcol1 as 4th column


# =============================================================================
# SECTION 10: Arithmetic / Broadcasting
# =============================================================================

f1 = np.array([4, 7, 6, 8, 9])
f2 = np.array([4, 2, 7, 6, 3])

f1 + 5          # Add scalar 5 to EVERY element → array([9, 12, 11, 13, 14])

f0 = 2 * f1 + 5 # Element-wise: multiply each by 2, then add 5 → array([13,19,17,21,23])

f1 + f2 + f0    # Element-wise addition of three arrays → array([21,28,30,35,35])

# Broadcasting example — adding a 1D array to a 2D array
f1 = np.array([3, 5, 4, 6, 7, 9, 3, 1, 2, 6, 7, 9])
f2 = f1.reshape(3, 4)   # 3×4 matrix

f3 = np.array([2, 4, 6, 8])   # 1D with 4 elements = matches columns of f2
f2 + f3   # Broadcasts f3 across each row of f2 → each row gets [+2,+4,+6,+8]

f3 = np.array([3, 4, 5]).reshape(-1, 1)   # Column vector (3,1)
f2 + f3   # Broadcasts f3 across each column of f2 → each column gets [+3,+4,+5]


# =============================================================================
# SECTION 11: Boolean Indexing & np.where()
# =============================================================================

f1 = np.array([3, 5, 4, 6, 7, 9, 3, 1, 2, 6, 7, 9])

# Fancy indexing: pick elements at specific positions
f1[[1, 3, 5, 7]]    # Elements at indices 1,3,5,7 → array([5, 6, 9, 1])
f1[6]               # Single element at index 6 → 3

# np.where(condition): returns a TUPLE of index arrays where condition is True
ind = np.where(f1 > 4)
# (array([ 1,  3,  4,  5,  9, 10, 11]),) — indices where value > 4

type(ind)       # tuple
len(ind[0])     # 7 — number of elements satisfying condition

# Boolean sum: True counts as 1, False as 0 → total count of matching elements
(f1 > 4).sum()  # 7

# ❌ ERROR: .sum(axis) only works for arrays ≥ that many dimensions
# (f1>4).sum(1) → AxisError (f1 is 1D, has no axis=1)

# Use the index tuple to retrieve the actual VALUES
f1[ind]         # array([5, 6, 7, 9, 6, 7, 9])

# Find odd numbers using modulo: p1%2 == 1 for odd, 0 for even
p1 = np.arange(1, 20)       # array([ 1, 2, 3, ..., 19])
ind = np.where(p1 % 2)      # Returns indices where remainder ≠ 0 (i.e., odd numbers)
p1[ind]                     # array([ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19])


# =============================================================================
# SECTION 12: Reshape (More Examples)
# =============================================================================

# ❌ ERROR: 6×8=48, not 49 or 50
# (np.arange(49)).reshape(6, 8) → ValueError
# (np.arange(50)).reshape(6, 8) → ValueError

reshape = (np.arange(48)).reshape(6, 8)    # 6×8=48 ✅ — 6 rows, 8 columns

# ❌ ERROR: np.range doesn't exist — use np.arange
# p1 = np.range(1, 20)  → AttributeError

p1 = np.arange(1, 20)      # 19 elements

# ❌ ERROR: 19 cannot be split into 2×10=20
# p4 = p1.reshape(2, 10)   → ValueError

# Append 20 to make it 20 elements, then reshape
p1 = np.append(p1, 20)     # Now 20 elements

p4 = p1.reshape(-1, 1)     # Column vector: shape (20,1)
p5 = p1.reshape(2, 10)     # 2 rows × 10 cols
p6 = p1.reshape(4, 5)      # 4 rows × 5 cols
p7 = p1.reshape(5, 4)      # 5 rows × 4 cols


# =============================================================================
# SECTION 13: Sorting
# =============================================================================

f1 = np.array([3, 5, 4, 6, 7, 9, 3, 1, 2, 6, 7, 9])

# Python's built-in sorted() — returns a plain Python LIST, ascending
s1 = sorted(f1)

# sorted() with [::-1] reversal — descending order, still a Python list
s1 = sorted(f1)[::-1]

# np.sort() — returns a sorted NumPy ARRAY (f1 itself is NOT modified)
np.sort(f1)     # array([1, 2, 3, 3, 4, 5, 6, 6, 7, 7, 9, 9])

# Reshape f1 to 2D (3×4) for axis-based sorting
f1 = f1.reshape(3, 4)

# np.sort(arr, axis=0): sort each COLUMN independently (top to bottom)
np.sort(f1, axis=0)
# array([[2, 5, 3, 1],   ← smallest in each column
#        [3, 6, 4, 6],
#        [7, 9, 7, 9]])   ← largest in each column

# np.sort(arr, axis=1): sort each ROW independently (left to right) — default
np.sort(f1, axis=1)


# =============================================================================
# SECTION 14: np.sort() — Only ONE axis at a time
# =============================================================================

# ❌ ERROR: Cannot pass axis twice as keyword argument — Python syntax rule
# np.sort(f1, axis=0, axis=1)    → SyntaxError: keyword argument repeated

# ❌ ERROR: Positional arg cannot follow a keyword arg
# np.sort(f1, axis=0, 1)         → SyntaxError

# ❌ ERROR: axis=0 is an int — you can't call an int like a function with ()
# np.sort(f1, axis=0(axis1))     → NameError / SyntaxWarning

# ✅ CORRECT: Sort row-wise (each row sorted left to right)
np.sort(f1, axis=1)
# array([[3, 4, 5, 6],
#        [1, 3, 7, 9],
#        [2, 6, 7, 9]])

# ✅ CORRECT: Sort column-wise (each column sorted top to bottom)
np.sort(f1, axis=0)
# array([[2, 5, 3, 1],
#        [3, 6, 4, 6],
#        [7, 9, 7, 9]])


# =============================================================================
# SECTION 15: resize vs reshape
# =============================================================================

# reshape() returns a NEW array with the new shape — original is UNCHANGED
f1.reshape(12)      # Flattens 3×4 → 1D array of 12 elements (f1 still 3×4)

# ❌ ERROR: reshape(4,) means shape=(4,) which needs exactly 4 elements; f1 has 12
# f1.reshape(4,)    → ValueError: cannot reshape array of size 12 into shape (4,)

# .resize() modifies the array IN-PLACE (changes f1 itself, returns None)
f1.resize(3, 4)     # f1 is now 3×4 shape — modifies f1 directly, returns None

# ❌ ERROR: f1 = f1.resize(...) sets f1 = None because resize() returns None
# f1 = f1.resize(12)   → f1 becomes None! Don't assign the result

# ❌ ERROR: resize() will refuse if another variable also references f1's data
# f1.resize(6, 8)   → ValueError: cannot resize an array that references
#                      or is referenced by another array in this way.
#                      Use np.resize() or refcheck=False

# np.resize(arr, new_shape): ALWAYS works, fills by repeating data if needed
f2 = np.resize(3, 4)   # Creates array of 4 elements all equal to 3
# array([3, 3, 3, 3])   — scalar 3 repeated 4 times


# =============================================================================
# SECTION 16: np.repeat() — Repeat Elements
# =============================================================================

f1 = np.array([3, 5, 4, 6, 7, 9, 3, 1, 2, 6, 7, 9])

# np.repeat(arr, repeats): repeat each element the given number of times
np.repeat(f1, 2)
# Each element repeated 2 times:
# array([3, 3, 5, 5, 4, 4, 6, 6, 7, 7, 9, 9, 3, 3, 1, 1, 2, 2, 6, 6, 7, 7, 9, 9])

# np.repeat(arr, [list of counts]): repeat each element a DIFFERENT number of times
r1 = np.array([9, 8, 7, 6, 5, 4])
np.repeat(r1, [1, 2, 3, 4, 5, 6])
# 9 repeated 1×, 8 repeated 2×, 7 repeated 3×, etc.
# array([9, 8,8, 7,7,7, 6,6,6,6, 5,5,5,5,5, 4,4,4,4,4,4])

# np.sort() does NOT modify original — original f1 stays unsorted
np.sort(f1)     # Returns sorted copy: array([1, 2, 3, 3, 4, 5, 6, 6, 7, 7, 9, 9])
f1              # Still: array([3, 5, 4, 6, 7, 9, 3, 1, 2, 6, 7, 9])


# =============================================================================
# SECTION 17: np.argsort() — Returns Sorted Indices
# =============================================================================

# np.argsort(arr): returns the INDICES that would sort the array (not the values)
np.argsort(f1)
# array([ 7,  8,  0,  6,  2,  1,  3,  9,  4, 10,  5, 11])
# Meaning: f1[7]=1 is smallest, f1[8]=2 is next, f1[0]=3 is next, ...
# Use case: f1[np.argsort(f1)] gives the sorted array


# =============================================================================
# SECTION 18: np.unique() — Unique Values & Counts
# =============================================================================

a1 = np.array([3, 2, 6, 7, 8, 5, 4, 6, 3, 1, 3, 2, 7, 8, 0, 9, 2])

# np.unique(arr): returns sorted array of UNIQUE values only
a2 = np.unique(a1)          # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# np.unique(arr, return_counts=True): also returns how many times each appears
a3 = np.unique(a1, return_counts=True)
# Returns a TUPLE: (unique_values, counts)
# (array([0,1,2,3,4,5,6,7,8,9]), array([1,1,3,3,1,1,2,2,2,1]))
# Meaning: 0 appears 1×, 2 appears 3×, 3 appears 3×, 6 appears 2× etc.

# np.unique(arr, return_index=True): also returns the FIRST index of each unique value
a4 = np.unique(a1, return_index=True)
# (array([0,1,2,3,4,5,6,7,8,9]), array([14, 9, 1, 0, 6, 5, 2, 3, 4, 15]))
# Meaning: 0 first appears at index 14, 1 at index 9, 2 at index 1, etc.


# =============================================================================
# SECTION 19: np.where() for Specific Value Search
# =============================================================================

# Find ALL positions where a1 equals a specific value
np.where(a1 == 1)   # (array([9]),)   → value 1 appears only at index 9
np.where(a1 == 2)   # (array([ 1, 11, 16]),) → value 2 appears at indices 1, 11, 16


# =============================================================================
# SECTION 20: reshape() vs resize() — Key Differences
# =============================================================================

f1 = np.array([3, 5, 4, 6, 7, 9, 3, 1, 2, 6, 7, 9])   # 12-element 1D array

# reshape() → returns a NEW VIEW/array, does NOT modify f1
f1.reshape(3, 4)    # Returns reshaped array; f1 is still 1D
# array([[3, 5, 4, 6],
#        [7, 9, 3, 1],
#        [2, 6, 7, 9]])

# .resize() → modifies f1 IN-PLACE, returns None
f1.resize(3, 4)     # f1 is now 3×4 (changed permanently)

# ❌ ERROR: resize to a LARGER shape that another array also references
# f1.resize(6, 8)   → ValueError: cannot resize an array that references
#                      or is referenced by another array in this way.
#                      FIX: use np.resize(f1, (6,8))  OR  f1.resize(6,8, refcheck=False)

# KEY DIFFERENCE SUMMARY:
# ┌─────────────────┬──────────────────────────┬──────────────────────────┐
# │  Method         │  Modifies original?       │  Returns                 │
# ├─────────────────┼──────────────────────────┼──────────────────────────┤
# │  arr.reshape()  │  NO  (returns new view)   │  New array               │
# │  arr.resize()   │  YES (in-place)           │  None                    │
# │  np.resize()    │  NO  (always works)       │  New array (repeats data)│
# └─────────────────┴──────────────────────────┴──────────────────────────┘
