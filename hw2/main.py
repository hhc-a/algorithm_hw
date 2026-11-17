import sys


def matrix_chain_order():
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    n = int(tokens[0])
    d = [int(tokens[i + 1]) for i in range(n + 1)]

    # 使用 1-based 索引對應課本演算法
    M = [[0] * (n + 1) for _ in range(n + 1)]
    P = [[0] * (n + 1) for _ in range(n + 1)]

    for diagonal in range(1, n):
        for i in range(1, n - diagonal + 1):
            j = i + diagonal
            M[i][j] = float("inf")
            for k in range(i, j):
                cost = M[i][k] + M[k + 1][j] + d[i - 1] * d[k] * d[j]
                if cost < M[i][j]:
                    M[i][j] = cost
                    P[i][j] = k

    def print_matrix(title, mat):
        print(title)
        for i in range(1, n + 1):
            row_str = []
            for j in range(1, n + 1):
                if j == 1:
                    row_str.append(str(mat[i][j]) if i == 1 else " ")
                elif j < i:
                    row_str.append("     ")
                else:
                    row_str.append(f"{mat[i][j]:5d}")
            print("".join(row_str))

    def build_order(i, j, is_root=False):
        if i == j:
            return f"A{i}"
        k = P[i][j]
        left = build_order(i, k, False)
        right = build_order(k + 1, j, False)
        sep = "" if (k == i and k + 1 == j) else " "
        expr = f"{left}{sep}{right}"
        return expr if is_root else f"({expr})"

    print_matrix("M =", M)
    print_matrix("P =", P)
    print(f"Optimal Solution: {build_order(1, n, True)}")


if __name__ == "__main__":
    matrix_chain_order()