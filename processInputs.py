INPUT_DIR_PATH = "inputs/"
SEPARATOR = ","


def get_formatted_input(day):
    path = INPUT_DIR_PATH + f"{str(day)}.txt"
    file = open(path)
    data = []
    for line in file:
        line = line.rstrip()
        if SEPARATOR in line:
            try:
                line = [int(x) for x in line.split(SEPARATOR)]
            except ValueError:
                line = [x for x in line.split(SEPARATOR)]
        else:
            try:
                line = int(line)
            except ValueError:
                pass
        data.append(line)
    if len(data) == 1:
        data = data[0]
    return data
