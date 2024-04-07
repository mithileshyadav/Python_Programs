""" 
AREA OF TRIANGLE
Area = 1/2 × b × h.
The basic formula for the area of a triangle is equal to half the product of its base and height, 
"""

# ==========================================
# Normal Way to fine Area of Triangle
# ==========================================
height = int(input("Enter the Height of triangle: ")) 
breadth = int(input("Enter the Breadth of triangle: ")) 
print("Area of Triangle is: ", 0.5*breadth*height)

# ==========================================
# USING FUNCTION BASED FIND AREA OF TRIANGLE
# ==========================================
def areaOfTriangle(h,b):
    return 0.5*b*h
h = int(input("Enter the Height of triangle: ")) 
b = int(input("Enter the Breadth of triangle: ")) 
print("Area of Triangle is: ", areaOfTriangle(h,b))

# ==========================================
# USING CLASS BASED FIND AREA OF TRIANGLE
# ==========================================
class AreaOfTriangle:
    def findArea(self, hght, breth):
        self.__h = hght     # private variable as height
        self.__b = breth     # private variable as breadth
        return 0.5*self.__h*self.__b

# Create an object of AreaOfTriangle
aofTriangle = AreaOfTriangle()
h = int(input("Enter the Height of triangle: ")) 
b = int(input("Enter the Breadth of triangle: "))
area = aofTriangle.findArea(h,b)
print("Area of Triangle is: ", area)

