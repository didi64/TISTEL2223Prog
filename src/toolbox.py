'''
Collection of usefull functions
type 'help(toolbox)' for more help
'''

import ipywidgets as widgets

class OutputWidget(widgets.Output):
    def __init__(self):
        super().__init__(layout = {'border': '1px solid black'})

def is_number(x):
    '''returns True if x is an int or a float'''
    try:
        int(x)
    except ValueError:
        try:
            float(x)
        except ValueError:
            return False
    return True    

def str2number(x):
    '''returns int(x) or float(x) or x'''
    if not is_number(x):
        return x
    try:
        int(x)
    except ValueError:
        return  float(x)
    return int(x)

def sign(x):
    '''returns the sign of the number x'''
    return (x<0 and -1) or (x>0 and 1) or 0
    
def table2str(header, rows, sep = ' │ ', fillchar = ' ', hline_char = '━'):
    '''returns a string displaying a table
    
       header: tuple of column names or numbers, 
       e.g. ('Nr.', 'Name', 'Email')
       rows:  list of tuples of strings or numbers, 
       e.g. [(1, 'Bob', 'foo@bar.ch'), ...]  
    '''   
    def row2str(row, widths, sep, fillchar):
        fstring = (sep+'{}') * len(row) + sep
        args = []
        for s, w in zip(row, widths):
            if type(s) == int or type(s) == float:
                s = str(s).rjust(w, fillchar)
            else:    
                s = str(s).ljust(w, fillchar)
            args.append(s)
   
        return fstring.format(*args)

    def get_widths(header, rows):
        widths = [len(h) for h in header]
        for row in rows:
            for i,item in enumerate(row):
                widths[i] = max(widths[i], len(str(item)))
        return widths                  

    res = []
    widths = get_widths(header, rows)
    hline = ('',) * len(header)
    
    res.append(row2str(header, widths, sep, fillchar))
    res.append(row2str(hline,  widths, sep, fillchar = hline_char))
   
    for row in rows:
        res.append(row2str(row, widths, sep, fillchar))
        
    return '\n'.join(res)       
    
