import random


def isPointInCircle(point):
    if (point[0] - 0.5)**2 + (point[1] - 0.5)**2 < 0.5**2:
        return True
    else:
        return False
    
    
    
    
numberPointsInCircle = 0
iterations = 100000



for iteration in range(iterations):
    # Random point in square generated
    point = [random.random(), random.random()]
    if isPointInCircle(point) == True:
        numberPointsInCircle +=1
        
        
        


print("Total points generated: " + str(iterations))
print("Points inside the circle: " + str(numberPointsInCircle))
print("PI calculated: " + str(4 * numberPointsInCircle / iterations))

    
    
    


