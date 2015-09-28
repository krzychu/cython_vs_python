from libcpp.unordered_map cimport unordered_map 
cimport numpy as np


def count(np.ndarray[np.uint8_t, ndim=3] arr):
    cdef int num_rows = arr.shape[0]
    cdef int num_cols = arr.shape[1]
    cdef int r = 0
    cdef int c = 0
    cdef int v = 0
    cdef unordered_map[int, int] counts

    while r < num_rows:
        c = 0
        while c < num_cols:
            v = arr[r, c, 0]
            v = v | (arr[r, c, 1] << 8)
            v = v | (arr[r, c, 2] << 16)
            counts[v] +=  1
            c += 1
        r += 1

    return counts
