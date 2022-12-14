'''
Collection of usefull functions.
Type 'help(toolbox)' for more help.
'''

def sign(n):
    '''returns the sign of the number n'''
    if n < 0:
        return -1
    elif n > 0:
        return 1
    else:
        return 0      
    
def _print_as_tuple(tp, widths):  
    '''gib tp als Tabellenzeile aus mit Spaltenbreite width'''  
    cols = []
    for item, width in zip(tp, widths):
        s = item.ljust(width)
        cols.append(s)

    s = '|'
    for col in cols:
        s = s + col + '|'
    print(s)    

def _get_widths(header, data_rows):
    '''gibt tuple mit den maximalen Spaltenbreiten 
       von header und data_rows zurueck
    '''   

    widths = [0] * len(header) 
    for row in [header] + data_rows:
        for i, item in enumerate(row):
            new_width = max(widths[i], len(item))
            widths[i] = new_width

    return widths    

def print_as_table(header, data_rows):    
    '''Gib header und data_rows in Tabellenform aus
    
       header: Tuple mit Spaltennamen
       data_rows: Liste von Tupeln mit Spalteneintraegen 
    '''
    col_widths = _get_widths(header, data_rows)
    hline = []
    for width in col_widths:
        hline.append('=' * width)


    rows = [header, hline] + data_rows
    for row in rows:
        _print_as_tuple(row, col_widths)    
