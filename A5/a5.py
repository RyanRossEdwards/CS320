import sys

def main():
    for line in sys.stdin:
        array = ([int(x) for x in line.split()])

        # Manually splitting for efficiency
        # array = []
        # dp1 = []
        # dp2 = []

        # jewels_value = 0
        # maximum = 0
        # number_string = ''

        # for i in range(len(line)):

        #     # For catching the last item (i.e. end of file)
        #     if i == len(line)-1:
        #         number_string += line[i]

        #     if line[i] == ' ' or line[i] == '\n' or i == len(line)-1:
        #         number = int(number_string)
        #         array += [number]
        #         dp1 += [number]
        #         dp2 += [number]

        #         jewels_value += number

        #         if number > maximum: maximum = number

        #         number_string = ''

        #     else:
        #         number_string += line[i]

        # kings_daughter1 = maxSum(array, dp1, dp2)
        # kings_daughter2 = jewels_value - kings_daughter1

        # print(kings_daughter1, kings_daughter2)


        # Case for no necklaces
        if len(array) == 0:
            print(0, 0)

        # Case for 1 necklace - first daughter gets it
        elif len(array) == 1:
            print(array[0], 0)

        # Case for 2 necklaces - first gets most valuable
        elif len(array) == 2:
            kings_daughter1 = max(array)
            kings_daughter2 = sum(array) - kings_daughter1
            print(kings_daughter1, kings_daughter2)

        # Case for 3 or more necklaces
        else:
            kings_daughter1 = maxSum4(array)
            kings_daughter2 = sum(array) - kings_daughter1

            print(kings_daughter1, kings_daughter2)


def maxSum(array, dp1, dp2):

    for i in range(2, len(array)-1):

        for j in range(0, i-1):

            if dp1[i] < dp1[j] + array[i]:
                dp1[i] = dp1[j] + array[i]


    for i in range(3, len(array)):

        for j in range(1, i-1):

            if dp2[i] < dp2[j] + array[i]:
                dp2[i] = dp2[j] + array[i]


    return max(max(dp1), max(dp2))

    
# Faster - only iterates thorugh for loops once
def maxSum2(array, dp1, dp2):

    dp1i_start = 2
    dp2i_start = 3

    dp1i_end = len(array)-1
    dp2i_end = len(array)

    dp1j_start = 0
    dp2j_start = 1

    # dp1 and dp2 both end at i-1

    for i in range(2, len(array)):

        for j in range(0, i-1):

            if dp1[i] < dp1[j] + array[i] and i >= dp1i_start and i < dp1i_end and j >= dp1j_start:
                dp1[i] = dp1[j] + array[i]

            if dp2[i] < dp2[j] + array[i] and i >= dp2i_start and i < dp2i_end and j >= dp2j_start:
                dp2[i] = dp2[j] + array[i]

    return max(max(dp1), max(dp2))


# Faster - calculates max on the fly
def maxSum3(array, dp1, dp2, maximum):

    dp1i_start = 2
    dp2i_start = 3

    dp1i_end = len(array)-1
    dp2i_end = len(array)

    dp1j_start = 0
    dp2j_start = 1

    # dp1 and dp2 both end at i-1

    for i in range(2, len(array)):

        for j in range(0, i-1):

            if dp1[i] < dp1[j] + array[i] and i >= dp1i_start and i < dp1i_end and j >= dp1j_start:
                dp1[i] = dp1[j] + array[i]

            if dp2[i] < dp2[j] + array[i] and i >= dp2i_start and i < dp2i_end and j >= dp2j_start:
                dp2[i] = dp2[j] + array[i]

            if dp1[i] > maximum: maximum = dp1[i]
            if dp2[i] > maximum: maximum = dp2[i]

    return maximum


def maxSum4(array):

    # For putting them into a single for loop
    dp1i_start = 2
    dp2i_start = 3

    dp1i_end = len(array)-1
    dp2i_end = len(array)

    dp1j_start = 0
    dp2j_start = 1

    # For implementing the algorithm

    dp1 = [0 * i for i in range(len(array))]
    dp2 = [0 * i for i in range(len(array))]

    dp1[0] = array[0]
    dp1[1] = max(array[1], dp1[0])

    dp2[1] = array[1]
    dp2[2] = max(array[2], dp2[1])

    # note: dp1 and dp2 both end at i-1

    for i in range(2, len(array)):

        if i >= dp1i_start and i < dp1i_end:
            if dp1[i-1] < dp1[i-2] + array[i]:
                dp1[i] = dp1[i-2] + array[i]
            else:
                dp1[i] = dp1[i-1]

        if i >= dp2i_start and i < dp2i_end:
            if dp2[i-1] < dp2[i-2] + array[i]:
                dp2[i] = dp2[i-2] + array[i]
            else:
                dp2[i] = dp2[i-1]

    return max(dp1[-2], dp2[-1])


        
main()