if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))
    sorted_arr = sorted(arr)
    print(sorted_arr[-2])