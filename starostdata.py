import pandas as pd

# Список старост и людей, уполномоченных отмечать группу
starosts = [
#('neeck_kola','Шмитьков Николай', 'ККСО-03-21'),
('134','Игнат', 'ККСО-03-21'),
('3456','желемых', 'ККСО-03-21'),
('234','пмитьков Николай', 'ККСО-03-21'),
('756','кмитьков Николай', 'ККСО-03-21'),
('gdrg','ермитьков Николай', 'ККСО-03-21'),
('fjyr','укитьков Николай', 'ККСО-03-21'),
             ]

# Create a DataFrame object from list
df = pd.DataFrame(starosts,
                  columns=['Id', 'Имя','Группа'])

