import os 
def fix_paths(paths):
    '''paths is a list of paths below /home/jovyan/work/TISTEL2223Prog/
       returns relative paths form current working directory
       fix('images/str_methods_1.png') returns
       
       
       Example:
       fix(['images/str_methods_1.png']) returns
         ['../../TISTEL2223Prog/images/str_methods_3.png'] if called from work/notebooks/foo.ipynb
         ['../TISTEL2223Prog/images/str_methods_1.png']    if called from TISTEL2223Prog/L3/foo.ipynb
    '''
    cdw = os.getcwd()[17:]
    return [cdw.count('/') * '../' + 'TISTEL2223Prog/' + path for path in paths]
