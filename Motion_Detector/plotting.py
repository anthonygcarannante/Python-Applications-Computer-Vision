# Run motiondetector.py and import dataframe of motion detection data
from motiondetector import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

cds=ColumnDataSource(df)

# Create figure object
p=figure(x_axis_type='datetime', height=200, width=500, title='Motion Graph')
p.yaxis.minor_tick_line_color=None

hover=HoverTool(tooltips=[('Start', '@Start'),('End', '@End')])
p.add_tools(hover)

# Create quadrants for plot
q = p.quad(left='Start',right='End',bottom=0,top=1,color='green',source=cds)

output_file("Graph.html")
show(p)