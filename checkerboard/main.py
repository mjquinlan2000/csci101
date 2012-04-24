# Part of the CheckerboardRecursion CSCI 101 Python assignment.
# (C) Keith Hellman 2011
# khellman@mines.edu

import sys
import random
import time

from Tkinter import *

from cbops import *

###
# color management
###
cc, ccindex, ccinc = None, None, None
def resetcolor( ) :
    global cc, ccindex, ccinc
    cc = [0xff, 0x00, 0x00]
    ccindex = 2
    ccinc = +51

def nextcolor( ) :
    global cc, ccindex, ccinc
    if cc[ccindex] in (0x00, 0xff) :
        # switch
        ccindex = ( ccindex + 1 ) % 3
        if cc[ccindex] == 0x00 :
            ccinc = abs(ccinc)
        else :
            ccinc = -abs(ccinc)

    cc[ccindex] = cc[ccindex] + ccinc
    # prevent colors two dark from being used
    while max( cc ) < 0x1f:
        nextcolor( ) 
    return '#%02x%02x%02x' % tuple(cc)

###
# Tk linetags allow us to delete graphical elements from the window stack
###
def linetag( t, u0, u1 ) :
    return "%s-%d-%d-%d-%d" % (t,u0[0],u0[1],u1[0],u1[1])

def tileoutline( cb, precoloredloc ) :
    # draws an outline around an L tile defined by the 2x2 cb and the 
    # square that is pre-colored.  The pre-colored square is identnified by
    # 0--3
    #   0 2
    #   1 3
    # 
    # the vertical lines for the 2x2 checkerboard fit into a 2x3 array
    # the horizontal lines fit into a 3x2 array
    # first we encode the coords of all twelve possible lines, and then 
    # based on the pre-colored square we nullify the 4 lines that should not be 
    # drawn (two outer lines, two inner lines).
    #
    # finally, the remaining lines are drawn
    
    R = cb[0][0][0]
    C = cb[0][0][1]
    vlines = [ [], [], ]
    for r in range(2) :
        for c in range(3) :
            vlines[r].append( (C+c,R+r,C+c,R+r+1) )
    hlines = [ [], [], [] ]
    for r in range(3) :
        for c in range(2) :
            hlines[r].append( (C+c,R+r,C+c+1,R+r) )

    # "nullify" the lines we don't need 
    if precoloredloc == 0 :
        # upper left sq was pre-colored
        vlines[0][0] = None  # outers
        hlines[0][0] = None
        # inners
        vlines[1][1] = None
        hlines[1][1] = None
    elif precoloredloc == 1 :
        # upper right sq was pre-colored
        vlines[1][0] = None  # outers
        hlines[2][0] = None
        # inners
        vlines[0][1] = None
        hlines[1][1] = None
    elif precoloredloc == 2 :
        # lower left sq was pre-colored
        vlines[0][2] = None  # outers
        hlines[0][1] = None
        # inners
        vlines[1][1] = None
        hlines[1][0] = None
    elif precoloredloc == 3 :
        # OK
        # lower right sq was pre-colored
        vlines[1][2] = None  # outers
        hlines[2][1] = None
        # inners
        vlines[0][1] = None
        hlines[1][0] = None

    global cbcanvas, sx, sy
    # draw them
    for r in range(2) :
        for c in range(3) :
            if vlines[r][c] is not None :
                #print "line", vlines[r][c][0], vlines[r][c][1], vlines[r][c][2], vlines[r][c][3]
                create_line( cbcanvas, vlines[r][c][0]*sx, vlines[r][c][1]*sy, 
                        vlines[r][c][2]*sx, vlines[r][c][3]*sy, fill="black" )
    for r in range(3) :
        for c in range(2) :
            if hlines[r][c] is not None :
                #print hlines[r][c][0], hlines[r][c][1], hlines[r][c][2], hlines[r][c][3]
                create_line( cbcanvas, hlines[r][c][0]*sx, hlines[r][c][1]*sy, 
                        hlines[r][c][2]*sx, hlines[r][c][3]*sy, fill="black" )

    # update_idletasks will be called by place tile

