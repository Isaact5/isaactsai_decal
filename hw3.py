#1

def computePower(x, y):
    cur = x;
    for i in range(y-1):
        cur*=x
    return cur

#2

def temperatureRange(readings):
    return (min(readings), max(readings))

#3

def isWeekend(day):
    return day == 6 or day == 7

#4

def fuel_efficiency(distance, fuel):
    return round(distance/fuel, 2)

#5

def decodeNumbers(n):
    last_digit = n % 10
    rest = n // 10
    return last_digit * (10 ** len(str(rest))) + rest

#6.1

def find_min_with_for_loop(nums):
    min_num = nums[0]
    for num in nums:
        if num < min_num:
            min_num = num
    return min_num

def find_max_with_for_loops(nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

#6.2

def find_min_with_while_loop(nums):
    min_num = nums[0]
    i = 1
    while i < len(nums):
        if nums[i] < min_num:
            min_num = nums[i]
        i += 1
    return min_num

def find_max_with_while_loops(nums):
    max_num = nums[0]
    i = 1
    while i < len(nums):
        if nums[i] > max_num:
            max_num = nums[i]
        i += 1
    return max_num

#7

def vowel_and_consonant_count(text):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    consonant_count = 0
    
    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return (vowel_count, consonant_count)

#8

def digital_root(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total
