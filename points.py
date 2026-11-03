from fractions import Fraction

class Proj:

    def __init__(self, *coordinates):
        self.data = tuple(Fraction(x) for x in coordinates)
        normalizer = next((n for n in self.data if n != 0), None)
        if normalizer is None:
            raise ValueError("zero vector is not a valid point")
        self.data = tuple(x/normalizer for x in self.data)
        
    def __repr__(self):
        return "[" + " : ".join(str(x) for x in self.data) + "]"
        
    def __eq__(self, other):
        if not isinstance(other, Proj): 
                return NotImplemented
        return self.data == other.data

    def __hash__(self):
        return hash(self.data)
