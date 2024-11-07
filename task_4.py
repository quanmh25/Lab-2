import xml.dom.minidom as minidom

with open("currency.xml", mode = 'r') as xml_file:
    xml_data = xml_file.read()

    dom = minidom.parseString(xml_data)
    dom.normalize()

    elements = dom.getElementsByTagName("Currency")
    currency_dict = {}

    for node in elements:
        name, value = None, None
        for child in node.childNodes:
            if child.nodeType == 1:
                if child.tagName == "Name":
                    if child.firstChild.nodeType == 3:
                        name = child.firstChild.data
                if child.tagName == "Value":
                    if child.firstChild.nodeType == 3:
                        value = float(child.firstChild.data)
        if name and value is not None:
            currency_dict[name] = value

        if node.getAttribute('id') == 'bk106':
            print(node.getElementsByTagName('Name')[0].firstChild.data)

    print(currency_dict)
    for key in currency_dict.keys():
        print(key, currency_dict[key])