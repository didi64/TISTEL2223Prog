def run():
    callback('App is running ...')

def set_callback(callback):
    global callback
    callback = callback 
    
callback = print
