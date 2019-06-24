
# coding: utf-8

# In[72]:


from collections import namedtuple
import random
import sys
import math
import time
import copy

def printf(format, *args):
    sys.stdout.write(format % args)

def showforest(nx,ny,t):
    for i in range(ny):
        for j in range(nx):
            if tnew[i][j].STATE == 'F':
                printf('\033[41m'"%c "'\033[0m',tnew[i][j].STATE)
            elif tnew[i][j].STATE == '^':
                printf('\033[42m'"%c "'\033[0m',tnew[i][j].STATE)
            elif tnew[i][j].STATE == '.':
                printf('\033[100m'"%c "'\033[0m',tnew[i][j].STATE)
            else:
                printf('\033[0m'"%c "'\033[0m',tnew[i][j].STATE)
        printf("\n")
    printf('\x1b[2J\x1b[H')
#    time.sleep(1)
    
def showforest_persist(nx,ny,t):
    for i in range(ny):
        for j in range(nx):
            if tnew[i][j].STATE == 'F':
                printf('\033[41m'"%c "'\033[0m',tnew[i][j].STATE)
            elif tnew[i][j].STATE == '^':
                printf('\033[42m'"%c "'\033[0m',tnew[i][j].STATE)
            elif tnew[i][j].STATE == '.':
                printf('\033[100m'"%c "'\033[0m',tnew[i][j].STATE)
            else:
                printf('\033[0m'"%c "'\033[0m',tnew[i][j].STATE)
        printf("\n")

NX = 30
NY = 30
generations = 20
Forest = namedtuple('Forest', 'STATE P B f')
tnew = []

for i in range(NY):
    new = []
    for j in range(NX):
        Node = Forest(' ',0.002,0.99,0.002)
        new.append(Node)
    tnew.append(new)


# Fill forest with trees
Dinit = 1
for i in range(1,NY-1):
    for j in range(1,NX-1):
        tnew[i][j] = tnew[i][j]._replace(STATE='^')

for step in range(generations):
    t = copy.deepcopy(tnew)
#    print(id(t),id(tnew),id(t[0]),id(tnew[0]),id(new),id(t[0][0]))
    for i in range(1,NY-1):
        for j in range(1,NX-1):
            
            #A burning tree becomes an empty site.
            if t[i][j].STATE == 'F':
                tnew[i][j] = tnew[i][j]._replace(STATE='.')
                    
            # If cell is unburnt but has burning neighbors see
            # if cell ignites.
            if t[i][j].STATE == '^':
                #A tree without a burning nearest neighbor becomes a burning tree with probability f.
                if t[i][j].f > random.random():
                    tnew[i][j] = tnew[i][j]._replace(STATE='F')
            
                # Either a corner neighbor possibly ignites cell
                # or side neighbor;
                # Corner neighbor influence is suppressed but 1/sqrt(2)
                # 0.293 is approx = 1-1/sqrt(2)
                elif 0.293 > random.random():
                    if (t[i+1][j+1].STATE=='F')or(t[i-1][j+1].STATE=='F')or(t[i+1][j-1].STATE=='F')or(t[i-1][j-1].STATE=='F'):
                        if t[i][j].B > random.random():
                            tnew[i][j] = tnew[i][j]._replace(STATE='F')
                else:    
                    if (t[i-1][j].STATE == 'F')or(t[i][j-1].STATE == 'F')or(t[i][j+1].STATE == 'F')or(t[i+1][j].STATE == 'F') :
                        if t[i][j].B > random.random():
                            tnew[i][j] = tnew[i][j]._replace(STATE='F')
                            
            #At an empty site, a tree grows with probability p.    
            if t[i][j].STATE == '.':
                if t[i][j].P > random.random():
                    tnew[i][j] = tnew[i][j]._replace(STATE='^')
                    
    showforest(NX,NY,tnew)
showforest_persist(NX,NY,tnew)


# In[54]:


from collections import namedtuple
import random
import sys
import math
import time
import copy

def printf(format, *args):
    sys.stdout.write(format % args)

