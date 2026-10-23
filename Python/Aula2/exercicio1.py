from datetime import datetime


def process_file(file):
    # open file in text read-only mode
    f = open(file, 'r')

    # limit file-size and file-date
    limit_file_size = 2 * pow(2, 20)
    limit_file_date = datetime(2000, 2, 28)

    # names
    names = []

    # iterate each line
    for line in f:
        # remove newlines
        line = line.strip()

        # slicing line to get data
        owner = line[0:6]
        size = line[6:12].lower()
        date = line[13:24]

        # parsing date
        file_date = datetime.strptime(date, '%d %b %Y')

        # parsing file size
        if 'k' in size:
            file_size = float(size.replace('k', '').strip()) * 1024
        elif 'm' in size:
            file_size = float(size.replace('m', '').strip()) * pow(1024, 2)
        elif 'g' in size:
            file_size = float(size.replace('g', '').strip()) * pow(1024, 3)
        else:
            file_size = int(size.strip())

        if file_size < limit_file_size and file_date < limit_file_date:
            names.append(owner)

    return len(list(set(names)))


print(process_file('C:/Software Splice/Python/files.txt'))