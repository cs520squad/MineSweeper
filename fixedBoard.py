import random
import numpy as np
import math
def Get_Index(num):
    row = int(num/5)
    col = num%5
    return row, col
def Board():
    dim = 5
    board = np.full((dim, dim), 0)
    mine  = set([])
    while len(mine)<5:
        mine.add(np.random.randint(0,25))
    for i in mine:
        row, col = Get_Index(i)
        board[row, col] = -1  
    return board
def adj_count(numb):
    dim = 5
    row, col = Get_Index(numb)
    count =0
    if numb == 0:
        for i in (numb+1, numb+dim, numb+dim+1):
            if i in Board.mine:
                count+=1
    elif numb == dim-1:
        for i in (numb-1, numb+dim, numb+dim-1):
            if i in Board.mine:
                count+=1
    elif numb>0 and numb<dim-1:
        for i in (numb-1, numb+1, numb+dim,numb+dim-1, numb+dim+1):
            if i in Board.mine:
                count+=1
    elif numb == dim*(dim-1):
        for i in (numb-dim,num-dim+1,num+1):
            if i in Board.mine:
                count+=1
    elif numb == dim*dim-1:
        for i in (numb-dim, numb-dim-1,numb-1):
            if i in Board.mine:
                count+=1
    elif numb>dim*(dim-1) and numb<dim*dim-1:
        for i in (numb-1,numb+1,numb-dim, numb-dim+1,numb-dim-1):
            if i in Board.mine:
                count+=1
    elif numb%dim ==0 and numb!=0 and numb!= dim*(dim-1):
        for i in (numb+1, numb-dim, numb+dim, numb+dim+1, numb-dim+1):
            if i in Board.mine:
                count+=1
    elif numb%dim ==dim-1 and numb!=dim-1 and numb!=dim*dime-1:
        for i in (numb-1, numb+dim, numb-dim, numb-dim-1, numb+dim-1):
            if i in Board.mine:
                count+=1
    else:
        for i in (numb-1, numb+1, numb+dim, numb-dim, numb+dim+1, numb+dim-1, numb-dim+1, numb-dim-1):
            if i in Board.mine:
                count+=1
    return row, col, count
def adj():
    dim = 5
    for i in range(dim*dim):
        if i not in Board.mine:
            x, y, count= adj_count(i)
            Board.board[x,y] += count