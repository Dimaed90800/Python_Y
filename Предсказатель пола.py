import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--barbie', default=50, type=int)
parser.add_argument('--cars', default=50, type=int)
parser.add_argument('--movie', default='other', type=str)
args = parser.parse_args()
if args.barbie not in range(0, 101):
    args.barbie = 50
if args.cars not in range(0, 101):
    args.cars = 50
if args.movie not in ['melodrama', 'football', 'other']:
    args.movie = 'other'
if args.movie == 'melodrama':
    args.movie = 0
if args.movie == 'football':
    args.movie = 100    
if args.movie == 'other':
    args.movie = 50   
b1 = ((100 - int(args.barbie)) + int(args.cars) + int(args.movie)) // 3
boys = 'boy: ' + str((100 - int(args.barbie) + int(args.cars) +
                     int(args.movie)) // 3)
girls = 'girl: ' + str(100 - b1)
print(boys)
print(girls)