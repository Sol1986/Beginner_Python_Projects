numbers_list = [1, 2, 2, 3, 8, 3, 9, 5, 5]

def calculate_mean():
    mean = (sum(numbers_list))/len(numbers_list)

    print (f"The mean is: {mean:.2f}")

calculate_mean()

def calculate_median():
    sorted_list = sorted(numbers_list)
    n = len(sorted_list)
    mid = n//2 # the index of the middle value


    if n % 2 == 0:
        median = (sorted_list[mid - 1] + sorted_list[mid]) / 2
        print(f"There where two medians, The median is: {median}")
    else:
        median = sorted_list[mid]
        print(f"Only one median, The median is: {median}")


calculate_median()

def calculate_mode():
    freq = {}

    for num in numbers_list:
        freq[num] = numbers_list.count(num)

    max_count = max(freq.values())

    # Find the number with the highest frequency max(dictionary, key=dictionary.get)    
    # mode = max(freq, key=freq.get)

    mode = [number for number,count in freq.items() if count == max_count]
    print(f"The mode is: {mode}") 
  

calculate_mode()