def showforest(nx,ny,t):
    for i in range(ny):
        for j in range(nx):
            if tnew[i][j].STATE == 'F':
                printf('\033[41m'"%c "'\033[0m',tnew[i][j].STATE)
            elif tnew[i][j].STATE == '^':
                printf('\033[42m'"%c "'\033[0m',tnew[i][j].STATE)
            elif tnew[i][j].STATE == '.':
                printf('\033[100m'"%c "'\033[0m',tnew[i][j].STATE)
            else:
                printf('\033[0m'"%c "'\033[0m',tnew[i][j].STATE)
        printf("\n")
    printf('\x1b[2J\x1b[H')
#    time.sleep(1)
    
def showforest_persist(nx,ny,t):
    for i in range(ny):
        for j in range(nx):
            if tnew[i][j].STATE == 'F':
                printf('\033[41m'"%c "'\033[0m',tnew[i][j].STATE)
            elif tnew[i][j].STATE == '^':
                printf('\033[42m'"%c "'\033[0m',tnew[i][j].STATE)
            elif tnew[i][j].STATE == '.':
                printf('\033[100m'"%c "'\033[0m',tnew[i][j].STATE)
            else:
                printf('\033[0m'"%c "'\033[0m',tnew[i][j].STATE)
        printf("\n")

NX = 30
NY = 30
generations = 20
Forest = namedtuple('Forest', 'STATE B I D')
tnew = []

for i in range(NY):
    new = []
    for j in range(NX):
        #Node = Forest('E',random.random(),random.random(),random.random())
        Node = Forest(' ',0.5,0.99,random.random())
        new.append(Node)
    tnew.append(new)


# Fill forest with trees

for i in range(1,NY-1):
    for j in range(1,NX-1):
        if Dinit - tnew[i][j].D > 0:
            tnew[i][j] = tnew[i][j]._replace(STATE='^')


