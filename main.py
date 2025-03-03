import json


OFFERS_FILE = "offers.json"
PRODUCTS_FILE = "products.json"
CUSTOMERS_FILE = "customers.json"


def load_data(filename):
    """Load data from a JSON file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Error decoding {filename}. Check file format.")
        return []


def save_data(filename, data):
    """Save data to a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


# TODO: Implementirajte funkciju za kreiranje nove ponude.
def create_new_offer(offers, products, customers):
    """
    Prompt user to create a new offer by selecting a customer, entering date,
    choosing products, and calculating totals.
    """
    # Omogućite unos kupca
    print('Unesite kupca:')
    for i, customer in enumerate(offers):
        print(f'{i + 1}. {customer['customer']}')
        
    customer_index = int(input('Unesite broj željenog kupca: '))
    selected_customer = offers[customer_index]
    
    # Unos datuma
    date = input('Unesite datum: ')
    
    # Biranje proizvoda
    print('Odaberite proizvod:')
    for i, product in enumerate(products):
        print(f'{i + 1}. {product['name']} = {product['price']}')
        
    # Izračunajte sub_total, tax i total
    product_index = int(input("Unesite broj proizvoda: ")) - 1
    selected_product = products[product_index]
    
    total = selected_product['price']

    # Dodajte novu ponudu u listu offers
    new_offer = {
        'customer': selected_customer,
        'date': date,
        'product': selected_product,
        'total': total
                 }
    offers.append(new_offer)
    print("Ponuda je uspješno kreirana!")
    
    pass


# TODO: Implementirajte funkciju za upravljanje proizvodima.
def manage_products(products):
    """
    Allows the user to add a new product or modify an existing product.
    """
    # Omogućite korisniku izbor između dodavanja ili izmjene proizvoda
    print('Odaberite broj "1" kako bi dodali proizvod ili broj "2" kako bi izmijenili postojeći proizvod: ')
    choice = int(input('Unesite broj: '))
     
    # Za dodavanje: unesite podatke o proizvodu i dodajte ga u listu products
    if choice == 1:
        name = input("Unesite naziv proizvoda: ")
        price = float(input("Unesite cijenu proizvoda: "))
        new_product = {'name': name, 'price': price}
        products.append(new_product)
        print(f"Proizvod '{name}' je uspješno dodan!")
    # Za izmjenu: selektirajte proizvod i ažurirajte podatke
    elif choice == 2:
        print("Dostupni proizvodi:")
        for i, product in enumerate(products):
            print(f"{i + 1}. {product['name']} - {product['price']}")
            product_index = int(input("Unesite broj proizvoda za izmjenu: ")) - 1
            
        if 0 <= product_index < len(products):
            new_name = input("Unesite novi naziv proizvoda: ")
            new_price = input("Unesite novu cijenu proizvoda: ")

            if new_name:
                products[product_index]['name'] = new_name
            if new_price:
                products[product_index]['price'] = float(new_price)

            print("Proizvod je uspješno ažuriran!")
        else:
            print("Nevažeći odabir proizvoda!")

    pass


# TODO: Implementirajte funkciju za upravljanje kupcima.
def manage_customers(customers):
    """
    Allows the user to add a new customer or view all customers.
    """
    # Za dodavanje: omogući unos imena kupca, emaila i unos VAT ID-a
    # Za pregled: prikaži listu svih kupaca
    pass


# TODO: Implementirajte funkciju za prikaz ponuda.
def display_offers(offers):
    """
    Display all offers, offers for a selected month, or a single offer by ID.
    """
    # Omogućite izbor pregleda: sve ponude, po mjesecu ili pojedinačna ponuda
    # Prikaz relevantnih ponuda na temelju izbora
    pass


# Pomoćna funkcija za prikaz jedne ponude
def print_offer(offer):
    """Display details of a single offer."""
    print(f"Ponuda br: {offer['offer_number']}, Kupac: {offer['customer']['name']}, Datum ponude: {offer['date']}")
    print("Stavke:")
    for item in offer["items"]:
        print(f"  - {item['product_name']} (ID: {item['product_id']}): {item['description']}")
        print(f"    Kolicina: {item['quantity']}, Cijena: ${item['price']}, Ukupno: ${item['item_total']}")
    print(f"Ukupno: ${offer['sub_total']}, Porez: ${offer['tax']}, Ukupno za platiti: ${offer['total']}")


def main():
    # Učitavanje podataka iz JSON datoteka
    offers = load_data(OFFERS_FILE)
    products = load_data(PRODUCTS_FILE)
    customers = load_data(CUSTOMERS_FILE)

    while True:
        print("\nOffers Calculator izbornik:")
        print("1. Kreiraj novu ponudu")
        print("2. Upravljanje proizvodima")
        print("3. Upravljanje korisnicima")
        print("4. Prikaz ponuda")
        print("5. Izlaz")
        choice = input("Odabrana opcija: ")

        if choice == "1":
            create_new_offer(offers, products, customers)
        elif choice == "2":
            manage_products(products)
        elif choice == "3":
            manage_customers(customers)
        elif choice == "4":
            display_offers(offers)
        elif choice == "5":
            # Pohrana podataka prilikom izlaza
            save_data(OFFERS_FILE, offers)
            save_data(PRODUCTS_FILE, products)
            save_data(CUSTOMERS_FILE, customers)
            break
        else:
            print("Krivi izbor. Pokusajte ponovno.")


if __name__ == "__main__":
    main()
