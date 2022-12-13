import uuid
import utilities
import os
from datetime import date

def add_client(clients, id, name, telephone, city):
    clients[str(id)] = {
      "nume": name,
      "telefon": telephone,
      "oras": city
    }
def create_client(name, telephone, city):
    id = uuid.uuid1()
    clients = utilities.read_data_from_json("clients.json")
    add_client(clients, id, name, telephone, city)
    utilities.write_to_disk(clients, "clients.json")
    add_balance_for(id)

def add_balance_for(client_id):
    balance = utilities.read_data_from_json("bank.json")
    balance[str(client_id)] = 0
    utilities.write_to_disk(balance, "bank.json")


def get_balance(client_id):
    dictionary = utilities.read_data_from_json('bank.json')
    utilities.check_key(dictionary, client_id, "Clientul cautat nu exista!")

    return dictionary[client_id]

def cash_deposit(client_id, sum):
    bank = utilities.read_data_from_json('bank.json')
    utilities.check_key(bank, client_id, "Clientul cautat nu exista!")

    new_sum = bank[client_id] + sum
    bank[client_id] = new_sum
    utilities.write_to_disk(bank, 'bank.json')
    record_transaction(client_id, sum)

def cash_withdrawal(client_id, sum):
    bank = utilities.read_data_from_json('bank.json')
    utilities.check_key(bank, client_id, "Clientul cautat nu exista!")

    current_balance = float(bank[client_id])
    if current_balance < sum:
        raise Exception("Fonduri insuficiente pentru retragere!")

    difference = current_balance - sum
    bank[client_id] = difference
    utilities.write_to_disk(bank, "bank.json")
    transaction = -sum
    record_transaction(client_id, transaction)

def record_transaction(client_id, sum):
    transactions = utilities.read_data_from_json("extras_cont.json")
    if client_id not in transactions:
        transactions[client_id] = []
    transactions[client_id].append(sum)
    utilities.write_to_disk(transactions, "extras_cont.json")

def transfer_between_clients(sender, receiver, sum):
    bank = utilities.read_data_from_json("bank.json")
    utilities.check_key(bank, sender, f"Clientul {sender} nu exista!")
    utilities.check_key(bank, receiver, f"Clientul {receiver} nu exista!")
    if bank[sender] < sum:
        raise Exception("Fonduri insuficiente pentru a efectua transferul!")

    bank[sender] -= sum
    bank[receiver] += sum
    utilities.write_to_disk(bank, 'bank.json')
    record_transaction(sender, -sum)
    record_transaction(receiver, sum)

def generate_extras(client_id):
    clients = utilities.read_data_from_json('clients.json')
    utilities.check_key(clients, client_id, "Clientul cautat nu exista!")
    name = clients[client_id]['nume']
    phone = clients[client_id]['telefon']
    city = clients[client_id]['oras']

    folder = "Folder_extrase"
    if not os.path.exists(folder):
        os.mkdir(folder)

    extras = open(f"{folder}\\{name}_{client_id}.txt", "w+")
    today = date.today()
    transactions = utilities.read_data_from_json('extras_cont.json')
    bank = utilities.read_data_from_json('bank.json')
    description = f"Nume: {name}\n Data generarii extrasului de cont: {today}\nID unic: {client_id}\nTotal cont: {bank[client_id]}\nTelefon: {phone}\nOras: {city}\n"
    extras.writelines(description)
    extras.writelines("Tranzactii:\n")
    list = transactions[client_id]
    for value in list:
        extras.writelines(f"{value}\n")

    extras.close()
