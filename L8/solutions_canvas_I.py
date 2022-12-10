'''
Loesungen zum Notebook
Canvas_I.ipynb
'''

def get_canvas_config(canvas):
    keys = ['line_width', 'stroke_style', 'fill_style']
    return {key: getattr(canvas, key) for key in keys}

def set_canvas_config(canvas, kwargs):
    keys = ['line_width', 'stroke_style', 'fill_style']
    for key in keys:
        if key in kwargs:
            setattr(canvas, key, kwargs[key])        

def draw_line(canvas, pts, **kwargs):
    '''draws a line on canvas through the points in the list points
    
       pts: list of points [(10,20), ...(100,100)]
    '''   
    cfg = get_canvas_config(canvas)
    
    set_canvas_config(canvas, kwargs)
    canvas.stroke_lines(pts)
    
    set_canvas_config(canvas, cfg)
    
def draw_points(canvas, pts, r=2, **kwargs):
    '''draws the points in the list pts on the canvas
    
       r: radius of point
       pts: list of points [(10,20), ...(100,100)]
    '''   
    cfg = get_canvas_config(canvas)
    
    set_canvas_config(canvas, kwargs)
    for x,y in pts:
        canvas.fill_circle(x, y, r)
        
    set_canvas_config(canvas, cfg)