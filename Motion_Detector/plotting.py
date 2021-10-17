# Run motiondetector.py and import dataframe of motion detection data
from motiondetector import df

from bokeh.plotting import figure, show, output_file

# Create figure object
p=figure(x_axis_type='datetime', height=300, width=500, title='Motion Graph')
p.yaxis.minor_tick_line_color=None

# Create quadrants for plot
q = p.quad(left=df['Start'],right=df['End'],bottom=0,top=1,color='green')

output_file("Graph.html")
show(p)