#Start a fire in the middle of the grid */
# Constant source fire */ //	tnew[nx/2][ny/2].B = 1;
tnew[NY//2][NX//2] = tnew[NY//2][NX//2]._replace(STATE = 'F');


for step in range(generations):
    t = copy.deepcopy(tnew)
#    print(id(t),id(tnew),id(t[0]),id(tnew[0]),id(new),id(t[0][0]))
    for i in range(1,NY-1):
        for j in range(1,NX-1):
            
            #If a cell is burning see if it continues burning
            #otherwise the fire goes out. 
            if t[i][j].STATE == 'F':
                if t[i][j].B < random.random():
                    tnew[i][j] = tnew[i][j]._replace(STATE='.')
            # If cell is unburnt but has burning neighbors see
            # if cell ignites.
            if t[i][j].STATE == '^':    
                # Either a corner neighbor possibly ignites cell
                # or side neighbor;
                # Corner neighbor influence is suppressed but 1/sqrt(2)
                # 0.293 is approx = 1-1/sqrt(2)
                if 0.293 > random.random():
                    if (t[i+1][j+1].STATE=='F')or(t[i-1][j+1].STATE=='F')or(t[i+1][j-1].STATE=='F')or(t[i-1][j-1].STATE=='F'):
                        if t[i][j].I > random.random():
                            tnew[i][j] = tnew[i][j]._replace(STATE='F') 
                else :    
                    if (t[i-1][j].STATE == 'F')or(t[i][j-1].STATE == 'F')or(t[i][j+1].STATE == 'F')or(t[i+1][j].STATE == 'F') :
                        if t[i][j].I > random.random():
                            tnew[i][j] = tnew[i][j]._replace(STATE='F') 
    showforest(NX,NY,tnew)
showforest_persist(NX,NY,tnew)


# In[ ]:


#parallelized version

from collections import namedtuple
import random
import sys
import math
import time
import copy
import itertools
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
stat = MPI.Status()

NX = 50
NY = 50
generations = 50

if size > NY:
        print("Not enough ROWS")
        exit()

subGridRowSize = NY//size + 2


def printf(format, *args):
	sys.stdout.write(format % args)

def showforest(nx,ny,tnew): 
	for i in range(ny):
		for j in range(nx):
			if tnew[i][j].STATE == 'F':
				printf('\033[41m'"%c "'\033[0m',tnew[i][j].STATE)
			elif tnew[i][j].STATE == '^':
				printf('\033[42m'"%c "'\033[0m',tnew[i][j].STATE)
			elif tnew[i][j].STATE == '.':
				printf('\033[100m'"%c "'\033[0m',tnew[i][j].STATE)
			else:
				printf('\033[0m'"%c "'\033[0m',tnew[i][j].STATE)
		printf("\n")
	printf('\x1b[2J\x1b[H')

    
def showforest_persist(nx,ny,tnew):
	for i in range(ny):
		for j in range(nx):
			if tnew[i][j].STATE == 'F':
				printf('\033[41m'"%c "'\033[0m',tnew[i][j].STATE)
			elif tnew[i][j].STATE == '^':
				printf('\033[42m'"%c "'\033[0m',tnew[i][j].STATE)
			elif tnew[i][j].STATE == '.':
				printf('\033[100m'"%c "'\033[0m',tnew[i][j].STATE)
			else:
				printf('\033[0m'"%c "'\033[0m',tnew[i][j].STATE)
		printf("\n")

        
def sendDown(subGrid):
	comm.send(subGrid[1],dest=rank-1)
	subGrid[0] = comm.recv(source=rank-1)

def sendUp(subGrid):
	comm.send(subGrid[subGridRowSize-2],dest=rank+1)
	subGrid[subGridRowSize-1]=comm.recv(source=rank+1)       


def forestfire(tnew):
	t = copy.deepcopy(tnew)
#    print(id(t),id(tnew),id(t[0]),id(tnew[0]),id(new),id(t[0][0]))
	for i in range(1,subGridRowSize-1):
		for j in range(1,NX-1):

			#A burning tree becomes an empty site.
			if t[i][j].STATE == 'F':
				tnew[i][j] = tnew[i][j]._replace(STATE='.')

			# If cell is unburnt but has burning neighbors see
			# if cell ignites.
			if t[i][j].STATE == '^':
				#A tree without a burning nearest neighbor becomes a burning tree with probability f.
				if t[i][j].f > random.random():
					tnew[i][j] = tnew[i][j]._replace(STATE='F')

				# Either a corner neighbor possibly ignites cell
				# or side neighbor;
				# Corner neighbor influence is suppressed but 1/sqrt(2)
				# 0.293 is approx = 1-1/sqrt(2)
				elif 0.293 > random.random():
					if (t[i+1][j+1].STATE=='F')or(t[i-1][j+1].STATE=='F')or(t[i+1][j-1].STATE=='F')or(t[i-1][j-1].STATE=='F'):
						if t[i][j].B > random.random():
							tnew[i][j] = tnew[i][j]._replace(STATE='F')
				else:    
					if (t[i-1][j].STATE == 'F')or(t[i][j-1].STATE == 'F')or(t[i][j+1].STATE == 'F')or(t[i+1][j].STATE == 'F') :
						if t[i][j].B > random.random():
							tnew[i][j] = tnew[i][j]._replace(STATE='F')

			#At an empty site, a tree grows with probability p.    
			if t[i][j].STATE == '.':
				if t[i][j].P > random.random():
					tnew[i][j] = tnew[i][j]._replace(STATE='^')
	return tnew



Forest = namedtuple('Forest', 'STATE P B f')
tnew = []
for i in range(subGridRowSize):
	new = []
	for j in range(NX):
		Node = Forest(' ',0.002,0.99,0.002)
		new.append(Node)
	tnew.append(new)
    
# Fill forest with trees
Dinit = 1
for i in range(1,subGridRowSize-1):
	for j in range(1,NX-1):
		tnew[i][j] = tnew[i][j]._replace(STATE='^')
if rank == size // 2:
	print "ignite:",rank
	tnew[subGridRowSize//2][NX//2] = tnew[subGridRowSize//2][NX//2]._replace(STATE = 'F')
		
time.sleep(2)
 

for i in range(generations):
	tnew = forestfire(tnew)
	if rank == 0:
		sendUp(tnew)
	elif rank == size -1:
		sendDown(tnew)
	else:
		sendUp(tnew)
		sendDown(tnew)

	finalGrid = comm.gather(tnew[1:subGridRowSize-1],root=0)

	if rank == 0:
		list_forest = list(itertools.chain.from_iterable(finalGrid))
		showforest_persist(NX,NY-2,list_forest) # [changed to NY-2 to match the number of columns]
		print "----------------------------" #[print a line to show more clearly]
		time.sleep(1)

