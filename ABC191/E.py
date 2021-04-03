from heapq import heappush, heappop

# 町数と道路数の入力
N, M = map(int, input().split())
# 道路
edge = [[] for _ in range(N)]

# 道路情報の入力
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1 # インデックスと町の番数をそろえるため
    b -= 1 # インデックスと町の番数をそろえるため
    edge[a].append((b, c))

ans = [-1]*N # 答え(時間)を入れる配列
path = [-1]*(N) # ノード
print(edge)
for n in range(N): # 町数繰り返す
    hq = [] # ヒープキュー
    for v_to, cost in edge[n]: # 自己ループを考慮して、最初にまず1手目の町をすべてヒープキューに入れる
        heappush(hq, (cost, v_to)) # ヒープキューに(距離, 行先)を追加
    while hq: # ダイクストラ法
        now_cost, v = heappop(hq) # 一番距離が短いのを取り出す
        print(v, now_cost)
        if v == n: # 戻ってきたら終了
            ans[n] = now_cost
            break
        elif path[v] < n: # まだ計算してない場合
            path[v] = n
            for v_to, cost in edge[v]: # 現在のノードからの道路ごと
                c = now_cost + cost 
                heappush(hq, (c, v_to)) # 進んだ場合のコストをプッシュする

for i in range(N):
    print(ans[i])
