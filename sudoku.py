#This is the Python Essentials 2 LAB 2.5.1.11 Sudoku

def test_a_string(str_to_test):
    # This function checks if the input string contains all digits from 1 to 9
    # Input string must have length = 9
    # Outputs True if the check is ok
    for digit in range(1, 10):
        if not str(digit) in str_to_test:
            return False
    return True

def is_valid_sudoku(sudoku):
    # This function finds all rows, columns and sub-squares in a square 9x9
    # Input is tuple with 9 strings
    # Each string that tuple is must have length = 9
    # Also this function uses test_a_string() function to validate strings
    ### check input
    for row in range(9):
        if not len(sudoku[row]) == 9 \     # check length ow sudoku rows
           or not sudoku[row].isdigit():   # only digits allowed
            print("Error in input")
            return False
    ### check rows
    for row in range(9):                   # iterate over rows in sudoku
        if not test_a_string(sudoku[row]): # send current string for verification
            return False                   # if verification failed -> terminate function
    ### check columns                                      
    for col in range(9):                    # iterate over columns in sudoku
        str_to_test = ""                    # initalize string for verification
        for row in range(9):                # iterate over rows in sudoku
            str_to_test += sudoku[row][col] # and get only one character from current row
        if not test_a_string(str_to_test):  # send current string for verification
            return False                    # if verification failed -> terminate function
    ### check sub-squares
    # let arrange tiles in the folloing order
    # 012
    # 345
    # 678
    for tile in range(9):                               # iterate over tiles in sudoku
        start_row = (tile // 3) * 3                     # from which row starts current tile?
        start_col = (tile % 3) * 3                      # same for columns
        str_to_test = ""                                # initalize string for verification
        for row in range(start_row, start_row + 3):     # iterate over rows from start_row
            str_to_test += sudoku[row][start_col:start_col + 3]# get slice from start_col
        if not test_a_string(str_to_test):              # send current string for verification
            return False                                # if verification failed -> terminate
    return True                                         # if we get here -> all checks are ok
        

def tests():
    # typical function that tries test cases
    print("Self-test ...")
    test_tuples = (("295743861",
                    "431865927",
                    "876192543",
                    "387459216",
                    "612387495",
                    "549216738",
                    "763524189",
                    "928671354",
                    "154938672",
                    ),
                   ("195743862",
                    "431865927",
                    "876192543",
                    "387459216",
                    "612387495",
                    "549216738",
                    "763524189",
                    "928671354",
                    "254938671",))
    test_results = (True,
                    False)
    for test_case_number in range(len(test_tuples)): # iterate over test cases
        tupl = test_tuples[test_case_number]         # get next test case (sudoku)
        for i in range(9):                           # iterate over strings in sudoku
            print(tupl[i])                           # print next string
        result = is_valid_sudoku(tupl)               # launch main algorithm
        print("->", result, end =" ")                # print it's result
        if result == test_results[test_case_number]: # compare it with expected result
                print("Ok")
        else:
                print("Fail")


# Main
if __name__ == "__main__":
    tests()
