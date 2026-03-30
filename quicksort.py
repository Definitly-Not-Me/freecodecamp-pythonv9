
def quick_sort(array):
    length = len(array)
    if length <= 1:
        return array
    if length == 2:
       return [min(array[0], array[1]), max(array[0], array[1])]
    pivot = array[length - 1]
    lesser = []
    equal = []
    greater = []

    for num in array:
        if num < pivot:
            lesser.append(num)
        elif num > pivot:
            greater.append(num)
        else:
            equal.append (num)  
     
    return quick_sort(lesser) + equal + quick_sort(greater)