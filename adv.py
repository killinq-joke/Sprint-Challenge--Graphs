from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path =  ['w', 'w', 's', 'w', 's', 's', 'n', 'n', 'e', 'n', 'e', 'n', 'w', 'w', 's', 'n', 'w', 's',
#  's', 's', 's', 'w', 's', 'w', 'e', 'n', 'w', 'e', 'e', 's', 's', 'w', 's', 'w', 's', 'w', 's', 'n', 'e',
#  'n', 'w', 'w', 's', 's', 'w', 's', 'w', 'e', 's', 'w', 'e', 's', 's', 'n', 'w', 'w', 'e', 'e', 'n', 'n',
#  'n', 'w', 'w', 'w', 'e', 'e', 'e', 'e', 's', 's', 's', 's', 'e', 'w', 'n', 'e', 'w', 'n', 'n', 'n', 'n',
#  'w', 'w', 'e', 'e', 'n', 'w', 'e', 'e', 'e', 'e', 'n', 'w', 'w', 'n', 's', 'w', 'n', 'w', 'n', 'n', 'w',
#  'n', 'w', 'e', 'e', 'n', 'w', 'n', 's', 'w', 'e', 'e', 'n', 's', 'e', 'e', 'e', 'n', 'e', 's', 'n', 'n',
#  'e', 'n', 's', 'e', 'e', 'n', 's', 'e', 'e', 'n', 'n', 'w', 'w', 'w', 'w', 'n', 's', 'w', 'n', 'w', 'n',
#  'w', 'n', 'n', 's', 's', 'w', 'w', 'w', 's', 'w', 'e', 'n', 'w', 'e', 'e', 'e', 'n', 'w', 'e', 'n', 'n',
#  's', 's', 's', 'e', 'e', 'n', 'n', 'n', 'w', 'e', 'n', 'n', 's', 's', 's', 's', 's', 's', 'w', 'w', 'e',
#  'e', 'e', 'n', 'n', 'n', 'n', 's', 's', 's', 's', 's', 'e', 'e', 'n', 'n', 'w', 'n', 's', 'e', 's', 's',
#  'e', 'e', 'n', 'n', 'n', 'w', 'w', 'n', 'w', 'e', 's', 'e', 'n', 's', 'e', 's', 's', 'w', 'n', 's', 'e',
#  's', 'e', 'e', 's', 'n', 'n', 'n', 'w', 'n', 'n', 'w', 'n', 'w', 'e', 'e', 'w', 's', 'e', 's', 's', 'e',
#  'n', 'n', 'e', 'e', 'n', 's', 'e', 'e', 'w', 'n', 'e', 'n', 'e', 'e', 'n', 's', 'e', 'w', 'w', 'n', 's',
#  'w', 's', 'e', 'w', 'w', 'n', 'n', 'n', 'n', 's', 's', 'e', 'n', 'n', 's', 'e', 'n', 'e', 'e', 'w', 's',
#  'n', 'w', 'n', 's', 's', 'w', 's', 'w', 's', 'w', 'n', 'n', 'n', 'n', 'e', 'e', 'w', 'w', 's', 'w', 'n',
#  'w', 'w', 'e', 'e', 's', 'w', 's', 's', 's', 'e', 'n', 'n', 's', 's', 'w', 'w', 'w', 'w', 'n', 'w', 'n',
#  'n', 'w', 'e', 's', 's', 'e', 'n', 'n', 'n', 's', 's', 's', 's', 'w', 's', 'w', 'e', 'n', 'w', 'n', 's',
#  'w', 'n', 's', 'e', 'e', 'e', 'e', 'e', 'n', 'w', 'n', 's', 'e', 'n', 's', 's', 'e', 's', 's', 'n', 'e',
#  'w', 's', 's', 'e', 'e', 'w', 'w', 's', 's', 's', 'w', 'n', 's', 's', 'w', 'e', 's', 'e', 's', 'e', 'e',
#  'e', 'n', 'e', 'n', 'e', 'n', 'e', 'e', 'e', 'n', 'e', 'w', 's', 'e', 'w', 'w', 's', 'e', 'e', 'e', 's',
#  'n', 'w', 'w', 'w', 'n', 'w', 's', 'n', 'w', 'n', 'e', 'n', 'n', 'e', 'e', 'e', 's', 'n', 'w', 'w', 'w',
#  's', 's', 'e', 'n', 'e', 'w', 's', 'w', 'w', 's', 's', 'w', 's', 'e', 'e', 'e', 'e', 'e', 's', 'n', 'w',
#  'w', 'w', 'w', 'w', 'w', 's', 'e', 's', 'n', 'e', 'e', 'e', 'w', 'w', 's', 'e', 'e', 'e', 'e', 'w', 'n',
#  's', 'w', 'w', 'w', 'n', 'w', 'w', 'w', 's', 's', 's', 'n', 'n', 'e', 's', 'e', 'e', 's', 'e', 'e', 'e',
#  'w', 's', 'n', 'w', 'w', 's', 's', 's', 's', 'e', 'e', 'w', 'w', 'n', 'e', 'e', 'w', 'w', 'n', 'e', 'e',
#  'w', 'n', 's', 'w', 'n', 'n', 'n', 'e', 'e', 'e', 'w', 'w', 'w', 'w', 'w', 's', 'e', 'w', 'n', 'n', 'w',
#  'n', 'w', 'n', 'n', 'n', 'n', 'n', 's', 's', 'e', 'n', 'n', 's', 's', 'w', 's', 's', 'e', 'n', 'e', 'n',
#  'n', 'n', 'n', 's', 's', 's', 'e', 'n', 'n', 'n', 's', 'e', 'n', 'n', 'e', 'n', 's', 'e', 'e', 'e', 'w',
#  'n', 's', 'w', 'n', 's', 'w', 'w', 's', 's', 'w', 's', 's', 'w', 's', 'w', 's', 'w', 's', 'w', 's', 's',
#  'e', 's', 'n', 'w', 's', 'w', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 'n', 'n', 'n', 'n', 'n',
#  'w', 'w', 'w', 'n', 's', 'e', 's', 'e', 's', 's', 's', 'n', 'n', 'n', 'w', 's', 'n', 'w', 's', 'n', 'e',
#  'n', 'e', 'n', 'w', 'e', 'n', 'w', 'e', 'n', 'w', 'w', 's', 'n', 'e', 'e', 'n', 'w', 'e', 'n', 'w', 'e',
#  'e', 'e', 's', 'e', 's', 's', 'n', 'n', 'e', 's', 'e', 'n', 'e', 's', 's', 'n', 'n', 'w', 's', 'w', 's',
#  'e', 's', 's', 'e', 'e', 'e', 'e', 'w', 'w', 'w', 'w', 'n', 'e', 'w', 'n', 'w', 's', 's', 's', 'e', 'w',
#  'n', 'n', 'n', 'n', 'n', 'w', 'w', 's', 's', 's', 'e', 's', 's', 's', 'e', 's', 's', 's', 'n', 'n', 'e',
#  's', 's', 'n', 'n', 'e', 's', 's', 'n', 'n', 'w', 'w', 'n', 'e', 'e', 'n', 'e', 'e', 'e', 'w', 's', 's',
#  'e', 'w', 's', 's', 'n', 'n', 'n', 'n', 'w', 's', 's', 'n', 'n', 'w', 's', 'w', 'w', 'w', 's', 's', 'w',
#  's', 'n', 'e', 's', 's', 'n', 'n', 'n', 'n', 'n', 'w', 's', 's', 'n', 'n', 'e', 'n', 'n', 'w', 's', 'n',
#  'n', 'n', 'n', 'n', 'n', 'n', 'w', 'n', 's', 's', 'n', 'w', 'e', 's', 'w', 'e', 'n', 'e', 'e', 'w', 'n',
#  'n', 'w', 'w', 'w', 'w', 'n', 's', 'w', 'w', 'w', 'w', 'w', 'w', 'e', 'n', 'n', 's', 'w', 'n', 'w', 'w',
#  'w', 'e', 'e', 'e', 'n', 's', 's', 'w', 's', 'n', 'w', 'e', 'e', 'e', 's', 'e', 'e', 'e', 'n', 'w', 'n',
#  'w', 'e', 's', 'w', 'e', 'e', 's', 's', 'w', 'w', 'w', 'e', 'e', 's', 'w', 'w', 'w', 's', 'w', 's', 'e',
#  's', 's', 'w', 'n', 'w', 'e', 's', 'e', 'e', 's', 'w', 'w', 's', 'w', 's', 'n', 'e', 'n', 'e', 'e', 'e',
#  'e', 'e', 'e', 's', 's', 's', 's', 's', 'e', 'e', 's', 's', 'e', 'w', 's', 'w', 'e', 'n', 'n', 'n', 'w',
#  's', 'n', 'w', 's', 'w', 'e', 'n', 'n', 'n', 'n', 'w', 's', 's', 's', 'n', 'n', 'w', 's', 'w', 'e', 's',
#  'w', 'e', 'n', 'n', 'e', 'n', 'e', 'n', 'n', 'n', 'n', 'n', 'w', 'n', 'w', 'w', 'w', 'e', 'e', 'e', 's',
#  'w', 'w', 's', 'w', 'n']

traversal_path = []


def reverse_dir(dir):
    if dir == "n":
        return "s"
    if dir == "s":
        return "n"
    if dir == "e":
        return "w"
    if dir == "w":
        return "e"
    else:
        return None


def findShortest_path(adj):
    q = Queue()
    q.enqueue([player.current_room.id])
    visited = set()
    while q.size() > 0:
        path = q.dequeue()
        vert = path[-1]
        if vert not in visited:
            if "?" in adj[vert].values():
                return path
            visited.add(vert)
            for room in adj[vert].values():
                new_path = list(path)
                new_path.append(room)
                q.enqueue(new_path)
    return None


def get_dir(adj, path):
    new_path = []
    for idx, room in enumerate(path):
        if idx > 0:
            last_room = path[idx - 1]
            for direction in adj[last_room]:
                if adj[last_room][direction] == room:
                    new_path.append(direction)
    return new_path


def travel_dir(traversal, path):
    for direction in path:
        traversal.append(direction)
        player.travel(direction)


def createTraversal_path():
    adjacency = dict()
    traversal = Stack()
    last_dir = None
    last_room = None
    while len(adjacency) < len(world.rooms):
        if player.current_room.id not in adjacency:
            adj = dict()
            for ext in player.current_room.get_exits():
                adj[ext] = "?"
            adjacency[player.current_room.id] = adj
        if last_room:
            adjacency[last_room][last_dir] = player.current_room.id
            adjacency[player.current_room.id][reverse_dir(last_dir)] = last_room
        last_room = player.current_room.id

        cur_adj = adjacency[player.current_room.id]
        unvisited = list()
        for direction, room in cur_adj.items():
            if room == "?":
                unvisited.append(direction)

        if len(unvisited) > 0:
            random.shuffle(unvisited)
            direction = unvisited[0]
            last_dir = direction
            traversal.push(direction)
            traversal_path.append(direction)
            player.travel(direction)
        else:
            path = findShortest_path(adjacency)
            if path is not None:
                dir_path = get_dir(adjacency, path)
                travel_dir(traversal_path, dir_path)
                last_dir = dir_path[-1]
                last_room = path[-2]

        # if not moved:
        #     ext = reverse_dir(traversal.pop())
        #     traversal_path.append(ext)
        #     last_dir = ext
        #     player.travel(ext)
lowest = 999999
shortest_path = []
for i in range(10000):
    player.current_room = world.starting_room
    traversal_path = []
    createTraversal_path()
    if len(traversal_path) < lowest:
        lowest = len(traversal_path)
        shortest_path = traversal_path

traversal_path = shortest_path
print(shortest_path)

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
