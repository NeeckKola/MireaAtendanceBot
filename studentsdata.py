import pandas as pd

# Список подписавшихся студентов
students = [
#('neeck_kola', 'ККСО-03-21'),
]

df = pd.DataFrame(students,
                  columns=['id', 'Группа'])
