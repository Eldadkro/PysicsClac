from math import sin,cos,tan,log,sqrt,exp,pi,radians
"""this document is created in order to initialize the calc with working vector classes that use regular
    syntax in order to calculate mathmaticle values """
class vector:
    """this class is the vector class in R^3 and will be maintained that way at the moment  """

    #constractor 
    def __init__(self,x = 0,y = 0,z = 0 ):
        self.x =x
        self.y =y
        self.z =z

    #the vector add
    def __add__(self, other):
        return vector(self.x+other.x,self.y+other.y,self.z+other.z)
    
    # for a skalar * vector opperation 
    def __rmul__(self,skalar):
        return vector(self.x*skalar,self.y*skalar,self.z*skalar)

    #for both vector * skalar and vector * vector (regualr skalar poduct)
    def __mul__(self,other):
        try:
            return self.x*other.x+self.y*other.y+self.z*other.z
        except:
            return vector(self.x*other,self.y*other,self.z*other)

    #for printing purpuses     
    def __str__(self):
        return '({}, {}, {})'.format(self.x,self.y,self.z)

    #for the regular expresions in the interpeter
    def __repr__(self):
        return '({self.x}, {self.y}, {self.z}) size = {self.size}'.format(self = self)
    
    #in order to get the norma of a vector OFFICLE
    def __abs__(self):
        return (self*self)**0.5 
    
    #another way to get the norma of a vector (**may be deleted**)
    @property
    def size(self):
        return (self*self)**0.5

    #return the projected vector of other onto self 
    def proj(self, other):
        return ((self * other)*(1/(self.size**2)))*self
    


if __name__ == "__main__":
    #here to create basic values that we use through out all of the course 
    
    x = vector(1) 
    y = vector(0,1)
    z = vector(0,0,1)
    O = vector()
    print('init done ')


