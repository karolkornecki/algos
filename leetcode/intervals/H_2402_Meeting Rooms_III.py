from typing import List
from heapq import heappush, heappop


class Reservation:
    def __init__(self, room_no: int, end_date: int):
        self.room_no = room_no
        self.end_date = end_date

    def __repr__(self):
        return f"r[{self.room_no}] - e[{self.end_date}]"

    def __lt__(self, other):
        if self.end_date < other.end_date:
            return True
        if self.end_date > other.end_date:
            return False
        return self.room_no < other.room_no


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        counter = [0 for _ in range(n)]
        available_rooms = [i for i in range(n)]
        reservations = []  # (room, end_date)

        while meetings:
            start_date, end_date = meetings.pop(0)
            # free room if there is any booked one until current start
            while reservations and reservations[0].end_date <= start_date:
                reservation = heappop(reservations)
                heappush(available_rooms, reservation.room_no)
            # now reserve room by taking free or taking the one where meeting ends the soonest
            if available_rooms:
                room_no = heappop(available_rooms)
                heappush(reservations, Reservation(room_no, end_date))
                counter[room_no] += 1
            else:
                reservation = heappop(reservations)
                heappush(reservations, Reservation(reservation.room_no, reservation.end_date + (end_date - start_date)))
                counter[reservation.room_no] += 1

        return counter.index(max(counter))


if __name__ == '__main__':
    s = Solution()
    assert s.mostBooked(2, [[0, 10], [1, 5], [2, 7], [3, 4]]) == 0
    assert s.mostBooked(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]) == 1
    assert s.mostBooked(2, [[0, 10], [1, 2], [12, 14], [13, 15]]) == 0
    assert s.mostBooked(3, [[0, 10], [1, 9], [2, 8], [3, 7], [4, 6]]) == 1
    assert s.mostBooked(4, [[19, 20], [14, 15], [13, 14], [11, 20]]) == 1
    assert s.mostBooked(4, [[48, 49], [22, 30], [13, 31], [31, 46], [37, 46], [32, 36], [25, 36], [49, 50], [24, 34],
                            [6, 41]]) == 0
