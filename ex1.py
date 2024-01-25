def find_way(function):
    def decorate():
        boost = function()
        way = start_speed*time + boost*end_speed/2
        return {'boost': boost, 'way': way}
    return decorate

@find_way
def find_boost():   
    try:
        boost = (end_speed - start_speed) / time
    except ZeroDivisionError:
        print("zero division time must not 0")
        exit()
    return boost

try:
    start_speed = int(input("start_speed "))
    end_speed = int(input("end_speed "))
    time = int(input("time "))
except ValueError:
    print("you must input nams")
    exit()

print(find_boost())