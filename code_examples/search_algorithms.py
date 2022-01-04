class Search:
    def linear_search(self, _list, search_for):
        '''
        sequential search is made over all items one by one. 
        Every item is checked and if a match is found then that particular item is returned, 
        otherwise the search continues till the end of the data structure.

        returns whether the value is within the list
        '''
        for i in range( len(_list)): 
            if _list[i] == search_for:
                return True
            else:
                return False

    def binary_search(self, _list, search_for):
        '''
        implementation of the binary search algorithm using iteration
        takes a list or array as _list
        and a value in search_for

        returns the index of the item within the list
        '''
        first = 0
        last = len(_list) - 1
        index = -1
        while (first<=last) and (index==-1):
            mid = (first+last)//2
            if _list[mid] ==search_for:
                index = mid
            else:
                if search_for < _list[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
        return index

    def jump_search(self, _list, search_for):
        '''
        Takes a list and jumps between the list in jumps equal to the square root of list length
        Identfying the jumps we perform a linear search within the list split
        '''
        import math
        length = len(_list)
        jump = int(math.sqrt(length))
        left, right = 0, 0
        while left < length and _list[left] <= search_for:
            right = min(length - 1, left + jump)
            if _list[left] <= search_for and _list[right] >= search_for:
                break
            left += jump
        if left >= length or _list[left] > search_for:
            return -1
        right = min(length - 1, right)
        i = left
        while i <= right and _list[i] <= search_for:
            if _list[i] == search_for:
                return i
            i += 1
        return -1

    def fibonacci_search(self, _list, search_for):
        fibM_minus_2 = 0  #2nd precing fibM
        fibM_minus_1 = 1  #1st preceding fibM
        fibM = fibM_minus_1 + fibM_minus_2
        while (fibM < len(_list)):
            fibM_minus_2 = fibM_minus_1
            fibM_minus_1 = fibM
            fibM = fibM_minus_1 + fibM_minus_2
        index = -1;
        while (fibM > 1):
            i = min(index + fibM_minus_2, (len(_list)-1))
            if (_list[i] < search_for):
                fibM = fibM_minus_1
                fibM_minus_1 = fibM_minus_2
                fibM_minus_2 = fibM - fibM_minus_1
                index = i
            elif (_list[i] > search_for):
                fibM = fibM_minus_2
                fibM_minus_1 = fibM_minus_1 - fibM_minus_2
                fibM_minus_2 = fibM - fibM_minus_1
            else :
                return i
        if (fibM_minus_1 and index < (len(_list)-1) and _list[index+1] == search_for):
            return index+1
        return index

    def exponential_search(self, _list, search_for):
        import numpy as np
        x = len(_list)
        if _list[0] == search_for:
            return 0
        index = 1
        while index < len(_list) and _list[index] <= search_for:
            index = index * 2
        return self.binary_search( _list[:min(index, x)] , search_for)

    def interpolation_search(self, _list, search_for):
        low = 0
        high = (len(_list) - 1)
        while low <= high and search_for >= _list[low] and search_for <= _list[high]:
            index = low + int(((float(high - low) / ( _list[high] - _list[low])) * ( search_for - _list[low])))
            if _list[index] == search_for:
                return index
            if _list[index] < search_for:
                low = index + 1
            else:
                high = index - 1
        return -1

def main():
    s = Search()
    import sorting_algorithms
    from sorting_algorithms import Sort
    list1 = [19, 2, 31, 45, 6, 11, 121, 27]
    print(s.linear_search(list1, 19))
    print(s.binary_search(list1, 121))
    print(s.jump_search(Sort().merge_sort(list1), 27))  #jump search has to be passed the sorted list
    print(s.fibonacci_search([1,2,3,4,5,6,7,8,9,10,11], 6))
    print(s.exponential_search([1,2,3,4,5,6,7,8,9,10,11], 3))
    print(s.interpolation_search([1,2,3,4,5,6,7,8,9,10,11], 3))
if __name__ == "__main__":
    main()