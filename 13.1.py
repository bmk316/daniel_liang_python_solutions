def main():
    while True:
        try:
            filename = input('Enter a filename:').strip()
            filename_open = open(filename, 'r')
            break
        except IOError:
            print('File',filename,'does not exist.Try again')

    string_to_remove = input('Enter string to be removed:')

    list1 = []

    for line in filename_open:
        changed = line.replace(string_to_remove, '')
        list1.append(changed)

    filename_open.close()

    fo = open(filename, 'w')

    for line in list1:
        fo.write(line)

    fo.close()
    print('Done')


main()