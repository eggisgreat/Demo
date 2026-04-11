from game2 import *
from game3 import *

player.position_setter((5, 10, 5));
iron = 0;
points = 0;

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
    makeores(30, 40, 7,"iron");
    makeores(5, 10, 5, "gold");
    blockid = 2;

generate();
text1 = Text(f"Points:{points}")

def input(key):
    global points, blockid, iron
    match key:
        case "1":blockid = 1;
        case "2":blockid = 2;
        case "3":blockid = 3;
    tile = mouse.hovered_entity;
    if tile != None:
        if key == "left mouse down":
            Audio("shoot.wav");
            p = tile.position+mouse.normal;
            match blockid:
                case 1:render(p, 2);
                case 2:render(p, 1);
                case 3:
                    if iron != 0:
                        render(p, 5);
                        iron -= 1;
        if key == "right mouse down":
                match tile.id:
                    case 3:points += 50;
                    case 4:iron += 1;
                Audio("shoot.wav");
                if tile in tiles:deltile(tile);
                text1.text = f"Points:{points}";
            
    if key=="r":player.position_setter((5, 20, 5));
    if key=="g":
        if points - 1000 >= 0:
            generate();
            points -= 1000;
    if key=="escape":print("\033[2J\033[H");quit();

app.run();