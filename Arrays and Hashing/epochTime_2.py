def meeting_planner(slotsA, slotsB, dur):
    sizeA, sizeB = len(slotsA), len(slotsB)
    iA, iB = 0, 0
    array = [1, 0]
    while iA < sizeA and iB < sizeB:
        A_start, A_end = slotsA[iA]
        B_start, B_end = slotsB[iB]
        start = max(A_start, B_start)
        end = min(A_end, B_end)
        overlap = end - start
        if overlap >= dur:
            return [start, start + dur]
        elif slotsA[iA][1] < slotsB[iB][1]:
            iA += 1
        else:
            iB += 1
    return [] 

slotsA = [[10, 50], [60, 120], [140, 210]]
slotsB = [[0, 15], [60, 70]]
dur = 8
print(meeting_planner(slotsA, slotsB, dur))