import asyncio
import random


async def partida(points, p1, p2):
    if random.randint(0,1)==0:
        points[p1] = points[p1] + 2
    else:
        points[p2] = points[p2] + 2
    await asyncio.sleep(0.25)


async def ronda(points, i):
    if(i==0):
        await asyncio.gather(partida(points, 0, 1), partida(points, 2, 3))
    elif (i==1):
        await asyncio.gather(partida(points, 0, 2), partida(points, 1, 3))
    elif(i==2):
        await asyncio.gather(partida(points, 0, 3), partida(points, 1, 2))

if __name__ == '__main__':
    content = ""
    with open("chess_players.txt", "r") as f:
        while True:
            linea = f.readline()
            if not linea:
                break
            content += linea
    
    players_info = content.split('\n')
    players = []
    points = []
    for i in range(4):
        player = players_info[i].split(',')
        players.append(player[0])
        points.append(int(player[1]))
    for i in range(3):
        asyncio.run(ronda(points, i))
    
    winner_id = points.index(max(points))
    print(f"El ganador es: {players[winner_id]}")
    
    