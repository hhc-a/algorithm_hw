import sys


def sequence_alignment():
    lines = sys.stdin.read().splitlines()
    if len(lines) < 2:
        return

    x = lines[0].strip()
    y = lines[1].strip()
    m, n = len(x), len(y)

    opt = [[0] * (n + 1) for _ in range(m + 1)]

    # 邊界條件：剩餘字元皆對應 gap（罰點 2）
    for j in range(n - 1, -1, -1):
        opt[m][j] = opt[m][j + 1] + 2
    for i in range(m - 1, -1, -1):
        opt[i][n] = opt[i + 1][n] + 2

    # 課本 3.7 節動態規劃填表（由右下往左上計算）
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            penalty = 0 if x[i] == y[j] else 1
            opt[i][j] = min(
                opt[i + 1][j + 1] + penalty,
                opt[i + 1][j] + 2,
                opt[i][j + 1] + 2,
            )

    # 從 (0, 0) 回溯還原最佳對齊序列
    align_x = []
    align_y = []
    i, j = 0, 0

    while i < m and j < n:
        penalty = 0 if x[i] == y[j] else 1
        if opt[i][j] == opt[i + 1][j + 1] + penalty:
            align_x.append(x[i])
            align_y.append(y[j])
            i += 1
            j += 1
        elif opt[i][j] == opt[i + 1][j] + 2:
            align_x.append(x[i])
            align_y.append("-")
            i += 1
        else:
            align_x.append("-")
            align_y.append(y[j])
            j += 1

    while i < m:
        align_x.append(x[i])
        align_y.append("-")
        i += 1
    while j < n:
        align_x.append("-")
        align_y.append(y[j])
        j += 1

    # 輸出最少罰點總數與兩行對齊結果
    print(opt[0][0])
    print("".join(align_x))
    print("".join(align_y))


if __name__ == "__main__":
    sequence_alignment()