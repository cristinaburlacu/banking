# utilities files:
# clients.txt - clienti - ID unic, nume, telefon, oras
# bank.txt - id client si balanta
# auth.txt - credentiale (user/parola functionar)
#
# Adauga clienti in fisierul clients.txt:
# --- Client: ID unic, nume, telefon, oras
# Verifica balanta pentru fiecare client in bank.txt
# Modifica balanta clientilor in bank.txt
# Faci transfer intre clienti
# Genereaza extras de cont:
# --- extrasul este generat intr-un fisier nou, numele fisierului contine numele clientului si id'ul (poate fi rescris daca cerem un extras de cont pentru acelasi client)
# — extrasul de cont ar trebui sa contina si intrarile si iesirile din acel cont
# --- extrasul de cont contine toate informatiile personale ale clientului si balanta
# --- extrasul de cont este placut estetic
# --- extrasul sa fie creat intr-un folder special



import json

from datetime import date
import os
import utilities
import banking
import sys

def show_balance():
    client_id = input("Introduceti id-ul clientului pentru care se verifica balanta: ")
    balance = banking.get_balance(client_id)
    print(f"Balanta pentru acest client este: {balance}")

def modify_balance():
    transaction = input("Ce tranzactie doriti sa efectuati:\n 1. Depunere numerar\n 2. Retragere numerar")
    client_id = input("Scrieti ID-ul unic al clientului: ")
    if transaction == "1":
        sum = float(input("Ce suma doriti sa depuneti? "))
        banking.cash_deposit(client_id, sum)
    elif transaction == "2":
        sum = float(input("Ce suma doriti sa retrageti? "))
        banking.cash_withdrawal(client_id, sum)

def add_client():
    name = input("Scrieti numele clientului: ")
    telephone = input("Scrieti telefonul clientului: ")
    city = input("Scrieti orasul clientului: ")
    banking.create_client(name, telephone, city)

def clients_transfer():
    sum = float(input("Ce suma doriti sa transferati? "))
    sender = input("Scrieti id-ul unic al clientului de la care se doreste transferul. ")
    receiver = input("Scrieti id-ul unic al clientului catre care se doreste transferul. ")
    banking.transfer_between_clients(sender, receiver, sum)

def generate_extras():
    client_id = input("Scrieti ID-ul unic al clientului: ")
    banking.generate_extras(client_id)

while True:
    try:
        option = input("Alege optiunea:\n 1.Adauga clienti\n 2.Verifica balanta pentru fiecare client\n 3.Modifica balanta clientilor\n 4.Transfer intre clienti\n 5.Generare extras de cont\n 6.Exit\n")
        if option == "1":
            add_client()
        elif option == "2":
            show_balance()
        elif option == "3":
            modify_balance()
        elif option == "4":
            clients_transfer()
        elif option == "5":
            generate_extras()
        elif option == "6":
            print("La revedere!")
            break
    except:
        e = sys.exc_info()[1]
        print(f"Operatia nu s-a putut produce. Eroare: {e}.")
