'''
Collection of usefull functions.
Type 'help(toolbox)' for more help.
'''

def sign(x):
    '''returns the sign of the number x'''
    return (x<0 and -1) or (x>0 and 1) or 0
    
def table2str(header, rows, sep = ' │ ', fillchar = ' ', hline_char = '━'):
    '''returns a string displaying a table
    
       header: tuple[int, float, str], tuple of column names, 
         e.g. ('Nr.', 'Name', 'Email')
       rows: list[tuple[int, float, str]], list of table row entries, 
         e.g. [(1, 'Bob', 'foo@bar.ch'), ...]
    '''   
    
    def row2str(row, widths, sep, fillchar):
        fstring = (sep + '{}') * len(row) + sep
        args = []
        for item, width in zip(row, widths):
            if isinstance(item, (int, float)):
                item = str(item).rjust(width, fillchar)
            else:    
                item = str(item).ljust(width, fillchar)
                
            args.append(item)
   
        return fstring.format(*args)

    def get_widths(header, rows):
        widths = [len(h) for h in header]
        for row in rows:
            for i, item in enumerate(row):
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