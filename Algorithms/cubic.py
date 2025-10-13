def matrix_multiply(A, B):
    """Multiplies two matrices A and B."""
    n = len(A)
    m = len(B[0])
    p = len(B)
    # Initialize the result matrix with zeros
    C = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(p):
                C[i][j] += A[i][k] * B[k][j]
    return C
# Example usage:
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result = matrix_multiply(A, B)
print("Resultant matrix is:")
for row in result:
    print(row)