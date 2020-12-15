import math

f = open("input", "r")

lines = [l.strip() for l in f.readlines()]

f.close()

INSTRUCTIONS = [ (l[0], int(l[1:])) for l in lines]


class Movable:

    def __init__(self):
        self.name = "Waypoint"
        # self.pos = {
        #     'N' :  1, # pos
        #     'E' : 0  # pos
        # }
        self.pos = {
            'N' :  1, # pos
            'E' : 10  # pos
        }
        self.directions = ['E', 'N', 'W', 'S'] # gUZS
    
    def move(self, dir, amount):
        if dir == 'N':
            self.pos[dir] += amount
        elif dir == 'S':
            self.pos['N'] -= amount
        elif dir == 'E':
            self.pos[dir] += amount
        elif dir == 'W':
            self.pos['E'] -= amount
        else:
            print("this should not have happened")
    
    def get_pos(self):
        return "{} E{} N{}".format(self.name, self.pos['E'], self.pos['N'])


class Ferry(Movable):

    def __init__(self):
        Movable.__init__(self)
        self.name = "Ferry"

        self.pos = {
            'N' : 0,
            'E' : 0
        }
        self.facing = 0 # in direction of directions
        self.turns = {'L' : 1,
                      'R' : -1}
    
    def move(self, dir, amount):
        if dir in self.directions:
            Movable.move(self, dir, amount)
        elif dir == 'F':
            Movable.move(self, self.is_facing(), amount)
        else:
            self.turn(dir, amount)
    
    def turn(self, dir, amount):
        self.facing = (self.facing + self.turns[dir]*int(amount/90)) % len(self.directions)
        
    def is_facing(self):
        return self.directions[ self.facing ]
    
    def get_distance(self):
        return abs( self.pos['N'] ) + abs( self.pos['E'] )


class IntructionHandler:

    def __init__(self, waypoint, ferry):
        self.waypoint = waypoint
        self.ferry = ferry
    
    def to_rad(self, degree):
        return math.pi * degree / 180.0

    def move(self, instruction, amount):
        if instruction in ['L', 'R']:
            cos = math.cos( self.to_rad(amount) ) if instruction == 'L' else math.cos(self.to_rad (-amount))
            sin = math.sin( self.to_rad(amount) ) if instruction == 'L' else math.sin(self.to_rad (-amount))
            newx = cos*self.waypoint.pos['E'] - sin * self.waypoint.pos['N']
            newy = sin * self.waypoint.pos['E'] + cos * self.waypoint.pos['N']
            self.waypoint.pos['E'] = round(newx)
            self.waypoint.pos['N'] = round(newy)
        elif instruction == 'F':
            dx = amount*self.waypoint.pos['E']
            dy = amount*self.waypoint.pos['N']
            self.ferry.pos['N'] += dy
            self.ferry.pos['E'] += dx
        else:
            self.waypoint.move(instruction, amount)


def get_pos(*movables):
    return "-"*80 + "\n" + "\n".join(m.get_pos() for m in movables)

def get_total():
    ferry = Ferry()
    for d, a in INSTRUCTIONS:
        ferry.move(d,a)
    return ferry.get_distance()

def get_total_part2():
    waypoint = Movable()
    ferry = Ferry()
    ihandler = IntructionHandler(waypoint, ferry)
    for i,a in INSTRUCTIONS:
        ihandler.move(i, a)#
    return ferry.get_distance()


if __name__ == "__main__":
    print( get_total() )
    print( get_total_part2() )
    # waypoint = Movable()
    # ferry = Ferry()
    # print(get_pos(waypoint, ferry))
    # ihandler = IntructionHandler(waypoint, ferry)
    # ihandler.move('F', 10)
    # print(get_pos(waypoint, ferry))
    # ihandler.move('N', 3)
    # print(get_pos(waypoint, ferry))
    # ihandler.move('F', 7)
    # print(get_pos(waypoint, ferry))
    # ihandler.move('R', 90)
    # print(get_pos(waypoint, ferry))