def seq_search(arr, ele):
    pos = 0
    found = False
    stopped = False
    while pos < len(arr) and not found and not stopped:
        if arr[pos] == ele:
            found = True
        else:
            if arr[pos] > ele:
                stopped = True
            pos+=1
    return found

def bin_search(arr, ele):
    first = 0
    last = len(arr) - 1
    found = False
    while first <= last and not found:
        mid = (first+last)/2
        if arr[mid] == ele:
            found = True
        else:
            if ele < arr[mid]:
                last = mid -1
            else:
                first = mid + 1
    return found

def rec_bin_search(arr, ele):

    if len(arr) == 0:
        return False
    else:
        mid = len(arr)/2
        if arr[mid] == ele:
            return True
        else:
            if ele < arr[mid]:
                return rec_bin_search(arr[:mid], ele)
            else:
                return rec_bin_search(arr[mid +1:],ele)



