Clean property based testing for python
========================================

Example usage: sqrt.py::

  from quickconstraint import constrain

  @constrain
  def sqrt(x2: lambda x: 0 <= x):
      x = 1
      while not approx(x*x - x2):
          x = (x + x2/x)/2.0
      return x

test-sqrt.py::

  from quickconstraint import theorem, test_all_theorems

  @theorem
  def theorem_sqrt_sq_inverse(n): return sq(sqrt(n)) == n

  if __name__=="__main__":
      test_all_theorems()