def placetile( cb ) :

    global cbcanvas
    global sx, sy
    global delay

    global stopvar     # stop recursion via gui (the Quit button punched)
    if stopvar.get() :
        return 

    if not ( len(cb) == len(cb[0]) == 2 ) :
        raise RuntimeError( "Cannot place tile in a %d x %d checkerboard (must be 2x2)" % \
                (len(cb), len(cb[0]) ) )

    nc = nextcolor()
    precolored = 0
    precoloredloc = None
    for r in range(2) :
        for c in range(2) :
            if cb[r][c][2] != None :
                precolored += 1
                precoloredloc = r+2*c
            else :
                cb[r][c][2] = nc
                drawsq( cb[r][c], cbcanvas, sx, sy )
    
    if  precolored != 1 : 
        raise RuntimeError( "The number of missing or pre-colored squares in the 2x2 checkerboard is not 1."
                #"\n%s." % str(cb)
            )

    tileoutline( cb, precoloredloc )

    update_idletasks( cbcanvas )
    delaymsecs( delay, 1, 1000. )
    global root
    root.update()


def divideboard( cb, returnOrder ) :

    global stopvar     # stop recursion via gui
    if stopvar.get() :
        x = [[None,None],[None,None]]  # 2 x 2
        return x, x, x, x


    l = len(cb[0])

    if l <= 2 : 
        raise RuntimeError( "The 2x2 checkerboards cannot be divided." )

    m = l/2

    # quad w/ missing sq (0=ul, 1=ur, 2=lr, 3=ll)
    missingsq = None
    # upper left
    ul = [ ]
    for r in range(m) :
        ul.append( [] )
        for c in range(m) :
            ul[r].append(cb[r][c])
            if cb[r][c][2] is not None :
                missingsq = 0
    # upper right
    ur = [ ]
    for r in range(m) :
        ur.append( [] )
        for c in range(m,l) :
            ur[r].append(cb[r][c])
            if cb[r][c][2] is not None :
                missingsq = 1
    # lower right
    lr = [  ]
    for r in range(m,l) :
        lr.append( [] )
        for c in range(m,l) :
            lr[r-m].append(cb[r][c])
            if cb[r][c][2] is not None :
                missingsq = 2
    # lower left
    ll = [ ]
    for r in range(m,l) :
        ll.append( [] )
        for c in range(m) :
            ll[r-m].append(cb[r][c])
            if cb[r][c][2] is not None :
                missingsq = 3

    nc = nextcolor()
    if missingsq != 0 :
        ul[m-1][m-1][2] = nc
    if missingsq != 1 :
        ur[m-1][0][2] = nc
    if missingsq != 2 :
        lr[0][0][2] = nc
    if missingsq != 3 :
        ll[0][m-1][2] = nc


    global cbcanvas, sx, sy, delay
    # remove any "lower" divider lines...
    removedividerlines( cbcanvas, len(ul)+1 )

    # draw divider lines
    if len(ul) >= 1 :
        # horizontal
        create_line( cbcanvas, ll[0][0][1]*sx, ll[0][0][0]*sy, (ll[0][0][1]+2*len(ll))*sx, ll[0][0][0]*sy, 
                width=2, fill='black', tag='q-%d'%len(ul) )
        # vertical
        create_line( cbcanvas, ur[0][0][1]*sx, ur[0][0][0]*sy, ur[0][0][1]*sx, (ur[0][0][0]+2*len(ur))*sy, 
                width=2, fill='black', tag='q-%d'%len(ul) )

    drawsq( ul[m-1][m-1], cbcanvas, sx, sy )
    drawsq( ur[m-1][0], cbcanvas, sx, sy )
    drawsq( lr[0][0], cbcanvas, sx, sy )
    drawsq( ll[0][m-1], cbcanvas, sx, sy )
    # trick -- you don't have to draw the outline of this title, because
    # it will be *bordered* by other tiles!

    update_idletasks( cbcanvas )
    delaymsecs( delay, 1, 1000. )

    quads = [ ul, ur, lr, ll ]
    if returnOrder == 'clockwise' :
        return quads
    elif returnOrder == 'relative' :
        mq = quads[missingsq:] + quads[0:missingsq]
    else :
        raise RuntimeError( "Second argument to divideboard must be either 'clockwise' or 'relative'" )

    return mq

def drawsq( sq, canvas, sizex, sizey ) :

    # background colors for checkerboard
    green = '#9db86b'
    brown = '#b8920a'
    clrs = [ green, brown, green ]

    clr = sq[2]
    if clr is None :
        clr = clrs[sq[0]%2+sq[1]%2] 
    elif clr is 0 :
        clr = "black"
    create_rectangle( cbcanvas, sq[1]*sizex, sq[0]*sizey, (sq[1]+1)*sizex, (sq[0]+1)*sizey,
            fill=clr, outline=clr )


