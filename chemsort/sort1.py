PREFIXES = []
def init_order():
    """load the prefixes structure"""
    global PREFIXES
    with open('prefixes.txt','r') as fp:
        prefixes = fp.read().split('\n')
    PREFIXES = []
    for p in prefixes:
        # strip of extraneous spaces and convert to lowercase
        PREFIXES.append(p.strip().lower())

    
def chem_compare(x,y):
    """returns a 1 if x "comes before" y, 0 if after"""
    global PREFIXES
    if PREFIXES == []:
        init_order()
    for p in PREFIXES:
        if p == x[0:len(p)]:
            return True
        if p == y[0:len(p)]:
            return False
    return x < y

def significant(x):
    global PREFIXES
    if PREFIXES == []:
        init_order()
    x = x.replace(' ','')
    x = x.lower()
    for p in PREFIXES:
        if p in x:
            x = x.replace(p,'')
    return x
        
    
def chem_compare2(x,y):
    """returns a 1 if x "comes before" y, 0 if after"""
    xs = significant(x)
    ys = significant(y)
    # debugging line below
    # print(x," compare ",y," ==> ",xs,' compare ',ys)
    if xs < ys:
        return True
    return False

def bubbleSort(arr, ascending=True):
    """a traditional ARRAY bubble sort using chem_compare2"""
    # this will have to get more complex when we introduce
    # additional columns/objects to the data structure
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if not ascending:
                if chem_compare2(arr[j], arr[j+1]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                if chem_compare2(arr[j+1], arr[j]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]                
                
                

if __name__ == '__main__':
    
    x = ['DL-Alanine','the','quick','brown','fox','jumped','over','the','lazy','dog','aaron','aarvark',
         'alpha-galactosidase','erythro-dibromide','erythomycin', 'trans-2\'-Bromostyrene',
         'threo-2 3-dibromo-3-phenylpropanoic acid','2,3-Dibromo-3-phenylpropanoic acid']
    xs = significant("trans-2'-Bromostyrene")
    print(x)
    print(sorted(x))
    print("="*40)
    print(x)
    bubbleSort(x)
    print(x)