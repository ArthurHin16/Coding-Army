"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that 
answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""
def dailyTemperatures(temperatures):
    result = [0] * len(temperatures)
    stack = [] #The stack will have a pair value [temperature, index]
    for index, temp  in enumerate(temperatures): #The enumerate() method returns the index, value
        while stack and temp > stack[-1][0]:
            stackT, stackI = stack.pop()
            result[stackI] = ( index - stackI )
        stack.append([temp, index]) #Monotonic Decreasing Stack
    return result
temperatures = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temperatures))