N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

def get_team_score(team):
    score = 0
    for i in team:
        for j in team:
            score += graph[i][j]
    return score

min_diff = float('inf')

def dfs(index, team):
    global min_diff
    
    if len(team) == N // 2:
        link = [i for i in range(N) if i not in team]
        start_score = get_team_score(team)
        link_score = get_team_score(link)
        diff = abs(start_score - link_score)
        min_diff = min(min_diff, diff)
        return
    
    for i in range(index, N):
        dfs(i + 1, team + [i])

dfs(0, [])
print(min_diff)
