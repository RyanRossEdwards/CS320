import sys

def main():
    firstLine = True
    for line in sys.stdin:
        # Skips the first line of input as meaningless
        # This won't work for numbers with more than 1 digit
        # if len(line) == 2:
            # continue

        # Skips the first line of input as meaningless
        if firstLine:
            firstLine = False
            continue

        # array = ([int(x) for x in line.split()])
        # print(array)
        
        # Manually processing the input for time efficiency
        array = []
        i = 0
        try:
            sn, fn = '', ''
            isSn = True

            while True:
                # Numbers seperated by ' '
                if line[i] == ' ':
                    if isSn:
                        isSn = False
                    else:
                        isSn = True
                        # To improve overall time efficiency
                        # a heap / sorting algorithm should get
                        # added here directly
                        array += [[int(sn), int(fn)]]
                        sn, fn = '', ''

                elif isSn:
                    sn += line[i]
                else:
                    fn += line[i]

                i += 1

        # This means it's at the end of the line
        except IndexError:
            # Last needs to be added
            array += [[int(sn), int(fn)]]

            print(array)
            start_first = sorted(array, key=lambda x: x[0])
            end_first = sorted(array, key=lambda x: x[1])
            print(start_first)
            print(end_first)

            print('Problem 3:')
            problem3(start_first)
            print()


def problem3(array):
    max_union = 0
    new_union = True
    union = 0

    for i in range(len(array)):
        sn, fn = array[i][0], array[i][1]
        if new_union:
            su, fu = sn, fn
            new_union = False
        # Overlap
        elif sn <= fu and fn > fu:
            fu = fn
        # No Overlap
        elif sn > fu:
            union = fu - su
            if union > max_union:
                max_union = union
            su, fu = sn, fn

        if i == len(array)-1:
            union = fu - su
            if union > max_union:
                max_union = union

        print(i, '-', sn, fn, su, fu, union)

    print(max_union)

















main()