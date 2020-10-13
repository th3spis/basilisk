def quine():
    #returns the code of this function
    import inspect
    lines = inspect.getsource(quine)
    return lines[len('def quine(): '):]

#prints its code
def example():
  s = 's = %r\nprint(s %% s)'
  print(s % s)
  
print(quine())
print("\n\n")
example()
