def meeting_planner(slotsA, slotsB, dur):
    """
    1. Loop throw the array and safe the start values of sloatA in a hashmap 10, 60, 140
    time[slotsA[i][0]] = slotsA[i][1]
        {
            10 -> 50
            60 -> 120
            140 - 210
        }
    Verify if the start time exists in slotsB time.get(slotsB[i][0]) in hashmap
        if it existist check if the total_time = slotsB[i][0] is less than the end_time and if it is less
        than the end time of slotsA time.get(slotsB[i][0]) add  the element in the result and the sum
    
    [[6,12]], [[2,11]], 5
    [6, 12]
    [2, 11]
    """
    total_time = 0
    times = {}
    for i in range(len(slotsA)):
        times[slotsA[i][0]] = slotsA[i][1]
    
    for j in range(len(slotsB)):
        if slotsB[j][0] in times:
            total_time = slotsB[j][0] + dur
            if total_time <= slotsB[j][1] and total_time <= times[slotsB[j][0]]:
                return [slotsB[j][0], slotsB[j][0] + dur]
    
    return []
slotsA = [[10, 50], [60, 120], [140, 210]]
slotsB = [[0, 15], [60, 70]]
dur = 8
print(meeting_planner(slotsA, slotsB, dur))
