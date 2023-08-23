import xml.etree.ElementTree as ET
import xml.dom.minidom

str = {}

# Tworzenie elementu "document" jako głównego elementu
document = ET.Element("document")
document.set("type", "order")

# Tworzenie elementu "head"
head = ET.SubElement(document, "head")

# Tworzenie elementu "author" z atrybutami
"""nazwa_elementu =ET.SubElement(rodzic, "nazwa_elementu")"""
author = ET.SubElement(head, "author")
"""dodanie atrybutu author.set("nazwa_atrybutu", "wartosc_atrybutu")"""
author.set("description", "TruTops Calculate")
author.set("authorversion", "18.0.0 build 3699")

# Tworzenie elementu "datetime" z tekstem
datetime = ET.SubElement(head, "datetime")
datetime.text = "2023-06-20 14:09:20"

# Tworzenie elementu "body"
body = ET.SubElement(document, "body")

# Tworzenie elementu "Options" wewnątrz "body" z atrybutami
options = ET.SubElement(body, "Options")
options.set("CalculationType", "PRE")
options.set("Measure", "metric")
options.set("BaseCurrency", "EUR")

# Tworzenie elementów potomnych dla "Options"
user = ET.SubElement(options, "User")
currency2 = ET.SubElement(options, "Currency2")
currency2.text = "EUR"
currency2_active = ET.SubElement(options, "Currency2Active")
currency2_active.text = "0"
currency2_exchange = ET.SubElement(options, "Currency2Exchange")
currency2_exchange.text = "1.000000"
charge_scrap = ET.SubElement(options, "ChargeScrap")
charge_scrap.text = "0"
setup_costs_surcharge = ET.SubElement(options, "SetupCostsSurcharge")
setup_costs_surcharge.text = "0"

# Tworzenie elementu OrderData
order_data = ET.SubElement(body, "OrderData")

# Tworzenie elementu CustomerData
customer_data = ET.SubElement(order_data, "CustomerData")
customer_id = ET.SubElement(customer_data, "id")
customer_id.text = "0"

# Tworzenie pozostałych elementów
quotation_no = ET.SubElement(order_data, "QuotationNo")
customer_order_no = ET.SubElement(order_data, "CustomerOrderNo")
production_order_no = ET.SubElement(order_data, "ProductionOrderNo")
article_id = ET.SubElement(order_data, "ArticleID")
article_id.text = "1"
article_uuid = ET.SubElement(order_data, "ArticleUuid")
article_uuid.text = "{458d1a1b-c7a9-4aed-91b8-bd0a921452a9}"
quantity = ET.SubElement(order_data, "Quantity")
quantity.text = "1.000000"

# Tworzenie elementu Operator
operator = ET.SubElement(order_data, "Operator")

price_fluctuation_agio = ET.SubElement(operator, "PriceFluctuationAgio")
price_fluctuation_agio.text = "0.000000"

foliation_agio = ET.SubElement(operator, "FoliationAgio")
metric_qty = ET.SubElement(foliation_agio, "metric_qty")
metric_qty.set("unit", "EUR/m²")
metric_qty.text = "0.000000"
inch_qty = ET.SubElement(foliation_agio, "inch_qty")
inch_qty.set("unit", "EUR/ft²")
inch_qty.text = "0.000000"

electric_energy_costs = ET.SubElement(operator, "ElectricEnergyCosts")
metric_qty = ET.SubElement(electric_energy_costs, "metric_qty")
metric_qty.set("unit", "EUR/kWh")
metric_qty.text = "0.150000"
inch_qty = ET.SubElement(electric_energy_costs, "inch_qty")
inch_qty.set("unit", "EUR/kWh")
inch_qty.text = "0.150000"

compressed_air = ET.SubElement(operator, "CompressedAir")
description = ET.SubElement(compressed_air, "Description")
description.text = "Druckluft"
costs = ET.SubElement(compressed_air, "Costs")
metric_qty = ET.SubElement(costs, "metric_qty")
metric_qty.set("unit", "EUR/Nm³")
metric_qty.text = "0.080000"
inch_qty = ET.SubElement(costs, "inch_qty")
inch_qty.set("unit", "EUR/scf")
inch_qty.text = "0.002265"

oxygen = ET.SubElement(operator, "Oxygen")
description = ET.SubElement(oxygen, "Description")
description.text = "O2"
costs = ET.SubElement(oxygen, "Costs")
metric_qty = ET.SubElement(costs, "metric_qty")
metric_qty.set("unit", "EUR/Nm³")
metric_qty.text = "1.490000"
inch_qty = ET.SubElement(costs, "inch_qty")
inch_qty.set("unit", "EUR/scf")
inch_qty.text = "0.042192"

