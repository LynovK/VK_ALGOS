def find_max_path_sum():
    def dfs(node):
        if not node:
            return 0,[]
    left_sum, left_path = dfs(node.left)
    right_sum, right_path = dfs(node.right)
    if left_sum > right_sum:
        current_max_path = left_path + [node.val]
    else:
        current_max_sum = max(left_sum,right_sum) + node.val

    if left_sum + node.val + right_sum > current_max_sum:
        max_sum = left_sum + node.val + right_sum
        max_path = left_path + [node.val] + right_path

    return current_max_sum, current_max_path

    global max_sum = min(int)
    global max_path = []
    dfs(root)
    return max_path
