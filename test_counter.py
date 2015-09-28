from PIL import Image
from collections import defaultdict
import numpy as np
import time
import counter


def count_in_python(arr):
    cnt = defaultdict(int)
    for r in xrange(arr.shape[0]):
        for c in xrange(arr.shape[1]):
            px = tuple(arr[r, c])
            cnt[px] += 1
    return cnt


def count_in_cython(arr):
    return counter.count(arr)


def test_counter(arr, f):
    t = time.time()
    f(arr)
    duration = time.time() - t
    print '{0}: {1}'.format(f.__name__, duration)


if __name__ == '__main__':
    img = Image.open('marmot.png')
    arr = np.array(img)

    assert arr.dtype == 'uint8'
    assert len(arr.shape) == 3
   
    test_counter(arr, count_in_cython)
    test_counter(arr, count_in_python)
