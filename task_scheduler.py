class Solution(object):
    def leastInterval(self, tasks, n):
        freq = Counter(tasks).values()
        m = max(freq)
        c = list(freq).count(m)
        return max(len(tasks),(m - 1) * (n + 1) + c)