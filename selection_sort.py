number = [ 3, 5, 9, 4, 7, 8, 2, 1, 6, 10 ]

def selection_sort(li):
  # loop over list
  for index in range(len(li) - 1):
    # We first assume that the first element is the lowest
    min_index = index

    # loop through the remaining elements
    for cur_pos in range(index + 1, len(li)):
      # update the min_index if a smaller value is found at the current position
      if li[cur_pos] < li[min_index]:
        min_index = cur_pos

    # After finding the lowest item of the unsorted regions, swap with the first unsorted item
    li[index], li[min_index] = li[min_index], li[index]

selection_sort(number)

print(number)