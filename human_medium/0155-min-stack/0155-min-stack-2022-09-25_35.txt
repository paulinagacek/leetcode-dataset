class MinStack:

  def __init__(self):
    self.stack = []
    self.min_stack = []

  def push(self, val: int) -> None:
    if self.min_stack: # check if stack is non-empty
      self.min_val = min(self.min_stack[-1], val) #update min_stack accordingly
    else:
      self.min_val = val
    self.min_stack.append(self.min_val)
    self.stack.append(val)


  def pop(self) -> None:
    self.stack.pop()
    self.min_stack.pop()
    

  def top(self) -> int:
    return self.stack[-1]


  def getMin(self) -> int:
    return self.min_stack[-1]
