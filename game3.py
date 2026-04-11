from game2 import *

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
        render((x,y,z), tid);
        if not s:
            for j in range(5):
                x+=random.choice([-1,1]);z+=random.choice([-1,1])
                render((x,y,z), tid);