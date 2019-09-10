import sys
from heapq import heappush, heappop

def main():
    firstLine = True
    for line in sys.stdin:

        # Skips the first line of input as meaningless
        if firstLine:
            firstLine = False
            continue
        
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

                        array += [[int(sn), int(fn)]]
                        sn, fn = '', ''

                elif isSn:
                    sn += line[i]
                else:
                    fn += line[i]

                i += 1

        # IndexError indicates end of line
        except IndexError:
            # Last item needs to be added (no ' ' at end)
            array += [[int(sn), int(fn)]]

            # Sort the algorithms n log n time
            start_first = sorted(array, key=lambda x: x[0])

            # Solve problem 1
            problem2(start_first)


def problem2(array):
    schedule = []

    # First Case - fn of first item
    schedule += [array[0][1]]

    for i in range(1, len(array)):
        sn, fn = array[i][0], array[i][1]

        # This works as comparisions only need to be
        # made on smallest fn due to properties of
        # being sorted by sn - did proof on paper

        fsmall = heappop(schedule)
        if sn > fsmall:
            heappush(schedule, fn)
        else:
            heappush(schedule, fn)
            heappush(schedule, fsmall)

    print(len(schedule))

main()