#  Write a function that will return a string of country codes from an argument
#  that is a string of prices (containing dollar amounts following the country
#  codes). Your function will take as an argument a string of prices like the
#  following: "US$40, AU$89, JP$200". In this example, the function would
#  return the string "US, AU, JP".
#
#  Hint: You may want to break the original string into a list, manipulate the
#  individual elements, then make it into a string again.


def get_country_codes(prices):
    price_list = prices.split(", ")
    for i in range(len(price_list)):
        price_list[i] = price_list[i][:price_list[i].find('$')]
    return ', '.join(price_list)


def testEqual(a, b):
    if a == b:
        print("Pass")
    else:
        print("Fail")


def main():
    """ Cursory test of get_country_codes(prices) """

    testEqual(get_country_codes("NZ$300, KR$1200, DK$5"), "NZ, KR, DK")
    testEqual(get_country_codes("US$40, AU$89, JP$200"), "US, AU, JP")
    testEqual(get_country_codes("AU$23, NG$900, MX$200, BG$790, ES$2"),
              "AU, NG, MX, BG, ES")
    testEqual(get_country_codes("CA$40"), "CA")


if __name__ == '__main__':
    main()
