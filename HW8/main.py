
import journal

user = input('Teacher or student? [t/s]: ')

if user == 't':
    more = 'yes'
    while more == 'yes':
        surname = input('Enter surname: ')
        subject = input('Enter subject: ')
        mark = int(input('Enter mark: '))
        journal.add_mark(surname, subject, mark)
        more = input('Do you want to add another mark? [yes/no]: ')
elif user == 's':
    surname = input('Enter surname: ')
    marks = journal.get_marks(surname)
    for subject in marks:
        print(f'{subject} - {", ".join(map(str, marks[subject]))}')
