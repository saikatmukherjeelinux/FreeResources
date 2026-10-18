"""Reference implementations corresponding to lessons in the website.
Run: python python_examples/algorithms.py
"""
from collections import deque


def bubble_sort(items):
    a = list(items)
    for end in range(len(a) - 1, 0, -1):
        swapped = False
        for i in range(end):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        if not swapped:
            break
    return a


def selection_sort(items):
    a = list(items)
    for i in range(len(a)):
        m = min(range(i, len(a)), key=lambda j: a[j])
        a[i], a[m] = a[m], a[i]
    return a


def insertion_sort(items):
    a = list(items)
    for i in range(1, len(a)):
        key, j = a[i], i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def linear_search(items, target):
    return next((i for i, x in enumerate(items) if x == target), -1)


def binary_search(sorted_items, target):
    lo, hi = 0, len(sorted_items) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_items[mid] == target:
            return mid
        if sorted_items[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def bfs(graph, start):
    seen, queue, order = {start}, deque([start]), []
    while queue:
        v = queue.popleft()
        order.append(v)
        for w in graph.get(v, []):
            if w not in seen:
                seen.add(w)
                queue.append(w)
    return order


def dfs(graph, start):
    seen, order = set(), []

    def visit(v):
        if v in seen:
            return
        seen.add(v)
        order.append(v)
        for w in graph.get(v, []):
            visit(w)

    visit(start)
    return order


if __name__ == '__main__':
    data = [8, 3, 5, 1, 9, 2]
    for sorting_function in (bubble_sort, selection_sort, insertion_sort):
        print(sorting_function.__name__, sorting_function(data))
    print('linear_search:', linear_search(data, 5))
    print('binary_search:', binary_search(sorted(data), 5))
    graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'],
             'D': [], 'E': ['F'], 'F': []}
    print('bfs:', bfs(graph, 'A'))
    print('dfs:', dfs(graph, 'A'))
