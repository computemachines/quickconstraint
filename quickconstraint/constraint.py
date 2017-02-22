import types
from inspect import signature

constrained = {}
theorems = []

class Constraint:
    def __init__(self, predicate=lambda x: True):
        self._predicate = predicate # function arg 'predicate' does not need self arg
    def __call__(self, value):
        return self.predicate(value)
    def predicate(self, value):
        return self._predicate(value)
    
class And(Constraint):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def predicate(self, value):
        return a(value) and b(value)
class TypeConstraint(Constraint):
    def __init__(self, _type):
        self._type = _type
    def predicate(self, value):
        return type(value) == self._type

def constrain(f):
    """Do not call with params."""
    print("constrain(f={})".format(f))
    
    def wrapper(*args):
        bound_args = constrained[wrapper].bind(*args)
        for arg in bound_args.arguments:
            value = bound_args.arguments[arg]
            constraint = constrained[wrapper].parameters[arg].annotation
            if type(constraint) == type:
                constraint = TypeConstraint(constraint)
            elif type(constraint) == types.FunctionType or type(annotation) == types.LambdaType:
                constraint = Constraint(constraint)
            assert(constraint(value))
        return f(*args)
    
    constrained[wrapper] = signature(f)
    return wrapper

def theorem(a, b=None):
    print("theorem({}, {})".format(a, b))
    def wrapper(f):
        print("theorem.wrapper({})".format(f))
        theorems.append(f)
        return f
    return wrapper