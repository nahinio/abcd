# ============================================================
#  CP Python Cheat Sheet + Template
#  Submit always with PyPy 3 (64-bit)
# ============================================================

import sys
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right, insort
from itertools import accumulate, permutations, combinations
from math import gcd, lcm, isqrt, inf

input = sys.stdin.readline
MOD = 10**9 + 7


# ------------------------------------------------------------
#  TEMPLATE
# ------------------------------------------------------------
def solve():
    n = int(input())
    a = list(map(int, input().split()))

    # ---- code here ----

    print(sum(a))


def main():
    t = int(input())
    for _ in range(t):
        solve()


# ------------------------------------------------------------
#  CHEAT SHEET (reference, run korle demo output dekhabe)
# ------------------------------------------------------------
def cheatsheet():
    # ---------- list (vector) ----------
    v = [5, 2, 8]
    v.append(1)                 # push_back
    v.pop()                     # pop_back
    last = v[-1]                # back()
    v.sort()                    # sort ascending
    v.sort(reverse=True)        # descending
    sub = v[0:2]                # subarray, index 0..1
    grid = [[0] * 3 for _ in range(2)]   # 2D vector (correct way)
    print("list:", v, sub, grid)

    pairs = [(1, 5), (1, 3), (2, 4)]
    pairs.sort(key=lambda x: (x[0], -x[1]))   # first asc, second desc
    print("custom sort:", pairs)

    # ---------- dict (map / unordered_map) ----------
    d = {}
    d[7] = d.get(7, 0) + 1
    cnt = defaultdict(int)
    cnt["a"] += 1
    c = Counter([1, 1, 2, 3, 3, 3])
    print("dict:", d, dict(cnt), c.most_common(1))

    # ---------- set ----------
    s = {1, 2, 3}
    s.add(4)
    s.discard(10)               # na thakleo error nai
    print("set:", s, 3 in s, s & {2, 3, 9})

    # ---------- bisect (lower_bound / upper_bound) ----------
    a = [1, 3, 3, 5]
    lb = bisect_left(a, 3)      # lower_bound -> 1
    ub = bisect_right(a, 3)     # upper_bound -> 3
    insort(a, 4)                # sorted rekhe insert
    print("bisect:", lb, ub, ub - lb, a)

    # ---------- heapq (priority_queue, MIN-heap) ----------
    pq = []
    heappush(pq, (3, "c"))
    heappush(pq, (1, "a"))
    top = pq[0]                 # smallest
    first = heappop(pq)
    mx = []
    for x in [4, 9, 2]:
        heappush(mx, -x)        # max-heap trick
    print("heap:", top, first, -heappop(mx))

    # ---------- deque (queue / stack / deque) ----------
    q = deque([1, 2])
    q.append(3)                 # push back
    q.appendleft(0)             # push front
    front = q.popleft()
    back = q.pop()
    print("deque:", front, back, list(q))

    # ---------- string ----------
    st = "hello"
    print("string:", st[::-1], st.find("l"), ord("a"), chr(98))
    chars = list(st)
    chars[0] = "j"
    print("edited:", "".join(chars))

    # ---------- math ----------
    print("math:", gcd(12, 18), lcm(4, 6), isqrt(50),
          pow(2, 10, MOD), pow(3, -1, MOD), -7 // 2)  # -7//2 = -4 (floor!)

    # ---------- itertools ----------
    arr = [1, 2, 3]
    pre = [0] + list(accumulate(arr))     # prefix sum
    print("prefix:", pre)
    print("perms:", list(permutations(arr)))
    print("combs:", list(combinations(arr, 2)))
    for i, x in enumerate(arr):
        pass                    # index + value
    for x, y in zip(arr, pre):
        pass                    # parallel loop

    # ---------- BFS example ----------
    g = defaultdict(list)
    for u, w in [(1, 2), (1, 3), (2, 4)]:
        g[u].append(w)
        g[w].append(u)
    dist = {1: 0}
    bq = deque([1])
    while bq:
        u = bq.popleft()
        for w in g[u]:
            if w not in dist:
                dist[w] = dist[u] + 1
                bq.append(w)
    print("bfs dist:", dist)

    # ---------- fast output ----------
    out = []
    for i in range(3):
        out.append(str(i))
    print("\n".join(out))


# ------------------------------------------------------------
#  Contest e: main() rakho, cheatsheet() comment out koro
# ------------------------------------------------------------
if __name__ == "__main__":
    cheatsheet()
    # main()
