# Your name: Kushal Sanjeev
# Your student id: 46299632
# Your email: kasanj@umich.edu
# List who you worked with on this homework: Ethan Goldstein

#The goal of this homework is to practice basic debugging and get familar with
# Python 3 basics.  It includes work with functions, strings, for-each loop,
# for loop, range, and conditionals

# Fix errors in the function below. It should return a count of the number
# of values greater than the passed target value in the passed list nums
def count_gt(target, nums):
    count = 0
    for num in nums:
        if num > target:
            count += 1
    return count

# Testing the count_gt function
def test_count_gt():
    print("Testing count_lt")
    res = count_gt(3, [0, 1, 2, 3])
    print("Expected: 0, Actual", res)
    res = count_gt(1, [0, 1, 2, 3])
    print("Expected: 2, Actual:", res)
    res = count_gt(2, [0, 1, 2, 3])
    print("Expected: 1, Actual", res)
    res = count_gt(-3, [0, -1, -2, 3])
    print("Expected: 4, Actual", res)
    res = count_gt(10, [])
    print("Expected: 0, Actual:", res)



# Fix errors in the function below.  It should return a total of the values from 0
# to the specified end (inclusive) when counting by 2's (0, 2, 4, etc).
def total_by_twos(end):
    total = 0
    for x in range(0, (int(end)+1), 2):
        total += x
    return total

# Testing the total_by_twos function
def test_total_by_twos():
    print("Testing total_by_twos")
    res = total_by_twos(10)
    print("Expected: 30, Actual:", res)
    res = total_by_twos(0)
    print("Expected: 0, Actual:", res)
    res = total_by_twos(15)
    print("Expected: 56, Actual:", res)
    res = total_by_twos(20)
    print("Expected: 110, Actual:", res)
    res = total_by_twos(25)
    print("Expected: 156, Actual:", res)



# Return true if all the values in num_list are negative (< 0) and false otherwise
def check_all_neg(num_list):
    for num in num_list:
        if num >= 0:
            return False
    return True

# Testing the check_all_neg function
def test_check_all_neg():
    print("Testing check_all_neg")
    res = check_all_neg([1, 2, 3])
    print("Expected: False, Actual:", res)
    res = check_all_neg([1, 3, 0, 2])
    print("Expected: False, Actual:", res)
    res = check_all_neg([-1, -3, -5])
    print("Expected: True, Actual:", res)
    res = check_all_neg([-1, 0, -5])
    print("Expected: False, Actual:", res)
    res = check_all_neg([-2, -20, -5])
    print("Expected: True, Actual:", res)


# Fix the function below to return the index of the maximum value in the list nums
# or -1 if there aren't any values in the list
def get_index_max(nums):

    # init the max and max_index
    max = 0
    max_index = -1

    # loop through the list
    for index in range(len(nums)):

        # get the current value
        current = nums[index]

        # if new max
        if current < max:

            # reset max and max index
            max = current
            max_index = index

    return max_index

# Testing the get_index_max function
def test_get_index_max():
    print("Testing get_index_max")
    res = get_index_max([2, -3, 5])
    print("Expected: 2, Actual:", res)
    res = get_index_max([-2, 3, -5])
    print("Expected: 1, Actual:", res)
    res = get_index_max([1])
    print("Expected: 0, Actual:", res)
    res = get_index_max([89, 20, 14, 4])
    print("Expected: 0, Actual:", res)
    res = get_index_max([])
    print("Expected: -1, Actual:", res)



# Fix the function below to return 3 if score < 100
# return 2 if score >= 100 and less than 150
# return 1 if score >= 150 and less than 180
# return 0 if score >= 180 and less than 200
# else return -1
def get_group(score):
    group = 0
    if score < 100:
        group = 3
    elif score >= 100 and score < 150:
        group = 2
    elif score >= 150 and score < 180:
        group = 1
    elif score >= 180 and score < 200:
        group = 0
    else: 
        group =-1
    return group

# Test the get_group function
def test_get_group():
    print("Testing get_group")
    res = get_group(99)
    print("Expected: 3, Actual:", res)
    res = get_group(100)
    print("Expected: 2, Actual:", res)
    res = get_group(150)
    print("Expected: 1, Actual:", res)
    res = get_group(180)
    print("Expected: 0, Actual:", res)
    res = get_group(200)
    print("Expected: -1, Actual:", res)



# Fix errors in the function below.  It should return a password (string)
# created from the last letter of each word in the passed string
# followed by ! and then the last two digits of the passed year
def create_pass(the_str, year):
    words = the_str.split()
    password = ""
    for word in words:
        password = password + word[-1]
    password = password + "!" + str(year)[-2] + str(year)[-1]
    return password

# Testing the create_pass function
def test_create_pass():
    print("Testing create_pass")
    res = create_pass("Hello world", 2021)
    print("Expected: od!21, Actual:", res)
    res = create_pass("Some one stop me", 2020)
    print("Expected: eepe!20, Actual:", res)
    res = create_pass("Walk", 2019)
    print("Expected: k!19, Actual:", res)
    res = create_pass("Walk 4 Hope", 2019)
    print("Expected: k4e!19, Actual:", res)
    res = create_pass("a b c", 2021)
    print("Expected: abc!21, Actual:", res)

# Extra credit - up to 5 points
# Finish the function below to create and return a new list of strings which matches the
# str_list, except it doesn't include the first and last character in each string
def get_mids(str_list):
    new_lst = []
    for i in str_list:
        new = i[1:-1]
        new_lst.append(new)
    return new_lst

# Testing the get_mids function
def test_get_mids():
    print("Testing get_mids")
    res = get_mids(["walk", "away"])
    print("Expected: ['al', 'wa'], Actual: " + str(res))
    res = get_mids(["hi", "there"])
    print("Expected: ['', 'her'], Actual: " + str(res))
    res = get_mids(["apple"])
    print("Expected: ['ppl], Actual: " + str(res))
    res = get_mids(["one", "two", "three"])
    print("Expected: ['n', 'w', 'hre'], Actual: " + str(res))
    res = get_mids(["yay"])
    print("Expected: ['a'], Actual: " + str(res))



# declare the main method
def main():

    test_count_gt()
    print()
    
    test_total_by_twos()
    print()
    
    test_check_all_neg()
    print()

    test_get_index_max()
    print()

    test_get_group()
    print()
    
    test_create_pass()
    print()
    
    test_get_mids() # remove the first # to test the extra credit


# call the main method
main()
