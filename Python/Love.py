func = input('type 1 for heart and 2 for circle\nchoose func:')
string = input('text for func:')
show_range = input('identify string show range(invalid inupt will set to default):')
try:
    show_range = int(show_range)
except ValueError:
    show_range = 30

def direct(func):
    if func == '1':
        call_func(1,string,show_range)
    if func == '2':
        call_func(2,string,show_range)

def call_func(func_initial,string,sr):
    if func_initial == 1:
        print('\n'.join([''.join([(string[(x-y)%len(string)]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ')for x in range(-sr,sr)])for y in range(sr,-sr,-1)]))
    if func_initial == 2:
        print('\n'.join([''.join([(string[(x-y)%len(string)]if (x*0.5)**2+y**2 <= 144 else ' ')for x in range(-sr,sr)])for y in range(sr,-sr,-1)]))


direct(func)
