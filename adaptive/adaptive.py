#!/usr/bin/env python
###
# Utility functions for adaptive dictionary compression assignment.
#
# See pages 59--60 of chapter 1, and questions 47--49 on pages 70--71
# (11th edition, Brookshear, Computer Science an Overview.
###

###
# Create (and return) a list representing an initial compression dictionary.
# The resulting list uses the index of each list element as the compression
# code (0--9).
#
# Add new entries to the dictionary with .append(word).
#
# The single argument should be a string of lowercase letters, and a single 
# capital S, representing the space character.
###
def createDictionary( initData ) :
    theDictionary = []
    for c in initData :
        if c == 'S' :
            theDictionary.append( ' ' )
        else :
            theDictionary.append( c )
    return theDictionary

###
# This function prompts the user for input and displays the compression 
# dictionary to the user.
#
# The function takes no arguments.
###
def getInitialDictionary() :
    init = raw_input( "Enter a sequence of characters for the initial dictionary.\nThe sequence should consist of lowercase letters\nand a single capital S for the space character: " )
    newDictionary = createDictionary( init )
    print "Initial dictionary:",
    for i in range(len(newDictionary)) :
        c = newDictionary[i]
        if c == ' ' :
            c = '[SPACE]'
        print "%d=%s" % ( i, c ),
    # terminate the output line
    print 

    return newDictionary

###
# The inflate function is the reverse of deflate (compression).  It takes
# a list of the integer codes resulting from compression (the deflate routine), and 
# an initial dictionary (which must be the same for both compression and decompression).
#
# inflate returns a list of words and space characters, and the final dictionary after
# decompression is finished.
###
def inflate( codes, dictionary ) :
    # we are continually building the last word till
    # we hit the code for a space, lastword begins as an "empty" string.
    lastword = ""
    # words will hold the words (and spaces) resulting from decompression
    words = []
    for c in codes :

		print
		print dictionary

		# provide a descriptive error message on a common error in compression
		if len(dictionary) <= c :
			print "\n\n\n----------------------------------------------------------------------------"
			print "Uh-oh.  The compression codes say use the word for code %d" % c
			print "but the DE-compression dictionary has codes only up to %d right now!" % (len(dictionary)-1,)
			print
			print "Did you forget to output a newly discovered word as its primitive elements"
			print "the first time it is encountered?"
			print "----------------------------------------------------------------------------\n\n\n"
			# no use in continuing
			return words, dictionary

		if dictionary[c] == ' ' :
			# the end of a word, append it to the output
			words.append( lastword )
			# ... was it in the dictionary?
			if lastword not in dictionary :
				# then we must add it now
				dictionary.append( lastword )
			# and begin building a new lastword
			lastword = ""

			# Don't forget to emit the whitespace that has triggered this 'lastword logic.'
			words.append( dictionary[c] )
		else :
			# add the character for this code to the current lastword we are building
			lastword = lastword + dictionary[c]
    
    # account for the last word not terminated with a space
    if len( lastword ) > 0 :
        words.append(lastword)

    return words, dictionary


def Main( studentsDeflate ) :
    # get a dictionary from the user
    dictionary = getInitialDictionary()

    # get the text to compress
    data = raw_input( "Enter a sequence 'words' (compatible with the initial dictionary) for compression: " )

    # break the original text into space delimited words (the input MUST have
    # only whitespace, no tabs or newlines).
    original_words = data.split()
    # this drops more than one whitespace in a row and removes leading and trailing whitespace.
    # use 
    #   >>> help("".join) 
    # to read up on what .join does, then experiment in the console if you are intrigued.
    inputwords = " ".join( original_words )  

    # call the students deflate function
    codes, deflateD = studentsDeflate( original_words, list(dictionary) )

    # convert the integer codes to a string of digits so the output is easily
    # read and compared to the printed text...  map() and list comprehensions rock (IMHO).
    codedigits = "".join( map( str, codes ) )

    print "  Compressed:", codedigits
    print "  Compression dictionary (final):", deflateD

    # now the reverse process, decompress the result from studentsDeflate
    words, inflateD = inflate( codes, list(dictionary) )

    print "    Original:", inputwords
    print "Decompressed:", "".join( words )
    print "Decompression dictionary (final):", inflateD

    # display results to the Python console
    if inflateD != deflateD :
        print "Yikes, the final dictionaries do not compare well..."

    # we took the whitespace *out* to make deflate easier, but now we must put
    # them back in to make proper comparisons against the output of inflate...
    for i in range(len(original_words),0,-1) :
        original_words.insert(i,' ')

    if original_words == words :
        print "Results Agree! Wonderous compression :) "
        print "Let's compare the lengths: "
        print "Input:", len(inputwords), "vs", "Output:", len(codedigits)
    else :
        print ":-( Broken compression..."
        print " INPUT", original_words
        print "OUTPUT", words

    # fini
