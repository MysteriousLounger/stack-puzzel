# stack-puzzel
This is a command-line game in python that teaches about sorting and data structures.

This game requires numpy and python 3.x


code by Dallin 2019
StackPuzzel

in this game, the main objective is for the player to 
order a random stack. the player can pop off the stack,
and push to the stack. the player can place the items
they pop from the stack into another stack, a variable that
can hold a single item, or into a queue. the player can,
of course, remove items from the queue, variable, and stack,
and place those onto the main stack.
this game is played in the console.

How to play:
		
		your goal is to put the stack in order, from left to right.
		i.e. it should look like this:
		[1,2,3,4,5]
		
		you can only remove the last
		item in the stack. in this example,
		you could only access the "5".
		you can only place items on the
		end of the stack. in this example,
		you could only place a number after
		the "5".
		
		once you "grab" an item from the stack,
		it goes into your hand. from your hand,
		you can put it into three different storage
		places, or back on the stack. you can put it
		on the STORAGE SHELF, in your STORAGE STACK,
		or in your STORAGE QUEUE.
		
		STORAGE SHELF:
		The storage shelf can hold only one number
		at a time. if you place a new number on the
		shelf, the old one will be placed in your hand.
		
		STORAGE STACK:
		The storage stack works in the same way as the
		main stack, that is, first in, last out. if your
		storage stack looks like this [4,2,9], you can
		only remove the "9". if you did, it would look like
		[4,2], and the 2 would be accesible.
		
		STORAGE QUEUE:
		The storage Queue works on a first in, fist out
		basis. if your storage queue looks like this
		[4,9,6] you can only emove the "4", and if you
		did, it would look like this [9,6] and the "9"
		would now be accesible.
