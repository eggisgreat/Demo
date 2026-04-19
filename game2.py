from init import *

def Tile(pos:Vec3,hasColor:bool=False,col=color.white,uv:tuple=(0,0)):
    if hasColor:
        return Button(color=col,parent=scene,position=pos);
    else:
        return Button(color=col,parent=scene,texture="atlas.png",position=pos,texture_scale=(-0.25,-0.5),texture_offset=uv);

def render(pos:Vec3, tid:int=0):
    global blockChange
    tuv = blockUV(tid);
    if tuv[1]:temp = Tile(pos,True,color.rgb32(*tuv[0]));
    else:temp = Tile(pos,uv=tuv[0]);
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
        for i in len(tiles) - 1:
            tile = tiles[i];
            if tile.tid > 0 != tiles[i+1] > 0:
                tile.enable();
            else:
                tile.disable();
    blockChange = False;

def update():pass