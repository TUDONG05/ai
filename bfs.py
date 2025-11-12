# from collections import deque

# def bfs_path(graph, start, goal):
#     # Hàng đợi lưu các đường đi đang được duyệt
#     queue = deque([[start]])
#     # Danh sách lưu thứ tự các đỉnh đã duyệt
#     visited_order = []
#     # Tập hợp để kiểm tra nhanh các đỉnh đã thăm
#     visited = set()

#     while queue:
#         path = queue.popleft()      # Lấy đường đi đầu tiên trong hàng đợi
#         node = path[-1]             # Lấy đỉnh cuối cùng trong đường đi

#         if node not in visited:
#             print("Đang duyệt:", node)  # 👈 In ra từng đỉnh khi duyệt
#             visited.add(node)
#             visited_order.append(node)

#             if node == goal:
#                 return path, visited_order  # Trả về khi gặp đích

#             # Thêm các đỉnh kề vào hàng đợi
#             for neighbor in graph.get(node, []):
#                 new_path = list(path)
#                 new_path.append(neighbor)
#                 queue.append(new_path)
    
#     return None, visited_order


# # Đồ thị theo đề bài
# graph = {
#     'A': ['D', 'N', 'K'],
#     'D': ['G'],
#     'N': ['S', 'P'],
#     'K': ['Z'],
#     'G': [],
#     'S': ['T','C'],
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

# path, visited_order = bfs_path(graph, start, goal)

# print("\n Thứ tự các đỉnh được duyệt:", " → ".join(visited_order))
# print("Đường đi từ", start, "tới", goal, "là:", " → ".join(path) if path else "Không có đường đi")


def dfs_path(graph, start, goal, path=None, visited_order=None):
    if path is None:
        path = [start]
    if visited_order is None:
        visited_order = []

    # Đánh dấu đã duyệt (nếu chưa)
    if start not in visited_order:
        visited_order.append(start)

    # Nếu tìm thấy đích → trả về
    if start == goal:
        return path, visited_order

    # Duyệt các đỉnh kề
    for neighbor in graph.get(start, []):
        if neighbor not in visited_order:
            new_path, visited_order = dfs_path(graph, neighbor, goal, path + [neighbor], visited_order)
            if new_path:
                return new_path, visited_order

    return None, visited_order


# Đồ thị
graph = {
    'A': ['D', 'N', 'K'],
    'D': ['G'],
    'N': ['S'],
    'K': ['P','Z'],
    'G': [],
    'S': ['T','C'],
    'P': ['B'],
    'Z': ['M'],
    'T': [],
    'C': [],
    'B': [],
    'M': []
}

# Theo đề
start = 'A'
goal = 'T'

path, visited_nodes = dfs_path(graph, start, goal)
print("Thứ tự các đỉnh được duyệt:", " → ".join(visited_nodes))
print("Đường đi từ", start, "tới", goal, "là:", " → ".join(path) if path else "Không tìm thấy đường đi")
