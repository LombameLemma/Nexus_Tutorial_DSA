if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores = list(arr)    
    unique_scores = sorted(list(set(scores)))    
    runner_up_score = unique_scores[-2]
    print(runner_up_score)
