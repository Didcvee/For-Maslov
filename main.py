import csv

csv_file_path = 'owid-covid-data.csv'
output_csv_file_path = 'output_results.csv'  # Укажите путь к выходному CSV файлу

datas = ['2023-11-30', '2023-11-29', '2023-11-28', '2023-11-27', '2023-11-26', '2023-11-25', '2023-11-24', '2023-11-23']

# Открываем CSV-файл для чтения
with open(csv_file_path, 'r') as file, open(output_csv_file_path, 'w', newline='') as output_file:
    csv_reader = csv.reader(file)
    csv_writer = csv.writer(output_file)
    mercedes = []

    # Записываем заголовок в выходной файл
    csv_writer.writerow(['ISO Code', 'Location', 'population', 'New_cases',  'Percentage', 'RT'])

    # Проходим по каждой строке в CSV
    for row in csv_reader:

        if row[3] in datas:
            if(row[5]==''):
                mercedes.append(0)
            else:
                mercedes.append(row[5])
         # Проверяем значение в нужном столбце (подставьте нужный номер столбца, начиная с 0)
            if row[3] == datas[0]:
            # Выполняем действия с соответствующей строкой
                iso_code = row[0]
                location = row[2]
                total_cases = row[4]
                population = row[62]
                if total_cases == '':
                    percent = 0
                else:
                    percent = round(float(total_cases) / float(population) * 100, 2)
                if float(mercedes[3])+float(mercedes[2])+float(mercedes[1])+float(mercedes[0]) == float(0):
                    result = 0
                elif (float(mercedes[7])+float(mercedes[6])+float(mercedes[5])+float(mercedes[4])) == float(0):
                    result = 0
                else:
                    result = (float(mercedes[7])+float(mercedes[6])+float(mercedes[5])+float(mercedes[4]))/float(mercedes[3])+float(mercedes[2])+float(mercedes[1])+float(mercedes[0])

            # Записываем результат в выходной файл
                csv_writer.writerow([iso_code, location, population, total_cases, percent, result])
                print(mercedes)
                mercedes = []

# Выбор модели
# Выбор модели в первую очередь зависит от цели: регрессия, классификация или кластеризация. В данной задачи нужно клссифицировать письма и отправлять их определенныйм людям,
# здесь применимы классфикация и кластеризация, но возможной большой разницы в темах писем кластеризация будет не эффективна, следсвенно наилучши выором является классифицируюшая модель.
#
# Мною было предположено 4 варианта реализации классифицирюшей модели модели:
# 1.RandomForestClassifier 2.Нейросеть реализованная на keras
# 3.ExtraTreesClassifier
# 4.GradientBoostingClassifier


# Основной ограничваюший фактор данной задачи - размер датасета.
# Данная проблема наиболее сильно отразится на нейросети(2), для эффективного обучения она требует в 10 раз большее размеры данных.
# Также данная пролема может отразится на RandomForestClassifier(1) из за треования алогритма делить данные на несколько частей.
# ExtraTreesClassifier(3) и GradientBoostingClassifier(4) лучше всего показывают себя на небольших датасетах из за алогоритмов основываюшихся на случайности.
# Из за технических ограничений так-же важна и скорость обучения, в которой выиграыет ExtraTreesClassifier(3), т.к. после первой итерации обучения показывет приемлемый результат.

#создание обекта модели
from sklearn.ensemble import ExtraTreesClassifier
classifier = ExtraTreesClassifier(n_estimators=100, random_state=0)


