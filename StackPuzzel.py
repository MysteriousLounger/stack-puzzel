## code by Dallin 2019
## StackPuzzel

## in this game, the main objective is for the player to 
## order a random stack. the player can pop off the stack,
## and push to the stack. the player can place the items
## they pop from the stack into another stack, a variable that
## can hold a single item, or into a queue. the player can,
## of course, remove items from the queue, variable, and stack,
## and place those onto the main stack.
## this game is played in the console.

import numpy as np
import random, time

def gameSetup(endVar):
	stackPuz = list(np.random.permutation(range(1,endVar)))
	return stackPuz

def reportGame(stackPuz,shelf,hand,m_stack,m_queue):
	print('this is the current state of the puzzel stack :')
	print(stackPuz)
	print('in your hand is ({}) and on the shelf is ({})'.format(hand,shelf))
	if m_stack != []:
		print('in your stack is:')
		print(m_stack)
	else:
		print('your stack is empty.')
	if m_queue != []:
		print('in your queue is:')
		print(m_queue)
	else:
		print('your queue is empty.')	
	action = input('type [help] for how to play the game.')
	if action.lower() == 'help':
		print('''
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
		
		''')
	return

def getTop(pStack, shelf, stack, queue, hand):
	if pStack == []:
		p = None
	else:
		p = pStack[-1]
	
	f = shelf

	if stack == []:
		s = None
	else:
		s = stack[-1]
	
	if queue == []:
		q = None
	else:
		q = queue[0]
	
	h = hand

	return p, f, s, q, h

def checkWin(stackPuz, endNum, start):
	win = False
	playing = True
	if stackPuz == list(range(1,endNum)):
		win = True
		print('You Won! your score was {:6.1f} seconds.'.format((time.time()-start)))
		action = input('Play again? [y/n]')
		if not action.lower == 'y':
			playing = False
		else:
			print('starting new game...')
		
	else:
		action = input('Press [n] to quit, any other button to keep playing')
		if action.lower() == 'n':
			playing = False
			win = True
			print('gave up after {:6.1f} seconds.'.format((time.time()-start)))
	return win, playing

def playLoop():
	playing = True
	win = False
	
	while playing:
		endNum = 11
		stackPuz = gameSetup(endNum) #the stack the player needs to sort
		shelf = None # number that is on the single-variable shelf.
		hand = None  # number that the player is currently moving between locations.
		m_stack = [] # stack that the player can hold numbers in
		m_queue = [] # queue that the player can hold numbers in
		
		start = time.time()
		
		reportGame(stackPuz,shelf,hand,m_stack,m_queue)
		
		while not win:
			
			p, f, s, q, h = getTop(stackPuz, shelf, m_stack, m_queue, hand)
			
			if hand == None:
				action = input('''grab from where?
(puzzelStack({})[p], shelf({})[f],
stack({})[s], queue({})[q])
				'''.format(p,f,s,q))
				if action.lower() == 'p':
					if stackPuz != []:
						hand = stackPuz.pop()
					elif stackPuz == []:
						print('Stack is empty!')
				elif action.lower() == 'f':
					hand, shelf = shelf, hand
				elif action.lower() == 's':
					if m_stack != []:
						hand = m_stack.pop()
					elif m_stack == []:
						print('Stack is empty!')
				elif action.lower() == 'q':
					if m_queue != []:
						hand = m_queue.pop(0)
					elif m_queue == []:
						print('Queue is empty!')
				else:
					print('invalid command')
				action=''
			
			p, f, s, q, h = getTop(stackPuz, shelf, m_stack, m_queue, hand)
			
			if hand != None:
				action = input('''put ({}) where?
(puzzelStack[p], shelf, swap with ({})[f],
stack[s], queue[q]
				'''.format(h, f))
				if action.lower() == 'p':
					stackPuz.append(hand)
					hand = None
				elif action.lower() == 'f':
					hand, shelf = shelf, hand
				elif action.lower() == 's':
					m_stack.append(hand)
					hand = None
				elif action.lower() == 'q':
					m_queue.append(hand)
					hand = None
				else:
					print('invalid command')
				action=''
			
			action = input('print game state?[y/n]')
			if action.lower() == 'y':
				reportGame(stackPuz,shelf,hand,m_stack,m_queue)
				action = ''
			
			win, playing = checkWin(stackPuz,endNum, start)
	return

if __name__ == '__main__':
	
	playLoop()

