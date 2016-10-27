import time    


def mergesort(seq, ascending = True):

    def merge(s1, s2):

        length = len(s1) + len(s2)
        merged = range(length)
        for index in xrange(length):
            if not s1:
                merged[index:] = s2
                break
            elif not s2:
                merged[index:] = s1
                break
            elif s1[0] >= s2[0]:
                merged[index] = s1.pop(0)
            else:
                merged[index] = s2.pop(0)
        return merged
    def initlist(seq):
        length = len(seq)
        retlist = [[max(seq[2*index], seq[2*index+1]),
                    min(seq[2*index], seq[2*index+1])]
                   for index in xrange(length/2)]
        if length % 2:
            retlist[-1] = merge(retlist[-1],[seq[-1]])
        return retlist
    def ms(seq):
        length = len(seq)

        if length == 1:
            return seq[0]
        retseq = [merge(seq[2*index], seq[2*index+1])
                  for index in xrange(length/2)] + ( length % 2 )*[seq[-1]]
        return ms(retseq)
    retlist = ms(initlist(seq))
    return retlist[::-1] if ascending else  retlist

def quicksort(seq, ascending = True):
    
    def divide(seq, pivot):
        retseqs = ([],[])
        for item in seq:
            retseqs[item < pivot].append(item)
        return retseqs
            
    length = len(seq)
    if length <= 1:
        return seq
    elif length == 2:
        return [max(seq), min(seq)]
    pivot = seq.pop()
    s1, s2 = divide(seq, pivot)
    retseq = quicksort(s1) + [pivot] + quicksort(s2)
    return retseq[::-1] if ascending else retseq
    
def heapsort(seq, ascending = True):

    def relocate(seq, length = None):
        if length == None:
            length = len(seq)
        pindex = 0
        cindex = 0
        parent = seq[0]
        children = [2 * pindex + 1, 2 * pindex + 2]
        if length > max(children):
            child, cindex = ((seq[children[0]], children[0])
                              if seq[children[0]] > seq[children[1]]
                              else (seq[children[1]], children[1]))
        elif length == children[1]:
            cindex = children[0]
            child = seq[cindex]
        else:
            return seq
        while child > parent:

            if child > parent:
                seq[cindex], seq[pindex] = parent, child
                cindex, pindex = pindex, cindex
            else:
                return seq
            children = [2 * pindex + 1, 2 * pindex + 2]
            if length > max(children):
                child, cindex = ((seq[children[0]], children[0])
                                  if seq[children[0]] > seq[children[1]]
                                  else (seq[children[1]], children[1]))
            elif length == children[1]:
                cindex = children[0]
                child = seq[cindex]
            else:
                return seq
        return seq
            

        
    def makeheap(seq):
        heap = [seq.pop()]
        index = 1
        while seq:
            heap.append(seq.pop())
            child,  parent = index, (index-1)/2
            while parent >= 0 and heap[parent] < heap[child]:
                heap[parent], heap[child] = heap[child], heap[parent]
                child, parent = parent, (parent - 1)/ 2
            index += 1
        return heap
    heap = makeheap(seq)
    for index in range(len(heap)-1,0,-1):
        heap[0], heap[index] = heap[index], heap[0]
        heap = relocate(heap, length = index)
    return heap if ascending else heap[::-1]

def selectionsort(seq, ascending = True):
    def binsearch(seq, item): 
        if item > seq[-1]:
            seq.append(item)
            return seq
        elif item < seq[0]:
            return [item] + seq
        else:
            floor, ceil = 0, len(seq) - 1
            mid = ceil/2
            while floor < mid < ceil:
                    
                if seq[mid] > item:
                    ceil = mid
                    mid = (ceil + floor) /2
                elif seq[mid] < item:
                    floor = mid
                    mid = (ceil + floor) /2
                elif seq[floor] == seq[ceil] + 2:
                    if seq[mid] > item:
                        break
                    else:
                        mid = ceil
                else:
                    break
            if seq[mid] >= item and seq[floor] <=item:
                return seq[:mid] + [item] + seq[mid:]
            else:
                return seq[:mid+1] + [item] + seq[mid+1:]
    seq = list(seq)
    done = [seq.pop()]
    item = seq.pop()
    done = [done[0], item] if item > done[0] else [item, done[0]]
    while seq:
        done = binsearch(done, seq.pop())
    return done if ascending else done[::-1]
               
def timeit(sorter, seq):
    t = time.time()
    _ = sorter(list(seq))
    return time.time() - t

if __name__ == '__main__':

    import numpy as np

    r = list(np.random.rand(10000))
    print 'selectionsort', timeit(selectionsort, r)
    print 'mergesort', timeit(mergesort, r)
    print 'heapsort', timeit(heapsort, r)
    print 'quicksort', timeit(quicksort, r)
    
    
    
        

