def TARGET_TEMP(days, temperatures):
    max_sum = 0
    current_sum = 0
    index = 0
    start = 0  # start index of subarray with maximum sum
    end = 0  # end index of subarray with maximum sum
    

    # Special case if every element in temperatures array is negative
    if len(days) == len(temperatures): # checks for length of arrays
        isallnegative = all(temp <= 0 for temp in temperatures) 
        if isallnegative:
            min_temp_abs = float('inf')
            for i in range(len(temperatures)):
                temp = temperatures[i]
                if abs(temp) < min_temp_abs: # find the largest negative number
                    min_temp_abs = abs(temp)
                    target_start = i
                    target_end = i 
            return days[target_start], days[target_end]


        while index < len(days):
                current_sum += temperatures[index]

                if current_sum <= 0:
                    current_sum = 0
                    start = index + 1

                if current_sum > max_sum:
                    max_sum = current_sum
                    end = index

                index += 1 

        target_start = days[start]
        target_end = days[end]      
    else:
        print("Not the same lengths")

    return target_start, target_end



# Example runs 
print(TARGET_TEMP([22, 23, 24, 25, 26], [9, 2, 3, 11, 4]) )
print(TARGET_TEMP([34, 35, 36, 37, 38], [-1, -3, 7, 4, 2]) )
print(TARGET_TEMP([1, 2, 3, 4, 5], [5, -2, 3, 8, -4]))
print(TARGET_TEMP([1, 2, 3, 4, 5], [-3, -2, 3, 8, -4]))
print(TARGET_TEMP([1, 2, 3, 4, 5], [-3, -2, -4, -8, -4]))
print(TARGET_TEMP([1, 2, 3, 4, 5], [-11, 0, 0, -8, -4]))
print(TARGET_TEMP([1, 2, 3, 4, 5], [-11, -4, -2, -1, -4]))
print(TARGET_TEMP([1, 2, 3, 4, 5], [-11, -4, -3, -2, -1]))