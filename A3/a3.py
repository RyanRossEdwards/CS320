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
        
        # Manually receiving the input for time efficiency
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
            print(array)




















main()