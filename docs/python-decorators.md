

# Python 装饰器

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import wraps

def logit(func):
	@wraps(func)
	def with_logging(*args, **kwargs):
		print(func.__name__ + "was called!")
		return func(*args, **kwargs)
	return with_logging

@logit
def addition_func(x):
	"""Do some math."""
	return x + x


result = addition_func(4)
print(result)
```