import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        # we could always take the student with the lowest denominator using a heap
        classes = [(num/denom - (num+1)/(denom+1), num, denom) for num, denom in classes]

        # make the heap of classes according to smallest denominator and biggest numerator
        heapq.heapify(classes)

        # check the trivial case that increasing helps nothing
        if classes[0][0] == 0:
            return 1

        # assign the students
        for _ in range(extraStudents):
            
            # get the class with the smallest denominator and the biggest numerator
            _, num, denom = heappop(classes)

            # increase the amount of students and push it back into the heap
            heappush(classes, ((num+1)/(denom+1) - (num+2)/(denom+2), num+1, denom+1))
        return sum(num/denom for _, num, denom in classes)/len(classes)

        