class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        
        self.contacts.append(dict(zip(('id', 'name', 'phone', 'email', 'favorite'), (Contacts.current_id, name, phone, email, favorite))))
        Contacts.current_id += 1
