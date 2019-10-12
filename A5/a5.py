import sys

def main():
    for line in sys.stdin:
        # array = ([int(x) for x in line.split()])

        # Manually splitting for efficiency
        array = []
        dp1 = []
        dp2 = []
        jewels_value = 0
        number_string = ''

        endOfFile = False

        for i in range(len(line)):

            # For catching the last item (i.e. end of file)
            if i == len(line)-1:
                number_string += line[i]

            if line[i] == ' ' or line[i] == '\n' or i == len(line)-1:
                number = int(number_string)
                array += [number]
                dp1 += [number]
                dp2 += [number]

                jewels_value += number

                number_string = ''

            else:
                number_string += line[i]

        kings_daughter1 = maxSum(array, dp1, dp2)
        kings_daughter2 = jewels_value - kings_daughter1

        print(kings_daughter1, kings_daughter2)


# To self - using built in max to find max, if it's slow manually implement it
# To self - can combine the for loops for even greater efficiency

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

    




































        
main()