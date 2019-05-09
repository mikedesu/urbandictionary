from requests_html import HTMLSession
from sys import argv, exit


class UrbanDictionaryDefinition:
    __slots__ = ['name', 'definitions']
    def __init__(self):
        self.name = ""
        self.definitions = []
    def set_name(self,name=""):
        self.name = name
    def add_definition(self,definition):
        self.definitions.append(definition)


def print_usage():
    print("Must have an search phrase")
    print("ex: python3 urban.py poop")
    print("ex: python3 urban.py \"poop poop\"")


def main():
    if len(argv)!=2:
        print_usage()
        exit(-1)
    
    # construct the url to query
    searchPhrase = argv[1]
    url = "https://www.urbandictionary.com/define.php?term=" + searchPhrase
    
    # establish connection, get html, parse for desired tags' class/id/etc
    session = HTMLSession()
    r = session.get(url)
    meanings = r.html.find('.meaning')

    # object-oriented style...
    # create a new definition object and add its properties
    d = UrbanDictionaryDefinition()
    d.set_name(searchPhrase)
    for meaning in meanings:
        d.add_definition(meaning.text)

    for definition in d.definitions:
        print(definition)
        print("----------")

if __name__ == '__main__':
    main()

