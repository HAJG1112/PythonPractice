class Sort:
    def bubble_sort(self, list):
    # Swap the elements to arrange in order
        for iter_num in range(len(list)-1,0,-1):
            for idx in range(iter_num):
                if list[idx]>list[idx+1]:
                    temp = list[idx]
                    list[idx] = list[idx+1]
                    list[idx+1] = temp

    def merge_sort(self, unsorted_list):
        if len(unsorted_list) <= 1:
            return unsorted_list
    # Find the middle point and devide it
        middle = len(unsorted_list) // 2
        left_list = unsorted_list[:middle]
        right_list = unsorted_list[middle:]

        left_list = self.merge_sort(left_list)
        right_list = self.merge_sort(right_list)
        return list(self.merge(left_list, right_list))

    # Merge the sorted halves
    def merge(self, left_half, right_half):
        res = []
        while len(left_half) != 0 and len(right_half) != 0: #while both halves are not equal to zero
            if left_half[0] < right_half[0]: #if the left half first value is less than the right half first value append to res 
                res.append(left_half[0])
                left_half.remove(left_half[0]) #remove that same number from left half list
            else:
                res.append(right_half[0])
                right_half.remove(right_half[0])
        if len(left_half) == 0:
            res = res + right_half
        else:
            res = res + left_half
        return res

    def insertion_sort(self, InputList):
        for i in range(1, len(InputList)):
            j = i-1
            nxt_element = InputList[i]
    # Compare the current element with next one
            while (InputList[j] > nxt_element) and (j >= 0): #next value in list is greater than previous and after the 2nd item
                InputList[j+1] = InputList[j]
                j=j-1
            InputList[j+1] = nxt_element

    def shell_sort(self, input_list):
        gap = len(input_list) // 2
        while gap > 0:
            for i in range(gap, len(input_list)):
                temp = input_list[i]
                j = i

    # Sort the sub list for this gap
                while j >= gap and input_list[j - gap] > temp:
                    input_list[j] = input_list[j - gap]
                    j = j-gap
                input_list[j] = temp

    # Reduce the gap for the next element
            gap = gap//2

    def selection_sort(self, input_list):
        for idx in range(len(input_list)):
            min_idx = idx
            for j in range( idx +1, len(input_list)):
                if input_list[min_idx] > input_list[j]:
                    min_idx = j
    # Swap the minimum value with the compared value
            input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]

    def quick_sort(self, _list):
        from random import randint

        if len(_list)< 2:
            return _list

        low, same, high = [], [], []
        pivot = _list[randint(0, len(_list) - 1)]
        for item in _list:
            # Elements that are smaller than the `pivot` go to
            # the `low` list. Elements that are larger than
            # `pivot` go to the `high` list. Elements that are
            # equal to `pivot` go to the `same` list.
            if item<pivot:
                low.append(item)
            elif item==pivot:
                same.append(item)
            elif item>pivot:
                high.append(item)
        
        return self.quick_sort(low) + same + self.quick_sort(high)

    def insertion_sort_tim(self, array, left=0, right=None):
        '''
        Modified insertion sort for the timsort
        '''
        if right is None:
            right = len(array) - 1

        # Loop from the element indicated by
        # `left` until the element indicated by `right`
        for i in range(left + 1, right + 1):
            # This is the element we want to position in its
            # correct place
            key_item = array[i]

            # Initialize the variable that will be used to
            # find the correct position of the element referenced
            # by `key_item`
            j = i - 1

            # Run through the list of items (the left
            # portion of the array) and find the correct position
            # of the element referenced by `key_item`. Do this only
            # if the `key_item` is smaller than its adjacent values.
            while j >= left and array[j] > key_item:
                # Shift the value one position to the left
                # and reposition `j` to point to the next element
                # (from right to left)
                array[j + 1] = array[j]
                j -= 1

            # When you finish shifting the elements, position
            # the `key_item` in its correct location
            array[j + 1] = key_item

        return array

    def tim_sort(self, _list):
        min_run = 32
        n = len(_list)

        # Start by slicing and sorting small portions of the
        # input _list. The size of these slices is defined by
        # your `min_run` size.
        for i in range(0, n, min_run):
            self.insertion_sort_tim(_list, i, min((i + min_run - 1), n - 1))

        # start merging the sorted slices.
        # Start from `min_run`, doubling the size on
        # each iteration until you surpass the length of
        # the _list.
        size = min_run
        while size < n:
            # Determine the _lists that will
            # be merged together
            for start in range(0, n, size * 2):
                # Compute the `midpoint` (where the first _list ends
                # and the second starts) and the `endpoint` (where
                # the second _list ends)
                midpoint = start + size - 1
                end = min((start + size * 2 - 1), (n-1))

                # Merge the two sub_lists.
                # The `left` _list should go from `start` to
                # `midpoint + 1`, while the `right` _list should
                # go from `midpoint + 1` to `end + 1`.
                merged__list = self.merge(
                    left_half=_list[start:midpoint + 1],
                    right_half=_list[midpoint + 1:end + 1])

                # Finally, put the merged _list back into
                # your _list
                _list[start:start + len(merged__list)] = merged__list

            # Each iteration should double the size of your _lists
            size *= 2

        return _list
        
