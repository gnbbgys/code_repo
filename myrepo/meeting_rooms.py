import pkgutil
import heapq
import math

def get_meeting_rooms(schedule: list) -> int:

    if schedule is None:
        return 0

    starts = []
    ends = []
    for meeting in schedule:
        starts.append((meeting[0], 1))
        ends.append((meeting[1],-1))

    heapq.heapify(starts)
    heapq.heapify(ends)
    
    print(starts)
    print(ends)
    print("========================")
    num_room = 1
    max_room = 1
    meeting = heapq.heappop(starts)
    
    while starts or ends:
        
        peek_start = starts[0][0] if starts else None
        peek_end = ends[0][0] if ends else None
        
        if peek_end is None:
            next_slot = starts
        elif peek_start is None:
            next_slot = ends
        elif peek_end > peek_start:
            next_slot = starts
        else:
            next_slot = ends
        
        num_room += heapq.heappop(next_slot)[1]
        print(starts)
        print(ends)
        max_room = max(max_room, num_room)
        
    return max_room
            

#examples:	
#schedule = [(1,2),(3,4)]
#schedule = [(1,5),(3,6),(8,9)]
schedule = [(2,5),(4,7),(3,9),(1,5),(10,20)]
print(get_meeting_rooms(schedule))

def swap(in_arr: list, r1: int, r2: int):
    
    if r1 >= len(in_arr) or r2 >= len(in_arr):
        return
    
    if r1 == r2:
        return
        
    temp = in_arr[r1]
    in_arr[r1] = in_arr[r2]
    in_arr[r2] = temp
    
# examples:	
# [(1,2),(3,4)]
# [(1,5),(3,6),(8,9)]
# schedule = [(2,5),(4,7),(3,9),(1,5),(10,20)]
# print(get_meeting_rooms(schedule)

def heapify(in_arr: list, arr_len: int, idx: int):
            
    l = 2*idx + 1
    r = 2*idx + 2
    
    m = idx
    if l < arr_len and in_arr[l] > in_arr[m]:
        m = l
    if r < arr_len and in_arr[r] > in_arr[m]:
        m = r
    print(m)
    
    if m != idx:
        swap(in_arr, idx, m)
        heapify(in_arr, arr_len, m)
        

def build_heap(in_arr: list, arr_len: int):
    
    if arr_len <= 0:
        return
    print(arr_len)
    last_root_idx = math.floor(arr_len/2) - 1
    for idx in range(last_root_idx, -1, -1):
        print(idx)
        heapify(in_arr, arr_len, idx)
    
    
#in_array = [2, 4, 5, 7, 6, 9, 10]
#build_heap(in_array, len(in_array))
#print(in_array)
