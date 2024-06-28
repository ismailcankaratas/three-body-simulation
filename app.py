import matplotlib.pyplot as plt
from person import Person 

persons = Person.get_all_persons()
chooses_persons = Person.get_all_chooses_persons()

for i in range(18):
    persons.insert(i, Person(i))

Person.choose()

def visualize_movement(person, target_x, target_y):
    step_count, distance = Person.get_step_count_and_distance()

    plt.figure(figsize=(8, 6))
    
    for p in chooses_persons:
        plt.plot(p.x, p.y, 'bo', markersize=8)  # Başlangıç noktaları mavi renkte
    
    plt.plot(target_x, target_y, 'ro', markersize=10)  # Hedef nokta kırmızı renkte
    
    plt.plot([chooses_persons[person].x, target_x], [chooses_persons[person].y, target_y], 'g--',label="dsa")  # Yeşil kesik çizgi
    plt.text(target_x -5, target_y -5, f'{step_count} adım')  # Adım
    plt.text((chooses_persons[person].x + target_x) / 2, (chooses_persons[person].y + target_y) / 2, f'{int(distance)} metre')  # Adım
    
    plt.title(f"{person + 1}. kişi hedefe doğru ilerliyor")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.grid(True)
    plt.show()

middle_point = Person.middle_point()
target_x = middle_point[0]
target_y = middle_point[1]

visualize_movement(2, target_x, target_y)     