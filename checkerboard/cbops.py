# Part of the CheckerboardRecursion CSCI 101 Python assignment.
# (C) Keith Hellman 2011
# khellman@mines.edu

"""
Checkerboard graphics operation playback or logging.
"""

import time
import random

# overwrite pre-existing file, otherwise do not record ops
try :
    _logfile = file( "record.lis" )
    _logfile.close()  # it was there, close it and overwrite
    _logfile = file( "record.lis", "w" )
except :
    _logfile = None   # no logging

def beginlog( *s ) :
    global _logfile
    if _logfile :
        _logfile.write( "begin;args=%s\n" % (s,) )

def delaymsecs( delay, n, d ) :
    global _logfile
    # max delay 3s
    time.sleep( min( [ 3, (delay*n)/d ] ) )
    if _logfile :
        _logfile.write( "delaymsecs(delay,*args);args=%s\n" % ( [n,d], ) )

def setseed( seedvar, s ) :
    global _logfile
    seedvar.set(s)
    random.seed(s)
    if _logfile :
        _logfile.write( "setseed(seedvar,*args);args=%s\n" % ( [s,] ) )

def create_line( cnv, x, y, x2, y2, **kw ) :
    global _logfile
    cnv.create_line( x, y, x2, y2, **kw )
    if _logfile :
        _logfile.write( "cnv.create_line(*args,**kw);args=%s;kw=%s\n" % ( [x,y,x2,y2], kw ) )

def create_rectangle( cnv, x, y, x2, y2, **kw ) :
    global _logfile
    cnv.create_rectangle( x, y, x2, y2, **kw )
    if _logfile :
        _logfile.write( "cnv.create_rectangle(*args,**kw);args=%s;kw=%s\n" % ( [x,y,x2,y2], kw ) )

def update_idletasks( cnv ) :
    global _logfile
    cnv.update_idletasks()
    if _logfile :
        _logfile.write( "cnv.update_idletasks()\n" )

def removedividerlines( cnv, lesize ) :
    global _logfile
    if _logfile :
        _logfile.write( "removedividerlines(cnv, *args);args=%s;\n" % ( [ lesize, ], ) )
    for x in range(lesize,1,-1) :
        map( cnv.delete, cnv.find_withtag('q-%d'%x))
    update_idletasks( cnv )

def endlog( *s ) :
    global _logfile
    if _logfile : 
        _logfile.write( "end;args=%s\n\n" % (s,) )

def replaylog( f, cnv, delay, stopvar, seedvar, root ) :
    l = f.readline()
    i = 0
    while len(l) and not stopvar.get() :
        terms = l.split(';')
        if not terms :
            continue
        #print "terms", terms
        if '(' in terms[0] :
            # stored generic procedure
            cxt = {'cnv':cnv, 'delay':delay, 'seedvar':seedvar}
            funcc = compile( terms[0], 'replaylog', 'eval' )  # the function
            if len(terms) > 1 :
                eval( compile( terms[1], 'replaylog', 'exec' ), globals(), cxt )  # the args list
                if len(terms) > 2 :
                    eval( compile( terms[2], 'replaylog', 'exec' ), globals(), cxt )    # the keyword values
            #print cxt
            # run it
            eval( funcc, globals(), cxt )
            if 'delaymsecs' in terms[0] :
                root.update()  # allow Stop evaluation when we pause

        # oh yeah,
        l = f.readline()

