'''
solutions variadic functions
'''

def add(*args, **units):
    fs = '{:8.2f} {}'
    baseunit = units['baseunit']
    
    values_in_baseunits = [val * units[unit] for val, unit in args]
    for val in values_in_baseunits:
        print(fs.format(val, baseunit))
        
    print('=' * 10)
    print(fs.format(sum(values_in_baseunits), baseunit))