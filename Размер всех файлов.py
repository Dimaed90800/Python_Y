import os


def human_read_format(size):
    s = 0
    weight = ['Б', 'КБ', 'МБ', 'ГБ']
    if size < 1024:
        return str(size) + weight[0]
    while size >= 1024:
        size = size / 1024
        s += 1
    return str(round(size)) + weight[s]


def get_files_sizes():
    ans = ''
    for i in os.listdir("."):
        if os.path.isfile(i):
            ans += i + ' ' + human_read_format(os.getsize(i)) + '\n'
    return ans