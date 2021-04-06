number = [ 3, 5, 9, 4, 7, 8, 2, 1, 6, 10 ]

def insertion_sort(li):
  # outer loop walks up the list (green)
  for index in range(len(li)):
    # current number for comparisons
    current_number = li[index]
    # loop to walk down the list -- stops a zero or a smaller number
    cur_pos = index - 1
    while cur_pos >= 0 and current_number < li[cur_pos]:
      # swap the values
      li[cur_pos], li[cur_pos + 1] = li[cur_pos + 1], li[cur_pos]
      cur_pos -= 1
    
insertion_sort(number)

print(number)
