# What are the primary conecepts of object oriented programing?

The concepts of object oriented programing are that you have objects which contain either data or methods

An example would be
```python
class test(object):
    def __init__(self):
        self.x = 10
    def test(self):
        print('test')
        print(self.x)
```

The class contains data and methods that a program can create and manipulate. So if

```python
n = test()
n.x = 12
```
`n.x` would be set to 12

The output of `n.test()` would be
```
test
12
```
