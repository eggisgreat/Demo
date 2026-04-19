from init import *

def render(pos:Vec3, tid:int=0):
    global blockChange
    tuv = blockUV(tid);
    if tuv[1]:temp = Button(position=pos,parent=scene,color=color.rgb32(*tuv[0]));
    else:temp = Button(texture=f"atlas.png",position=pos,parent=scene,texture_scale=(-0.25,-0.5),texture_offset=tuv[0]);
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