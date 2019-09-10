import sys

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
            end_first = sorted(array, key=lambda x: x[1])

            # Solve problem 1
            problem1(end_first)


def problem1(array):
    schedule = []

    for i in range(len(array)):
        sn, fn = array[i][0], array[i][1]

        if schedule == [] or sn > schedule[len(schedule) - 1]:
            schedule += [fn]

    print(len(schedule))

main()