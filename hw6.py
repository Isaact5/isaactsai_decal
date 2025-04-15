import numpy as np

#1
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def containsPrimes(arr):
    mask = np.array([any(is_prime(x) for x in row) for row in arr])
    return arr[mask]

# Test function
#arr = np.array([[2, 3, 5], [4, 6, 8], [11, 13, 17], [7, 10, 13]])
#result = containsPrimes(arr)
#print(result)


#2.1
def checkerboard():
    board = np.zeros((8, 8), dtype=int)
    
    for i in range(0, 8, 2):
        board[i, ::2] = 1
        
    return board

#2.2
def checkerboard():
    board = np.zeros((8, 8), dtype=int)
    
    for i in range(0, 8, 2):
        board[i, ::2] = 1
    
    for i in range(1, 8, 2):
        board[i, 1::2] = 1

    return board

#2.3
def reverse_checkerboard():
    board = np.zeros((8, 8), dtype=int)
    
    for i in range(0, 8, 2):
        board[i, 1::2] = 1
    
    for i in range(1, 8, 2):
        board[i, ::2] = 1
        
    return board

# Test functions
#print(checkerboard())
#print(reverse_checkerboard())

#3
def expansion(universe, spaces):
    spacing = ' ' * spaces
    
    def expand_string(s):
        return spacing.join(list(s))
    
    expanded = np.array([expand_string(s) for s in universe])
    return "['" + "', '".join(expanded) + "']" #this is for the comma lol or else I would've just returned expanded

# Test functions
#universe = np.array(['galaxy', 'clusters'])
#print(expansion(universe, 1))
#print(expansion(universe, 2))

#4
def secondDimmest(stars):
    return np.array([np.sort(stars[:, i])[1] for i in range(stars.shape[1])])

# Test function
#np.random.seed(123)
#stars = np.random.randint(500, 2000, (5, 5))
#print(stars)
#print(secondDimmest(stars))