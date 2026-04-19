from game2 import *

blockid = 2;

def makeores(cl:int,ch:int,r:int,ore:str,s:bool=False):
    for i in range(randint(cl, ch)):
        x = randint(0,8);
        y = randint(0,r);
        z = randint(0,8);
        tid = 0;
        match ore:
            case "rock":tid = 1;
            case "grass":tid = 2;
            case "gold":tid = 3;
            case "iron":tid = 4;
            case "diamond":tid = 6;
            case "copper":tid = 7;
        render((x,y,z),tid);
        if not s:
            render((x+1,y,z),tid);
            render((x,y,z+1),tid);
            render((x+1,y,z+1),tid);

def tree():
    x = round(randint(1, 8)/2);
    z = round(randint(1, 8)/2);
    for i in range(4):
        render((x,10+i,z),9)
    render((x,13,z),2)
    for i in range(3):
        for j in range(3):
            render((x-1+i,12,z-1+j),2);

def generate():
    global points, blockid, iron, text1
    for tile in tiles:
        tiles.remove(tile);
        destroy(tile);
    for i in range(10):
        for j in range(10):
            for k in range(9):
                render((j, k, i), 1);
    for i in range(10):
        for j in range(10):
            render((j, 9, i), 2);
    makeores(20, 24, 7,"copper");
    makeores(10, 20, 7,"iron");
    makeores(5, 10, 5, "gold");
    makeores(2, 5, 3, "diamond",True);
    for i in range(3):tree();
    blockid = 2;

def spawn():player.position_setter((5, 20, 5));