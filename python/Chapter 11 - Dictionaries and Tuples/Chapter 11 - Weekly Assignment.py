
def sort_contacts(contact_dict):
    """
    Given a dictionary <contact_dict> of the form
        contact_dict = {name: (phone, email), etc.}
    Return a list <contact_list> sorted by name of the form
        contact_list = [(name, phone, email)]
    """

    #  Create a list of contact_dict keys (i.e., names) and sort it
    name_list = list(contact_dict.keys())
    name_list.sort()

    #  Iterate through the sorted name list and construct the contact list to
    #  be returned based on the information in the contact dictionary passed in
    contact_list = []
    for name in name_list:
        contact_list.append(
            (
                name,
                contact_dict[name][0],
                contact_dict[name][1]
            )
        )

    return contact_list


def testEqual(a, b):
    """ Home-rolled version of testEqual """

    if a == b:
        print("Pass")
    else:
        print("Fail")


def main():
    """ Cursory testing of sort_contacts(dict) """

    testEqual(sort_contacts(
        {
            "Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"),
            "Welles, Orson": ("1-312-720-8888", "orson@notlive.com"),
            "Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")
        }),
        [
            ('Freud, Anna', '1-541-754-3010', 'anna@psychoanalysis.com'),
            ('Horney, Karen', '1-541-656-3010', 'karen@psychoanalysis.com'),
            ('Welles, Orson', '1-312-720-8888', 'orson@notlive.com')
    ])

    testEqual(sort_contacts(
        {
            "Summitt, Pat": ("1-865-355-4320", "pat@greatcoaches.com"),
            "Rudolph, Wilma": ("1-410-5313-584", "wilma@olympians.com")
        }),
        [
            ('Rudolph, Wilma', '1-410-5313-584', 'wilma@olympians.com'),
            ('Summitt, Pat', '1-865-355-4320', 'pat@greatcoaches.com')
    ])

    testEqual(sort_contacts(
        {
            "Dinesen, Isak": ("1-718-939-2548", "isak@storytellers.com")
        }),
        [
            ('Dinesen, Isak', '1-718-939-2548', 'isak@storytellers.com')
    ])

    testEqual(sort_contacts(
        {
            "Rimbaud, Arthur": ("1-636-555-5555", "arthur@notlive.com"),
            "Swinton, Tilda": ("1-917-222-2222", "tilda@greatActors.com"),
            "Almodovar, Pedro": ("1-990-622-3892", "pedro@filmbuffs.com"),
            "Kandinsky, Wassily": ("1-333-555-9999", "kandinsky@painters.com")
        }),
        [
            ('Almodovar, Pedro', '1-990-622-3892', 'pedro@filmbuffs.com'),
            ('Kandinsky, Wassily', '1-333-555-9999', 'kandinsky@painters.com'),
            ('Rimbaud, Arthur', '1-636-555-5555', 'arthur@notlive.com'),
            ('Swinton, Tilda', '1-917-222-2222', 'tilda@greatActors.com')
    ])


if __name__ == "__main__":
    main()
