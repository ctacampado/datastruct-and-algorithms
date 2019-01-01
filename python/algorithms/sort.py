#https://en.wikipedia.org/wiki/Multi-key_quicksort
def quick3Sort(array):
"""     algorithm sort(a : array of string, d : integer) is
        if length(a) ≤ 1 or d ≥ K then
            return
        p := pivot(a, d)
        i, j := partition(a, d, p)   (Note a simultaneous assignment of two variables.)
        sort(a[0:i), d)
        sort(a[i:j), d+1)
        sort(a[j:length(a)), d) """

#https://en.wikipedia.org/wiki/Quicksort
def quickSort(array):
"""     algorithm quicksort(A, lo, hi) is
        if lo < hi then
            p := partition(A, lo, hi)
            quicksort(A, lo, p - 1)
            quicksort(A, p + 1, hi)

    algorithm partition(A, lo, hi) is
        pivot := A[hi]
        i := lo
        for j := lo to hi - 1 do
            if A[j] < pivot then
                if i != j then
                    swap A[i] with A[j]
                i := i + 1
        swap A[i] with A[hi]
        return i """