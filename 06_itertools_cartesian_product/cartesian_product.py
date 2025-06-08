
from itertools import product

if __name__ == '__main__':
    
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    cartesian_product = product(A,B)
    
    print(' '.join(str(t) for t in cartesian_product))
    
