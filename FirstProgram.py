def is_valid(num, min_sum, max_sum):
    digits_str = str(num)
    
    # Check for zero digits
    if '0' in digits_str:
        return False
    
    digits = list(map(int, digits_str))
    
    # Check divisibility by each digit
    for d in digits:
        if num % d != 0:
            return False
    
    # Check digit sum range
    s = sum(digits)
    if s < min_sum or s > max_sum:
        return False
    
    # Check reversed divisibility
    rev_num = int(digits_str[::-1])
    rev_digits = list(map(int, str(rev_num)))
    for d in rev_digits:
        if d == 0 or rev_num % d != 0:
            return False
    
    return True

# Input
L, R = map(int, input().split())
minSum, maxSum = map(int, input().split())

valid_numbers = []

for num in range(L, R+1):
    if is_valid(num, minSum, maxSum):
        valid_numbers.append(num)

count = len(valid_numbers)
total_sum = sum(valid_numbers)
average = total_sum / count if count > 0 else 0

# Output
print(count)
print(total_sum)
print(f"{average:.2f}")