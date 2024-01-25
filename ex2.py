
class ChildrenPoints():
    def __init__(this, name, points) -> None:
        this.name =name
        this.points = points

    def __str__(self) -> str:
        return f"{self.name} - {self.points} баллов"

def find_best_childrens():
    best_chidren = {}

    with open("mat_dv.txt", 'r', encoding="utf-8") as file:
        for line in file:
            line_list = line.split()

            current_class = int(line_list[2])
            current_point = int(line_list[3]) + int(line_list[4])


            if ( best_chidren.get(current_class) == None ) or (best_chidren.get(current_class).points < current_point):
                children = ChildrenPoints(line_list[0] + line_list[1], current_point)
                best_chidren[current_class] = children
    return best_chidren


def found_best_in_one():
    best_math = None
    best_geom = None

    with open("mat_dv.txt", 'r', encoding="utf-8") as file:
        for line in file:
            line_list = line.split()
            current_math_point = int(line_list[3])
            current_geom_point = int(line_list[4])


            if (best_geom == None) or (best_geom.points < current_geom_point):
                best_geom = ChildrenPoints(line_list[0] + line_list[1], current_geom_point)
            
            if (best_math == None) or (best_math.points < current_math_point):
                best_math = ChildrenPoints(line_list[0] + line_list[1], current_math_point)
            
    return {'best_math ':best_math, 'best_geom' : best_geom}

bests = find_best_childrens()
for i in bests.keys():
    print(f'{i} класс: {bests[i]}')




bests = found_best_in_one()
for i in bests.keys():
    print(f'{i}: {bests[i]}')

