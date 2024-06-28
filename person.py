import random

class Person: 
    persons = []
    chooses_persons = []

    def __init__(self,id):
        self.id = id
        self.x = random.uniform(0,100)
        self.y = random.uniform(0,100)
        Person.persons.append(self) 

    @classmethod
    def get_all_persons(cls):
        return cls.persons
    
    @classmethod
    def get_all_chooses_persons(cls):
        return cls.chooses_persons
    
    @classmethod
    def choose(cls):
        while True:
            choosed_person_id = random.randint(0,17)
            cls.chooses_persons.append(cls.persons[choosed_person_id])
            if len(set(cls.chooses_persons)) == 3: 
                break
   
    @classmethod
    def middle_point(cls): 
        middle_point_list = []
        a = cls.chooses_persons[0]
        b = cls.chooses_persons[1]

        middle_x = int ((a.x + b.x) / 2)
        middle_y = int ((a.y + b.y) / 2)
        middle_point_list.append(middle_x)
        middle_point_list.append(middle_y)
        
        return middle_point_list

    @classmethod
    def get_step_count_and_distance(cls):
        c = cls.chooses_persons[2]

        middle_points = cls.middle_point()
        middle_x = middle_points[0]
        middle_y = middle_points[1]
        
        distance = ((c.x - middle_x) ** 2 + (c.y - middle_y) ** 2) ** 0.5
        step_meter = 0.2
        step_count = int (distance / step_meter)

        return step_count, distance