nitrogen = ET.SubElement(operator, "Nitrogen")
description = ET.SubElement(nitrogen, "Description")
description.text = "N2"
costs = ET.SubElement(nitrogen, "Costs")
metric_qty = ET.SubElement(costs, "metric_qty")
metric_qty.set("unit", "EUR/Nm³")
metric_qty.text = "0.350000"
inch_qty = ET.SubElement(costs, "inch_qty")
inch_qty.set("unit", "EUR/scf")
inch_qty.text = "0.009911"

argon = ET.SubElement(operator, "Argon")
description = ET.SubElement(argon, "Description")
description.text = "Argon"
costs = ET.SubElement(argon, "Costs")
metric_qty = ET.SubElement(costs, "metric_qty")
metric_qty.set("unit", "EUR/Nm³")
metric_qty.text = "3.440000"
inch_qty = ET.SubElement(costs, "inch_qty")
inch_qty.set("unit", "EUR/scf")
inch_qty.text = "0.097410"

##########################################

# Konwersja do tekstu z wcięciami i znakami nowej linii
xml_str = ET.tostring(document, encoding="utf-8")
dom = xml.dom.minidom.parseString(xml_str)
pretty_xml_str = dom.toprettyxml(indent="  ")
# Zapisywanie do pliku XML
with open("nazwa_pliku.xml", "w") as f:
    f.write(pretty_xml_str)


################################################################
# mydoc = xml.dom.minidom.parse('wycena_z_geo_xml.xml')
# items = mydoc.getElementsByTagName('CalculationType')

tree = ET.parse('wycena_z_geo_xml.xml')   # import xml from
root = tree.getroot()
# tree = ET.parse('test2.xml')   # import xml from
# root = tree.getroot()

# deklaracja temp slownika
dict = {}

Panelist_list = []
# './body/Options
for item in root.findall('./head'):    # find all projects node
    Panelist = {}              # dictionary to store content of each projects
    panelist_login = item.attrib
    # make panelist_login the first key of the dict
    Panelist.update(panelist_login)
    for child in item:
        print(child)  # debug
        panelist_login2 = child.attrib
        Panelist[child.tag] = child.text
        for atrib in panelist_login2:
            print(atrib)  # debug
            value = panelist_login2[atrib]
            dict[atrib] = value
            # Panelist[child.tag] = ("atrib", "sfsfds")
            Panelist[child.tag] = dict
            # Panelist_list[child.tag] = {"atrib": "sfsfds"}
    Panelist_list.append(Panelist)
print(Panelist_list)


# based on Panelist_list create xml file:

# Tworzenie elementu "document" jako głównego elementu
document = ET.Element("document")
document.set("type", "order")

for A in Panelist_list:
    print(A)
    res = list(A.keys())[0]
    # print(str(res))
    for new_s, new_val in A.items():
        # print first key
        # create dynamicaly variable name like key
        Dynami_variable_name = new_s
        locals()[Dynami_variable_name] = ET.SubElement(head, new_s)
        print(new_s)
    for B in A:
        print(A[B])
        # if type(A[B]) == dict:
        for new_s2, new_val2 in A[B].items():
            # print first key
            Dynami_variable_name.set(new_s2, new_val2)
            print(new_s)
        for C in A[B]:
            if type(C) == dict:
                for new_s, new_val in C.items():
                    # print first key
                    print(new_s)
            # if not isinstance(C, str):
            # print(type(A[B]))
            # if not type(A[B]) is str:
            if type(A[B]) == dict:
                print(C)


# Tworzenie elementu "head"
head = ET.SubElement(document, "head")
# Tworzenie elementu "author" z atrybutami
"""nazwa_elementu =ET.SubElement(rodzic, "nazwa_elementu")"""
author = ET.SubElement(head, "author")
"""dodanie atrybutu author.set("nazwa_atrybutu", "wartosc_atrybutu")"""
author.set("description", "TruTops Calculate")
author.set("authorversion", "18.0.0 build 3699")

# Tworzenie elementu "datetime" z tekstem
datetime = ET.SubElement(head, "datetime")
datetime.text = "2023-06-20 14:09:20"

# # one specific item attribute
# print('Item #2 attribute:')
# print(items[1].attributes['CalculationType'].value)

# # all item attributes
# print('\nAll attributes:')
# for elem in items:
#     print(elem.attributes['CalculationType'].value)

# # one specific item's data
# print('\nItem #2 data:')
# print(items[1].firstChild.data)
# print(items[1].childNodes[0].data)

# # all items data
# print('\nAll item data:')
# for elem in items:
#     print(elem.firstChild.data)
