# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first):firt i try every pair where i is less then j then if num[i] +num[j] = target then it will return i and j
    #  
   for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    

def max_profit(prices):
    # Outline: we look throug prices to find the lowest price then we find the profit then find out if it is the biggest prifit 
    if not prices:
        return 0

    lowest = prices[0]
    best = 0

    for price in prices:
        if price < lowest:
            lowest = price

        profit = price - lowest
        if profit > best:
            best = profit

    return best


def max_subarray(nums):
# Outline: Keep a running sum of the current block of numbers then if the running sum goes below 0 drop it and start a new block and at the end return the best sum    current = 0
    best = nums[0]

    for num in nums:
        current = current + num

        if current > best:
            best = current

        if current < 0:
            current = 0

    return best

def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}

    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if len(stack) == 0:
                return False
            last = stack.pop()
            if last != pairs[ch]:
                return False

    return len(stack) == 0


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    pass


if __name__ == "__main__":
    main()