def drawcb( cb, canvas ) :
    global sx, sy
    ix = len(cb[0])
    iy = len(cb)
    for r in range(iy) :
        for c in range(ix) :
            drawsq( cb[r][c], canvas, sx, sy )


def Run() :

    global cbcanvas, sx, sy

    # update n
    global nvar
    try :
        n = nvar.get() or 0
    except :
        # bad value in ninput
        n = 0
    if n <= 0 :
        n = 1
    nvar.set(n)

    # update seed
    global seedvar, newseedvar 
    try :
        seed = seedvar.get() or 0
    except :
        seed = 0
    if seed <= 0 or newseedvar.get() :
        newseedvar.set(1)
        seed = int((time.time() % 1)*10000+1) 
    setseed( seedvar, seed )

    # update delay
    global delay, delayvar
    try :
        delay = delayvar.get() or 0
    except :
        delay = 0
    if delay < 0 :
        delay = 200
    delayvar.set( delay )

    cols = 2**(2**n)
    rows = 2**(2**n)
    sx = pwidth // cols
    sy = pheight // rows

    cb = [ [ [] for y in range(cols) ] for x in range(rows) ] 
    for r in range(rows) :
        for c in range(cols) :
            cb[r][c] = [r,c,None]
    # knock a checker out of the checkerboard
    cb[random.randrange(rows)][random.randrange(cols)][2] = 0

    resetcolor()

    global root
    root.focus_set()

    global quitbuttontext, quitbutton, stopvar
    global seedinput, ninput, newseedinput, delayinput 
    global Abutton, Bbutton, Cbutton, Dbutton, runbutton

    for inp in ( seedinput, ninput, newseedinput, delayinput,
            Abutton, Bbutton, Cbutton, Dbutton, runbutton ) :
        inp.config( state=DISABLED )

    quitbuttontext.set("Stop")
    quitbutton.config( command=lambda : stopvar.set(True) )
    stopvar.set( False )  # and we are off!

    beginlog( "begin primitives recording for replay\n" )

    drawcb( cb, cbcanvas )
    update_idletasks( cbcanvas )
    if not stopvar.get() :
        delaymsecs( delay, 1, 100. )

    global checkerboard
    try :
        checkerboard( cb )
        # remove divider lines
        removedividerlines( cbcanvas, len(cb) )

    except Exception, e:
        if str(e) != "Stop" :
            import tkMessageBox
            tkMessageBox.showerror( "Error!", str(e) )
            
    endlog( "end primitives recording for replay\n" )

    for inp in ( seedinput, ninput, newseedinput, delayinput,
            Abutton, Bbutton, Cbutton, Dbutton, runbutton ) :
        inp.config( state=NORMAL )

    quitbuttontext.set("Quit")
    quitbutton.config( command=Quit )

def Replay( logname ) :

    global cbcanvas

    # update delay
    global delay, delayvar
    try :
        delay = delayvar.get() or 0
    except :
        delay = 0
    if delay < 0 :
        delay = 200
    delayvar.set( delay )

    global root
    root.focus_set()

    global quitbuttontext, quitbutton, stopvar
    global seedinput, ninput, newseedinput, delayinput 
    global Abutton, Bbutton, Cbutton, Dbutton, runbutton

    for inp in ( seedinput, ninput, newseedinput, delayinput,
            Abutton, Bbutton, Cbutton, Dbutton, runbutton ) :
        inp.config( state=DISABLED )

    quitbuttontext.set("Stop")
    quitbutton.config( command=lambda : stopvar.set(True) )
    stopvar.set( False )  # and we are off!

    try :
        # each replay will set the seed to whatever was used for its generation
        newseedvar.set(0)
        replaylog( file( logname ), cbcanvas, delay, stopvar, seedvar, root )
    except Exception, e :
        if str(e) != "Stop" :
            import tkMessageBox
            tkMessageBox.showerror( "Error!", str(e) )
 
    for inp in ( seedinput, ninput, newseedinput, delayinput,
            Abutton, Bbutton, Cbutton, Dbutton, runbutton ) :
        inp.config( state=NORMAL )

    quitbuttontext.set("Quit")
    quitbutton.config( command=Quit )




delay = 200
pwidth = 512      # pixel width and height
pheight = 512
sx, sy = None, None  

