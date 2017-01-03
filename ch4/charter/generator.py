""" view created image in GNOME via eog (eye of gnome) default image viewer
http://superuser.com/questions/104599/how-can-i-launch-the-gnome-image-viewer-from-the-terminal
"""

from PIL import Image, ImageDraw
from .renderers import (title,x_axis,y_axis,bar_series,line_series)
from .constants import *


def generate_chart(chart, filename):
  image = Image.new("RGB",(CHART_WIDTH, CHART_HEIGHT),"#ffffff") #ffffff= white
  drawer = ImageDraw.Draw(image)

  title.draw(chart,drawer)
  x_axis.draw(chart,drawer)
  y_axis.draw(chart,drawer)
  if chart['series_type'] == "bar":
    bar_series.draw(chart,drawer)
  elif char['series_type'] == "line":
    line_series.draw(chart,drawer)

  image.save(filename,format="png")

if __name__ == "__main__":
  generate_chart("bogus","bogus")
