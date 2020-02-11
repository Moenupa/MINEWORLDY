import pandas as pd
import matplotlib.pyplot as plt
print('---Graphing Machine---')
def func_procs():
    global depth_whole, name
    #input
    while True:
        name = input('Stock Name:\t').upper()
        
        cpn_sep()

    #process data       
        try:
            dataset = pd.read_csv(open('{0}.csv'.format(name))).dropna().loc[:,['Date','Close']]
            break
        except FileNotFoundError:
            continue
    data = dataset['Close'].tolist()
    depth_whole = len(data)
    
    return dataset
def func_show(dataset):
    '''
    '''
    global depth_whole, name
    plt.plot(list(range(depth_whole)), dataset['Close'].tolist(), 'b-', label = 'All Historical {0} Data'.format(name))
    plt.legend(loc = 'best')
    plt.show()
    cpn_sep()
def cpn_sep():
    '''
    Seperate sections
    Input: None
    Output: None
    '''
    print('-'*8)
while True:
    dataset = func_procs()
    print(dataset)
    func_show(dataset)