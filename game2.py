from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina(title="Game",fullscreen=True);
player = FirstPersonController();
Sky();
tiles = [];
grid = {};
attrs = {};
blockChange = False;
Button.default_color = color.white;

def uv(x, y):
    return (x*0.25, y*0.5)

def render(pos:Vec3, tid:int=0):
    tuv = ()
    match tid:
        case 1:tuv = uv(2,0)
        case 2:tuv = uv(1,0)
        case 3:tuv = uv(3,0)
        case 4:tuv = uv(4,0)
        case 5:tuv = uv(2,1)
    temp = Button(model="cube",texture=f"atlas.png",position=pos,origin_y=0.5,parent=scene,texture_scale=(-0.25,-0.5),texture_offset=tuv);
    temp.id = tid;
    for tile in tiles:
        if tile.position == temp.position:
            tiles.remove(tile);
            destroy(tile);
            break;
    tiles.append(temp);
    blockChange = True;

def deltile(tile:Button):
    tiles.remove(tile);
    destroy(tile);

def drawTiles(pos:Vec3):
    if blockChange:
        for tile in tiles:
            if tile.tid > 0:
                tile.enable();
            else:
                tile.disable();
    blockChange = False;

def update():pass