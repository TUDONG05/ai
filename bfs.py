# # Tìm kiếm theo chiều rộng 
# # a) cấu trúc dữ liệu : danh sách kề 


# from collections import deque

# def bfs_path(graph, start, goal):
#     # Hàng đợi (queue) để lưu các đường đi đang được duyệt
#     queue = deque([[start]])
    
#     # Tập hợp các đỉnh đã được thăm
#     visited = set()

#     while queue:
#         path = queue.popleft()       # Lấy đường đi đầu tiên trong hàng đợi
#         node = path[-1]              # Lấy đỉnh cuối cùng trong đường đi

#         if node == goal:
#             return path               # Trả về đường đi khi gặp đích

#         if node not in visited:
#             visited.add(node)
#             for neighbor in graph.get(node, []):
#                 new_path = list(path)
#                 new_path.append(neighbor)
#                 queue.append(new_path)
    
#     return None                       # Không tìm thấy đường đi

# # Đồ thị theo đề bài
# graph = {
#     'A': ['D', 'N', 'K'],
#     'D': ['G'],
#     'N': ['S', 'P', 'Z'],
#     'K': [],
#     'G': ['T'],
#     'S': ['C'],
#     'P': [],
#     'Z': ['B', 'M'],
#     'T': [],
#     'C': [],
#     'B': [],
#     'M': []
# }

# # Theo đề bài: To = A, Tg = P
# start = 'A'
# goal = 'P'

# path = bfs_path(graph, start, goal)
# print("Đường đi từ", start, "tới", goal, "là:", " → ".join(path) if path else "Không có đường đi")


def dfs_path(graph, start, goal, path=None, visited=None):
    if path is None:
        path = [start]
    if visited is None:
        visited = set()
    
    visited.add(start)

    if start == goal:
        return path

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            new_path = dfs_path(graph, neighbor, goal, path + [neighbor], visited)
            if new_path:
                return new_path
    return None


# Đồ thị theo đề bài
graph = {
    'A': ['D', 'N', 'K'],
    'D': ['G'],
    'N': ['S', 'P', 'Z'],
    'K': [],
    'G': ['T'],
    'S': ['C'],
    'P': ['B'],
    'Z': ['M'],
    'T': [],
    'C': [],
    'B': [],
    'M': []
}

# Theo đề: To = A, Tg = T
start = 'A'
goal = 'T'

path = dfs_path(graph, start, goal)
print("Đường đi từ", start, "tới", goal, "là:", " → ".join(path) if path else "Không tìm thấy đường đi")



