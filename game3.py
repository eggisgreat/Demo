from game2 import *

blockid = 2;

def makeores(cl:int,ch:int,r:int,ore:str,s:bool=False):
    for i in range(random.randint(cl, ch)):
        x = random.randint(0,9);
        y = random.randint(0,r);
        z = random.randint(0,9);
        tid = 0;
        match ore:
            case "rock":tid = 1;
            case "grass":tid = 2;
            case "gold":tid = 3;
            case "iron":tid = 4;
            case "diamond":tid = 6;
            case "copper":tid = 7;
        render((x,y,z), tid);
        if not s:
            for j in range(5):
                x+=random.choice([-1,1]);z+=random.choice([-1,1])
                render((x,y,z), tid);

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
    makeores(40, 45, 7,"copper");
    makeores(30, 40, 7,"iron");
    makeores(5, 10, 5, "gold");
    makeores(2, 3, 3, "diamond",True);
    blockid = 2;

def spawn():player.position_setter(5, 20, 5);