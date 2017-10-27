Draw a reference diagram for `a` and `b` before and after the third line of the following Python code is executed:

```python
a = [1, 2, 3]
b = a[:]
b[0] = 5
```

Before:

a ---------> [ | , | , |]
               |   |   |
               v   v   v
               1   2   3
               ^   ^   ^
               |   |   |
b ---------> [ | , | , |]

After:

a ---------> [ | , | , |]
               |   |   |
               v   v   v
               1   2   3
                   ^   ^
                   |   |
b ---------> [ | , | , |]
               |
               v
               5