def main():
    import time
    s = Sort()
    bubble_list = [19, 2, 31, 45, 6, 11, 121, 27]
    merg_list = [19, 2, 31, 45, 6, 11, 121, 27]
    insert_list = [19, 2, 31, 45, 6, 11, 121, 27]
    shell_sort = [19, 2, 31, 45, 6, 11, 121, 27]
    select_sort = [19, 2, 31, 45, 6, 11, 121, 27]
    quick_sort = [19, 2, 31, 45, 6, 11, 121, 27]
    tim_sort = [19, 2, 31, 45, 6, 11, 121, 27]

    print('Pre-bubble sort:', bubble_list)
    tic = time.perf_counter()
    s.bubble_sort(bubble_list)
    toc = time.perf_counter()
    time1 = toc - tic
    print(f'Post-bubble sort: {bubble_list} in {time1:0.10f} seconds. Complexity O(n^2)')
    print('\n')

    print('Pre-merge sort:', merg_list)
    tic1 = time.perf_counter()
    merged = s.merge_sort(merg_list)
    toc1 = time.perf_counter()
    time2 = toc1 - tic1
    print(f'Post-merge sort :{merged} in {time2:0.10f} seconds')
    print('\n')

    print('Pre-insert sort',insert_list)
    tic2 = time.perf_counter()
    s.insertion_sort(insert_list)
    toc2 = time.perf_counter()
    time3 = toc2 - tic2
    print(f'Post-insert sort: {insert_list} in {time3:0.10f} seconds. Complexity O(n^2)')
    print('\n')

    print('Pre-shell sort', shell_sort)
    tic3 = time.perf_counter()
    s.shell_sort(shell_sort)
    toc3 = time.perf_counter()
    time4 = toc3 - tic3
    print(f'Post-insert sort: {shell_sort} in {time4:0.10f} seconds')
    print('\n')

    print('Pre-selection Sort', select_sort)
    tic4 = time.perf_counter()
    s.selection_sort(select_sort)
    toc4 = time.perf_counter()
    time5 = toc4 - tic4
    print(f'Post-selection sort: {select_sort} in {time5:0.10f} seconds')
    print('\n')

    print('Pre-quick Sort', quick_sort)
    tic5 = time.perf_counter()
    s.quick_sort(select_sort)
    toc5 = time.perf_counter()
    time6 = toc5 - tic5
    print(f'Post-quick sort: {quick_sort} in {time6:0.10f} seconds')
    print('\n')

    print('Pre-tim Sort', tim_sort)
    tic6 = time.perf_counter()
    s.tim_sort(tim_sort)
    toc6 = time.perf_counter()
    time7 = toc6 - tic6
    print(f'Post-tim sort: {tim_sort} in {time7:0.10f} seconds')

if __name__ == "__main__":
    main()