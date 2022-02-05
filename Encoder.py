def clean_the_string(string):
    """
    Removes any unwanted things in that string like umlaute, special characters, \n and double whitespace.
    :param string: string to clean
    :return: cleaned string
    """

    #    string.encode("UTF-8")

    string = string.replace("ü", "ue")
    string = string.replace("Ü", "Ue")
    string = string.replace("ä", "ae")
    string = string.replace("Ä", "Ae")
    string = string.replace("ö", "oe")
    string = string.replace("Ö", "Oe")
    string = string.replace("ß", "ss")
    string = string.replace(",", " ")
    string = string.replace(".", " ")
    string = string.replace("!", " ")
    string = string.replace("?", " ")
    string = string.replace(":", " ")
    string = string.replace(";", " ")
    string = string.replace("-", " ")
    string = string.replace("_", " ")
    string = string.replace(")", " ")
    string = string.replace("(", " ")
    string = string.replace("\n", " ")
    string = string.replace("  ", " ")

    return string


print(
    "This the 'TxtFileEncoder 1.0', please enter the name of the file "
    "you would like to encode like this 'Examplefile.txt' \n "
)


txtfile = input("Name of the txt file to Encode:")
fh = open(txtfile)

print(fh)


fhlist = [line for line in fh]

fh_string = "".join(fhlist)

clean_the_string(fh_string)

lowerd_clean_string = fh_string.lower()

print(lowerd_clean_string)
