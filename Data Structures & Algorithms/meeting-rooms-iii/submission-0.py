from heapq import heappush, heappop
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available_rooms = [i for i in range(n)]
        used_rooms = []
        used_counter = [0] * n
        
        meetings.sort( key = lambda x: x[0])

        for start, end in meetings:
            #check for opening
            while used_rooms and used_rooms[0][0]<=start: #is it just ended now
                _,room = heappop(used_rooms)
                heappush(available_rooms,room)
            
            # forced to delay
            if len(available_rooms) == 0:
                earliest_end, room = heappop(used_rooms)
                end = earliest_end + (end-start)
                heappush(available_rooms, room)
            
            #append to heap
            empty_room = heappop(available_rooms)
            heappush(used_rooms,(end, empty_room))
            used_counter[empty_room] += 1
        return used_counter.index(max(used_counter))


            