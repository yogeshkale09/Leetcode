class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str: 
        # Python only have min heap
        heap = [(-ord(key), value) for key, value in Counter(s).items()]
        heapq.heapify(heap)
        ans = ""

        while heap:
            # The current character
            k, v = heapq.heappop(heap)
            if v <= repeatLimit:
                # Add all this character
                ans += chr(-k) * v
            else:
                # Only add limit numbers of character
                ans += chr(-k) * repeatLimit
                # If nothing in the heap (no next character), then we have the answer
                if not heap:
                    break
                # The next character
                nk, nv = heapq.heappop(heap)
                # Add one to the answer
                ans += chr(-nk)
                # If there's still next character remaining, add it back to the heap
                if nv > 1:
                    heapq.heappush(heap, (nk, nv - 1))
                # Add the remaining current character back to the heap
                heapq.heappush(heap, (k, v - repeatLimit))
        return ans
        