from pprint import pprint

ACTIVE = "#"
INACTIVE = "."

class PocketPlane:

    def __init__(self, inputfile):
        self.cosy = self.from_input(inputfile)
        self.clear_inactives()

    def get_neighbors(self, x, y, z):
        neighbors = []
        for _x in range(-1,2):
            for _y in range(-1,2):
                for _z in range(-1,2):
                    if not (0 == _x == _y == _z):
                        neighbors.append( (x+_x,y+_y,z+_z)  )
        return neighbors
    
    def advance_time(self, cycles=1):
        # it should be sufficient to loop through all of
        # self.cosy, since INACTIVE cubes are not stored here
        while cycles:
            cubes_to_check = self.collect_potential_cubes()
            cubes_to_switch = self.get_cubes_to_switch(cubes_to_check)
            self.apply_changes(cubes_to_switch)
            cycles -= 1
    
    def collect_potential_cubes(self):
        cubes_to_check = set()
        for k in self.cosy.keys():
            if self.cosy[k] != ACTIVE:
                raise ValueError("there shouldnt be a inavtive cube in self.cosy")
            cubes_to_check.update(self.get_neighbors(*k))
            # since it is not his own neighbor, append this one too
            cubes_to_check.add(k)
        return cubes_to_check
    
    def get_cubes_to_switch(self, set_of_cubes):
        cubes_to_switch = set()
        for element in set_of_cubes:
            if self.cube_evolution(*element):
                cubes_to_switch.add(element)
        return cubes_to_switch

    def apply_changes(self, cubes_to_switch):
        for cube in cubes_to_switch:
            self.switch_cube(*cube)
    
    def clear_inactives(self):
        # this my not be needed if set method is smart
        to_delete =[]
        for key in self.cosy.keys():
            if self.cosy[key] == INACTIVE:
                to_delete.append(key)
        for key in to_delete:
            del self.cosy[key]

    def cube_evolution(self, x, y, z):
        # method returns True if x,y,z should be switched

        # active with 2 or 3 neighbors active => stay active
        #        otherwise => becomes inactive
        # inactive exactly 3 neighbots active => become active
        #        otherwise => stays inactive
        # neighbors = [(x,y,z) for (x,y,z) in self.get_neighbors(x,y,z)]
        # for nb in neighbors:
        #     print(self.is_active(*nb))
        # active_neighbors = len([nb for nb in neighbors if self.is_active(*nb)])
        active_neighbors = len([(x,y,z) for (x,y,z) in self.get_neighbors(x,y,z) if self.is_active(x,y,z)])
        if self.is_active(x,y,z) and (active_neighbors<2 or active_neighbors>3):
            # check if less than 2 or more than 3 neighbors are active, then switch
            return True
        elif (not self.is_active(x,y,z)) and active_neighbors == 3:
            return True
        return False

    def get_cube(self, x, y, z):
        if (x,y,z) in self.cosy:
            return self.cosy[(x,y,z)]
        return "."

    def set_cube(self, x, y, z, value):
        if value == ACTIVE:
            self.cosy[(x,y,z)] = value
        elif value == INACTIVE and (x,y,z) in self.cosy:
            del self.cosy[(x,y,z)]
    
    def switch_cube(self, x,y,z):
        if self.is_active(x,y,z):
            self.set_cube(x, y, z, INACTIVE)
        else:
            self.set_cube(x, y, z, ACTIVE)
    
    def is_active(self, x, y, z):
        return self.get_cube(x,y,z) == ACTIVE

    def print_slice(self, z):
        print("not implemented yet")
    
    def from_input(self, inputfile):
        # reads 2-dimensional slice (z=0)
        f = open(inputfile, "r")
        lines = [l.strip() for l in f.readlines()]
        f.close()
        initial_config = {}
        for y, line in enumerate(lines):
            for x, val in enumerate(line):
                initial_config[(x,y,0)] = val
        return initial_config
    

if __name__ == '__main__':
    pp = PocketPlane("input")
    pp.advance_time(cycles=6)
    print("{} cubes active".format(len(pp.cosy)))
    