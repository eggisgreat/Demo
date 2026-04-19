from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import *
app = Ursina(title="Game",fullscreen=True);
player = FirstPersonController();
Sky();
tiles = [];
blockChange = False;
Button.default_color = color.white;
Button.default_model = "cube";
player.scale_y = 0.85
player.jump_height = 1.5;

def uv(x, y):
    return (x*0.25, y*0.5)

def blockUV(tid):
    tuv = ();
    sCol = False;
    col = ();
    match tid:
        case 1:tuv=uv(2,0);
        case 2:tuv=uv(1,0);
        case 3:tuv=uv(3,0);
        case 4:tuv=uv(4,0);
        case 5:tuv=uv(2,1);
        case 6:tuv=uv(3,1);
        case 7:tuv=uv(1,1);
        case 8:tuv=uv(0,1);
        case 9:
            sCol=True;
            col = (170,85,0);
    if sCol:
        return [col, True];
    else:
        return [tuv, False];