root = Tk()
root.title( "CSCI101 Checkerboard Recursion" )
root.bind( 'q', lambda x: sys.exit(0) )
root.bind( 'Q', lambda x: sys.exit(0) )
root.bind( 'r', lambda x: Run() )
root.bind( 'R', lambda x: Run() )

# main toolbar
tbar = Frame( root, borderwidth=2, relief="raised" )

# ... run button
runbutton = Button( tbar, text="Run", command=Run )
runbutton.pack( side=LEFT, padx=2, pady=2, fill=X )

# ... quit button
def Quit() :
    sys.exit(0)
stopvar = BooleanVar()
stopvar.set(True)
quitbuttontext = StringVar()
quitbuttontext.set("Quit")
quitbutton = Button( tbar, textvariable=quitbuttontext, command=Quit )
quitbutton.pack( side=RIGHT, padx=2, pady=2 )

delayframe = Frame(tbar, padx=4 )
delaylabel = Label(delayframe, text="Delay (msec)")
delaylabel.pack(side=LEFT)
delayvar = IntVar()
delayvar.set(delay)
delayinput = Entry(delayframe, width=5, textvariable=delayvar)
delayinput.pack(side=LEFT)
delayframe.pack(side=RIGHT)

newseedframe = Frame(tbar, padx=4 )
newseedvar = BooleanVar()
newseedvar.set(not sys.argv>2)
newseedinput = Checkbutton(newseedframe, text="New Seed", var=newseedvar)
newseedinput.pack(side=LEFT)
newseedframe.pack(side=RIGHT)

seedframe = Frame(tbar, padx=4 )
seedlabel = Label(seedframe, text="Seed")
seedlabel.pack(side=LEFT)
seedvar = IntVar()
seedvar.set( int(sys.argv[2]) if len(sys.argv)>2 else 0 )
seedinput = Entry(seedframe, width=5, textvariable=seedvar)
seedinput.pack(side=LEFT)
seedframe.pack(side=RIGHT)

nframe = Frame(tbar, padx=4 )
nlabel = Label(nframe, text="n")
nlabel.pack(side=LEFT)
nvar = IntVar()
nvar.set(int(sys.argv[1]) if len(sys.argv)>1 else 2)
ninput = Entry(nframe, width=5, textvariable=nvar)
ninput.pack(side=LEFT)
nframe.pack(side=RIGHT)

tbar.pack(side=TOP, fill=X)

# challenge question toolbar
cbar = Frame( root, borderwidth=2, relief="raised" )
# challenge0
Abutton = Button( cbar, text="Challenge A", command=lambda : Replay( "A.lis" ) )
Abutton.pack( side=LEFT, padx=2, pady=2, fill=X )
Bbutton = Button( cbar, text="Challenge B", command=lambda : Replay( "B.lis" ) )
Bbutton.pack( side=LEFT, padx=2, pady=2, fill=X )
Cbutton = Button( cbar, text="Challenge C", command=lambda : Replay( "C.lis" ) )
Cbutton.pack( side=LEFT, padx=2, pady=2, fill=X )

idwarnings = 0
def ImpossibleD() :
    import tkMessageBox
    global idwarnings
    if idwarnings < 3 :
        tkMessageBox.showwarning( "Wait...", "Challenge D is\nNOT part of the assignment.\n\n" 
            "You are welcome to complete a checkerboard()\n" 
            "function that will work for this recursion pattern.\nDoing so earns you bragging rights, and perhaps that "
            "sinking feeling when you've spent too much time not *NOT* working on real assignments for other classes.\n\n"
            "Have fun.\n\n"
            "BTW:  You may have to study the replay to see how the recursion pattern is non-trivial, "
            "and you shouldn't have to alter the number of parameters provided to checkerboard, OR ANY other (non-checkerboard) "
            "parts of the code to reproduce the recursion pattern for D." )
        idwarnings += 1
    Replay( "D.lis" )

Dbutton = Button( cbar, text="Impossible D?", command=ImpossibleD )
Dbutton.pack( side=RIGHT, padx=2, pady=2, fill=X )
cbar.pack(side=TOP, fill=X)

cbcanvas = Canvas( root, width=pwidth, height=pheight )
cbcanvas.pack(side=TOP)

checkerboard = lambda : 0
def Main(f) :
    global checkerboard, root
    checkerboard=f
    root.mainloop()

