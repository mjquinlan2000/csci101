#!/usr/bin/env python
from adaptive import Main


#
# STUDENTS
# ========
# Complete the deflate function below; it should complete the compression logic
# for the adaptive dictionary scheme presented in the textbook.
#




###
# The deflate function takes a list of words to be compressed and the initial
# compression dictionary to use.
#
# WORDS
# =====
# A list of words (as opposed to a sequence of characters where deflate would have
# to LOOK for the word-separating spaces) makes this function must easier to 
# write.  To handle each word in turn, use a loop:
#   
#   for theWord in words :
#      ... do this for each word ...
#
# NOTE:  after the code(s) for each word are added to the codes output list,
# you must also append the code for a space:
#   
#   codes.append( dictionary.index( ' ' ) )
#
# so that the decompression logic knows when two words are separated!
#
# DICTIONARY
# ==========
# The dictionary may have words added to it with 
#
#   dictionary.append( theWord )
# 
# The dictionary can be queried to see if a paricular word exists in it:
#
#   if theWord in dictionary :
#      ... then do this...
#
# IF theWord exists in the dictionary, the integer code (the index) for it can
# be retrieved and appended to the codes list like this:
#
#   codes.append(  dictionary.index(theWord) )
#
#
# deflate returns a list of compression codes (list indices) and the final
# dictionary after compression is finished.
###
def deflate( words, dictionary ) :
	codes = []
		
	# Add new words to dictionary
	for word in words:
		if word in dictionary:
			codes.append(dictionary.index(word))
		else:
			for letter in word:
				codes.append(dictionary.index(str(letter)))
			dictionary.append(word)
		codes.append(dictionary.index(' '))

	# Add spaces to dictionary
	#dictionary.append(' ')
	#codes.append(dictionary.index(' '))

	return codes, dictionary



Main( deflate )
