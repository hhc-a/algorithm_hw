import sys


def floyd_warshall():
    # 使用 split() 自動處理一個或多個空白與換行字元
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    n = int(tokens[0])
    INF = 10**9

    # 讀取相鄰矩陣，將 -1 轉換為 INF
    dist = []
    idx = 1
    for _ in range(n):
        row = []
        for _ in range(n):
            val = int(tokens[idx])
            idx += 1
            row.append(INF if val == -1 else val)
        dist.append(row)

    # Floyd-Warshall 核心演算法（k 必須為最外層迴圈）
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] < INF and dist[k][j] < INF:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

    # 輸出最短距離矩陣 D
    for i in range(n):
        print(" ".join("-1" if dist[i][j] == INF else str(dist[i][j]) for j in range(n)))


if __name__ == "__main__":
    floyd_warshall()