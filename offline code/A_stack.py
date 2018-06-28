_stack = []

def push(x):
	"""
	Добавляет элемент х в конец стека
	
	>>> size = len(_stack)
	>>> push(5)
	>>> len(_stack) - size
	1
	>>> _stack[-1]
	5
	"""
	_stack.append(x)

def pop():
	x = _stack.pop()
	return x
	
def clear():
	_stack.clear()
	
def is_empty():
	return len(_stack) == 0
	
def top():
	return _stack[len(_stack)-1]