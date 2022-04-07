# 최단 경로

```
  최단 경로 알고리즘은 가장 짧은 경로를 구하는 알고리즘이다. 
  최단 경로 알고리즘은 크게 2가지로 나뉜다.
  
  첫번째는 한 노드에서 나머지 모든 노드로의 최단거리를 구하는
  다익스트라 최단 경로 알고리즘 두번째는 모든 노드에서 다른 모든 노드로의
  최단 거리를 구한 플로아드 워셜 알고리즘이다.
```

## 다익스트라 알고리즘

```
   다익스트라 알고리즘은 5단계의 절차를 거친다.
   1. 출발 노드를 설정한다.
   2. 최단 거리 테이블을 INF와 같이 매우 큰 값으로 초기화한다.
   3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
   4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블(리스트)을 업데이트한다.
   5. 3, 5번을 반복한다.
```

### 다익스트라 구현(힙정렬 사용)
```python
  import heapq
  import sys
  input = sys.stdin.readline
  INF = int(1e9)

  n, m = map(int, input().split())
  start = int(input())

  graph = [[] for i in range(n+1)]
  distance = [INF] * (n+1)

  for _ in range(m):
      a, b, c = map(int, input().split())
      graph[a].append((b, c))


  def dijkstra(start):
      q = []

      heapq.heappush(q, (0, start))
      distance[start] = 0

      while q:
          dist, now = heapq.heappop(q)

          if distance[now] < dist:
              continue

          for i in graph[now]:
              cost = dist + i[1]

              if cost < distance[i[0]]:
                  distance[i[0]] = cost
                  heapq.heappush(q, (cost, i[0]))

  dijkstra(start)

```
## 플로이드 워셜 알고리즘
```
  플로이드 워셜 알고리즘은 모든 지점에서 다른 모든 지점으로의 최솟값을 찾는 다대다 알고리즘이다.
  이 알고리즘의 특징은 중간에 거치는 지점을 두었을때 거리가 한번에 가는 거리와 비교하여 
  업데이트 하는 방식이다. 
  
  그렇기 때문에 각각의 노드들을 "거쳐가는 노드"로 보고 알고리즘을 구현한다.
```

### 플로이드 워셜 구현
```python
  INF = int(1e9)

  n = int(input())
  m = int(input())

  graph = [[INF] * (n+1) for _ in range(n+1)]

  for a in range(1, n+1):
      for b in range(1, n+1):
          if a == b:
              graph[a][b] = 0

  for _ in range(m):
      a, b, c = map(int, input().split())
      graph[a][b] = c


  for k in range(1, n+1):
      for a in range(1, n+1):
          for b in range(1, n+1):
              graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
```

