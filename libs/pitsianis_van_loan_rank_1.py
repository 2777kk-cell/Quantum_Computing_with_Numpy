import numpy as np

def pitsianis_van_loan_rank_1(A, m1, n1, m2, n2):
    """
    Computes the optimal rank-1 Kronecker product approximation of matrix A.

    A is assumed to have dimensions (m1 * m2, n1 * n2).
    The approximation is A_approx = U1 @ V1, where U1 has dimensions (m1, n1)
    and V1 has dimensions (m2, n2).

    Args:
        A (np.ndarray): The input matrix.
        m1 (int): Row dimension of the first factor.
        n1 (int): Column dimension of the first factor.
        m2 (int): Row dimension of the second factor.
        n2 (int): Column dimension of the second factor.

    Returns:
        tuple: (U1, V1) the two factor matrices.
    """
    # 1. Reshape the input matrix A into a permuted matrix T
    # The dimensions of T will be (m1 * n1, m2 * n2)
    T = A.reshape(m1, m2, n1, n2).transpose(0, 2, 1, 3).reshape(m1 * n1, m2 * n2)
    
    # 2. Perform Singular Value Decomposition (SVD) on T
    U, S, Vh = np.linalg.svd(T, full_matrices=False)
    
    # 3. The best rank-1 approximation is based on the first singular value and vectors
    # U has dimensions (m1*n1, rank), Vh has dimensions (rank, m2*n2)
    # The first (left) singular vector is U[:, 0]
    # The first (right) singular vector is Vh[0, :]
    s1 = S[0]
    u1_vec = U[:, 0]
    v1_vec = Vh[0, :]
    
    # 4. Reshape the singular vectors back into the desired factor dimensions
    U1 = np.sqrt(s1) * u1_vec.reshape(m1, n1)
    V1 = np.sqrt(s1) * v1_vec.reshape(m2, n2)
    
    return U1, V1