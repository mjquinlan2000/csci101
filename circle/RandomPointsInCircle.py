###
# CSCI101 Assignment:  Monte Carlo creation of Random Points in a Circle
###

import math
import random

# matplotlib is a plotting library for Python, see the gallery page
# at http://matplotlib.sourceforge.net/gallery.html
import matplotlib.pyplot as plt  # a plotting library in Python
import matplotlib.patches as patches

N = input( "Enter the number of points to visualize in the unit circle: " )

# creates a new plot with a title, a red circle, and a square aspect ratio
fig = plt.figure()
subfig = fig.add_subplot(111)
subfig.set_title( 'Random Points in a Circle (n=%d)' % N )
subfig.add_patch( patches.Circle( (0,0), 1, fill=False, edgecolor='red' ) )
subfig.axis('equal')

###
# Students:  complete a loop here that calculates N random points in the 
# unit circle (center at the origin, radius 1) and adds them to the subfig
# with the command:
#
#   subfig.plot( x, y, 'o', color='blue' )
#
# (the 'o' and 'blue' arguments dictate the color and shape of the symbol).
###


# show the data --- this should be run *after* the students code has been
# completed.  Without any student added logic above, all you get is a red
# circle.
fig.show()
fig.waitforbuttonpress()


