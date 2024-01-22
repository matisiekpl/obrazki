import csv
import json

csvfile = open('out3.csv', encoding='utf-8')

rows = []
reader = csv.reader(csvfile, delimiter=';', quotechar='"')
# next(reader)
for row in reader:
    correctness = row[6].lower()
    rows.append({
        'question': row[0],
        'answer_a': row[1],
        'answer_b': row[2],
        'answer_c': row[3],
        'answer_d': row[4],
        'answer_e': row[5],
        'answer_a_correct': correctness.find('a') != -1,
        'answer_b_correct': correctness.find('b') != -1,
        'answer_c_correct': correctness.find('c') != -1,
        'answer_d_correct': correctness.find('d') != -1,
        'answer_e_correct': correctness.find('e') != -1,
    })

with open('src/assets/questions.json', 'w', encoding='utf-8') as outfile:
    json.dump(rows, outfile, ensure_ascii=False)