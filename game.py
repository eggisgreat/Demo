from game2 import *
from alt import *

spawn();
iron = 0;
points = 0;
gold = 0;

generate();
text1 = Text(f"Points:{points}");
text2 = Text(f"Iron:{iron}",origin=(-0.5,-0.5));
text3 = Text(f"Gold:{gold}",origin=(-0.5,-1.5))

def input(key):
    global points, blockid, iron, gold
    match key:
        case "1":blockid = 1;
        case "2":blockid = 2;
        case "3":blockid = 3;
        case "4":blockid = 4;
    tile = mouse.hovered_entity;
    try:
        if distance(tile, player) < 8:
            if key == "left mouse down":
                Audio("shoot.wav");
                p = tile.position+mouse.normal;
                match blockid:
                    case 1:render(p, 2);
                    case 2:render(p, 1);
                    case 3:
                        if iron != 0:render(p, 5);iron -= 1;
                    case 4:
                        if gold != 0:render(p, 8);gold -= 1;
            if key == "right mouse down":
                if tile in tiles:
                    match tile.id:
                        case 3:points += 50;gold += 1;
                        case 4:iron += 1;
                        case 6:points += 100;
                    deltile(tile);
                    Audio("shoot.wav");
                    text1.text = f"Points:{points}";
                    text2.text = f"Iron:{iron}";
                    text3.text = f"Gold:{gold}";
    except:
        pass;
    if key=="r":spawn();
    if key=="escape":print("\033[2J\033[H");quit();

app.run();