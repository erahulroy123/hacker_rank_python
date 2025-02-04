if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    coordinates = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if sum([i, j, k]) != n] #[iterable, for loop/loops, condition]
    print(coordinates)
    

# coordinates = []
# 
# for i in range(x + 1):
#     for j in range(y + 1):
#         for k in range(z + 1):
#             if sum([i+j+k]) != n:
#                 coordinates.append([i, j, k])
# 
# print(coordinates)
