
def get_marks(surname):
    all_marks = {}
    with open(f'students/{surname.lower()}.csv', 'r') as marks:
        for line in marks:
            subject, mark = line.split(',')
            mark = int(mark)
            if subject in all_marks:
                all_marks[subject].append(mark)
            else:
                all_marks[subject] = [mark]
    return all_marks

def add_mark(surname, subject, mark):
    with open(f'students/{surname.lower()}.csv', 'a') as marks:
        marks.write(f'{subject.lower()},{mark}\n')
