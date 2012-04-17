from main import placetile, divideboard, Main

#################################################################################
# Q1: what is the difference in divideboard results depending on whether the 
# second argument is the string 'clockwise' or 'relative'?
#
# Place your answer here, as a Python comment (all lines preceded with a #)
# 
#
#
#
#
#################################################################################

def checkerboard( cb ) :
    if len( cb ) == 2 :
        ###
        # placetile draws a newly colored L shaped tile over the 2x2 checkerboard
        # (the cb argument).
        #
        # placetile will fail if cb is not 2x2, or if cb doesn't have exactly one
        # square that is either covered by a previous tile or the missing square
        # in the puzzle setup.  If placetile fails, it will display an error
        # message saying so.
        ###
        placetile(cb)
    else :
        ###
        # divideboard takes a checkerboard with 2**(2**n), n>0, squares and 
        # chops it up into 4 equal quadrants.  The quadrants are returned as 4
        # values, and stored here into m, n, p, and q.
        #
        # The specific order and relationships between m, n, p, and q are dictated
        # by whether the second argument is 'clockwise' or 'relative'.  We'd 
        # love to say more, but we would be giving away Q1.
        ###
        m, n, p, q = divideboard( cb, 'clockwise' )
        checkerboard( m )
        checkerboard( q )
        checkerboard( p )
        checkerboard( n )


#################################################################################
# Q2: Copy the checkerboard function above to below this comment, and RENAME the 
# function above to cbOriginal (or some such).
#
# Now, in the checkerboard user interface, watch the Challenge A replay and
# change the checkerboard function (the one you just created by copying, NOT
# cbOriginal) so that it reproduces the recursive pattern for Challenge A.
#################################################################################







#################################################################################
# Q3: Again, copy the checkerboard function above to below this comment, and 
# RENAME the function above to just A.
#
# Now, in the checkerboard user interface, watch the Challenge B replay and
# change the checkerboard function (the one you just created by copying, NOT
# cbOriginal or A) so that it reproduces the recursive pattern for Challenge B.
#################################################################################







#################################################################################
# Q4: Finally, copy the checkerboard function above to below this comment, and 
# RENAME the function above to just B.
#
# Now, in the checkerboard user interface, watch the Challenge C replay and
# change the checkerboard function (the one you just created by copying, NOT
# cbOriginal, A, or B) so that it reproduces the recursive pattern for
# Challenge C.
#################################################################################









#################################################################################
# Do not change anything below this line (the application may fail to work)
#################################################################################

Main( checkerboard )

