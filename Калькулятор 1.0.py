import sys

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        a = (''.format(sys.argv[1], sys.argv[-1]))
        print(sum(a.split()))
    else:
        print("0")