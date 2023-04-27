"""
There are n cars going to the same destination along a one-lane road. The destination is target miles away.

You are given two integer array position and speed, both of length n, where posqition[i] is the position of 
the ith car and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the 
same speed. The faster car will slow down to match the slower car's speed. 
The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.
If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination. """

def carFleet(target, position, speed):
    pair = [(p,s) for p, s in zip(position,speed)] #We create an array of tuples, containing the position and the speed
    stack = []
    pair.sort(reverse=True) #We sort the array in reverse order, to see which car will arrive at the target position
    for p, s in pair:
        stack.append((target - p)/s) #We add to the stack the 'time' that will take to reach the target position
        if len(stack) >= 2 and stack[-1] <= stack[-2]: #If the car arrives at the same time of before, they are a car fleet.
            stack.pop() #We pop the most recent value of the car fleet
    return len(stack) #The number of elements in our stack, are the number of car fleets

target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
print(carFleet(target, position, speed))