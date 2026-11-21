# REVERSEWORD - Rating 850

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Reverse Words in a String

You are given a string $s$ consisting of English letters, digits, and spaces `' '`.
Your task is to  **reverse the order of the words**  in the string.

A word is defined as a sequence of non-space characters.
The words in $s$ are separated by one or more spaces.

You must:

- Return the words in reverse order, separated by a single space.
- Remove any leading, trailing, or multiple spaces between words.
### Function Declaration
### Function Name

$reverseWords$ – This function reverses the order of words in a given string while removing extra spaces.

### Parameters
- $s$ : A reference to a string consisting of English letters (uppercase and lowercase), digits, and spaces.
### Return Value
- Returns a string where: The order of words is reversed. Words are separated by a single space. Leading, trailing, and multiple spaces are removed.
## Constraints
- $1 \leq T \leq 100$
- $1 \leq |s| \leq 10^4$
- The string contains English letters (uppercase and lowercase), digits, and spaces.
- There is at least one word in the string.
### Input Format
- The first line contains a single integer $T$ — the number of test cases.
- Each of the next $T$ lines contains a string $s$.
### Output Format
- For each test case, print a single line containing the string with words in reverse order, separated by a single space.
### Sample 1:
Input
Output

```
4
codechef is awesome
  java   and   python  
123 test case
   learn   data   structures   

```

```
awesome is codechef
python and java
case test 123
structures data learn

```

### Sample 2:
Input
Output

```
1
Roses are red
```

```
red are Roses
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-21T15:21:06.227Z  

```py
def reverse_words(s: str) -> str:
    words = s.split()
    words.reverse()
    return " ".join(words)
    # .
```

---

[View on CodeChef](https://www.codechef.com/problems/REVERSEWORD)