import sys
from heapq import heappush, heappop

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
        # Very case specific - e.g. errors on empty lines
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
            # Last item needs to be added (no ' ' at end)
            array += [[int(sn), int(fn)]]
            # print(array)

            # Sort the algorithms n log n time
            start_first = sorted(array, key=lambda x: x[0])
            end_first = sorted(array, key=lambda x: x[1])
            print(start_first)
            # print(end_first)

            # Solve the three problems
            print('Problem 1:')
            problem1(end_first)

            print('Problem 2:')
            problem2(start_first)

            print('Problem 3:')
            problem3(start_first)
            print()


def problem1(array):
    schedule = []

    for i in range(len(array)):
        sn, fn = array[i][0], array[i][1]

        if schedule == [] or sn > schedule[len(schedule) - 1]:
            schedule += [fn]

    print(len(schedule))


def problem2(array):
    schedule = []
    heap = []

    # First Case
    sn, fn = array[0][0], array[0][1]
    schedule += [fn]

    for i in range(1, len(array)):
        sn, fn = array[i][0], array[i][1]

        # j = 0

        # try:
        #     while True:
        #         fsmall = heappop(schedule)

        #         if sn > fsmall:
        #             heappush(heap, fn)

        #         else:
        #             heappush(heap, fsmall)



        #         schedule = heap
        #         heap = []

        # # There is no compatible class room
        # # heappop([]) throws IndexError
        # except IndexError:

        # This works as comparisions only need to be
        # made on smallest fn due to properties of
        # being sorted by sn

        fsmall = heappop(schedule)
        if sn > fsmall:
            heappush(schedule, fn)
        else:
            heappush(schedule, fn)
            heappush(schedule, fsmall)

    print(len(schedule))




            




def problem3(array):
    max_union = 0
    new_union = True
    union = 0

    # Can be coded better
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

        # print(i, '-', sn, fn, su, fu, union)

    print(max_union)

















main()