import os 
def fix_paths(paths):
    '''paths is a list of paths below /home/jovyan/work/NIA22Prog/
       returns relative paths form current working directory
       fix('images/str_methods_1.png') returns
       
       
       Example:
       fix(['images/str_methods_1.png']) returns
         ['../../NIA22Prog/images/str_methods_3.png'] if called from work/notebooks/foo.ipynb
         ['../NIA22Prog/images/str_methods_1.png']    if called from NIA22Prog/L3/foo.ipynb
    '''
    cdw = os.getcwd()[17:]
    return [cdw.count('/') * '../' + 'NIA22Prog/' + path for path in paths]
