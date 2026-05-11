contacts = [
    {"name": "Ayesha Bibi",   "phone": "0301-1234567", "city": "Karachi",  "favorite": True},
    {"name": "Bilal Ahmed",   "phone": "0312-9876543", "city": "Lahore",   "favorite": False},
    {"name": "Sara Khan",     "phone": "0321-1112233", "city": "Karachi",  "favorite": True},
    {"name": "Usman Tariq",   "phone": "0333-4445566", "city": "Islamabad","favorite": False},
    {"name": "Hina Malik",    "phone": "0345-7778899", "city": "Lahore",   "favorite": True},
    {"name": "Zaid Hussain",  "phone": "0311-0001122", "city": "Karachi",  "favorite": False},
]

def format_contact(contacts):
    for contact in contacts:
        if contact["favorite"] == True:
            print(contact["name"], "|", contact["phone"], "|", contact["city"], "|", "\u2605")
        else:
            print(contact["name"], "|", contact["phone"], "|", contact["city"], "|")
    print()


def favorite_contacts():
   
    for contact in contacts:
        if contact["favorite"] == True:
            print(contact["name"], ",", contact["phone"], ",", contact["city"], ",", contact["favorite"])
    print()


def contacts_by_city(contacts, city_name):
    print("city:", city_name)
    for contact in contacts:
        if city_name == contact['city']:
            print(contact)
    print()



def count_by_name(b):
    c = 0
    for contact in contacts:
        name = contact["name"].lower()
        if b in name:
            c += 1
    return c


def search_contact(b):
    for contact in contacts:
        name = contact["name"].lower()
        if b in name:
            print(contact)
    print( count_by_name(b))
    print()


def count_by_city():
    count = {}
    for contact in contacts:
        city = contact["city"]
        if city in count:
            count[city] += 1
        else:
            count[city] = 1
    print(count)
    print()


def is_valid_phone(phone):
    if len(phone) == 12 and "-" in phone:
        parts = phone.split("-")
        if len(parts) == 2:
            if len(parts[0]) == 4 and len(parts[1]) == 7:
                return True
    return False


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    valid = is_valid_phone(phone)

    if valid:
        city = input("Enter city name: ")
        fav_input = input("True/False: ").lower()
        
        if contacts[3] == "true":
          favorite = True
        else:
         favorite = False

        contact = {"name": name, "phone": phone, "city": city, "favorite": favorite}
        contacts.append(contact)

        print("Added:", contact)
    else:
        print("invalid")
    print()


# def main_function():


def main_function():
    if choice=="a":
         format_contact(contacts)
    elif choice=="b":
         city_name = input("enter city name: ")
         contacts_by_city(contacts, city_name)
    elif choice=="c":
         a = input("enter any letter: ")
         b = a.lower()
         search_contact(b)
    elif choice=="d":
         count_by_city()
    elif choice =="e":
        add_contact()
        print(contacts)
        
    elif choice.lower() == 'exit':
        print("Thanks")
        return False
        
    else: 
         print("\nPlease Enter a Valid Choice!\n")
    
    return True


run = True
print("---MENU---\n")
while run:

    print("a: All contacts")
    print("b: Count by city")
    print("c: search by city")
    print("d: city summary")
    print("e: add contact")
    choice = input("choose anyone: ")
    print("\n")

    run = main_function()