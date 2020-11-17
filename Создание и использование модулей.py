import argparse
 
 
def get_lines(file):
    try:
        with open(file) as fl:
            return len(fl.readlines())
    except Exception:
        return 0
 
 
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file")
    args = parser.parse_args()
 
    print(get_lines(args.file))
 
 
if __name__ == '__main__':
    main()
