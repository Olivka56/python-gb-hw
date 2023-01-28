import csv

def save_contact(first_name, second_name, phone, description):
    with open('contacts.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([first_name, second_name, phone, description])
    with open('contacts.txt', 'a') as txt_file:
        writer = csv.writer(txt_file, delimiter='\n', lineterminator='\n----------\n')
        writer.writerow([first_name, second_name, phone, description])

def get_contacts():
    contacts = []
    with open('contacts.csv', newline='') as cnt:
        reader = csv.reader(cnt)
        for contact in reader:
            contacts.append(contact)
    return contacts
