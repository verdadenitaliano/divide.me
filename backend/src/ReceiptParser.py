import re
from backend.src.parser_files import ReceiptDoc

class ReceiptParser(ReceiptDoc):
    def __init__(self, text):
        ReceiptDoc.__init__(self, text)

    def parse(self):
        return self.get_items()


    # def get_itemName(self):
    #     # item_pattern = "(\s+([A-Za-z0-9]+\s+)+)\$([+-])?"
    #     item_pattern = "(\w[A-Za-z\s]+)\s+\$([\d.]+)"  # new regular expression to capture item and amount at the same time
    #     items = re.findall(item_pattern, self.text)
    #
    #     if len(items) > 0:
    #         # items_dict =
    #         items_list = list(items)
    #         print(type(items_list[0]))
    #         return items_list

    # def get_itemAmount(self):
    #     item_pattern = "([0-9]+\.[0-9]+)"
    #     items = re.findall(item_pattern, self.text)
    #     items
    #     if len(items) > 0:
    #         items_list = list(items)
    #         return items_list

    def get_items(self):
        #pattern = r'(.+?)\s+\$([\d.]+)
        pattern = r'(\w[A-Za-z\s]+)\s+\$([\d.]+)'
        matches = re.findall(pattern, self.text, re.DOTALL)

        item_list = []
        total = 0.0
        total_found = False

        for match in matches:
            description = match[0].strip()
            price = float(match[1])
            if description.lower() == 'total':
                total_found = True
                total = price
                break
            item_list.append({"description": description, "price": price})

        if not total_found:
            print("WARNING: 'TOTAL' not found in the text")

        items_dict = {
            "items": item_list,
            "total": total
        }
        return items_dict


if __name__ == '__main__':
    document_text = '''
    MARCHE FU TAT

6700 COTE-OES-NEIGES UNIT 2090
MONTREAL H39 2A2

« §t4- ~ if
TELa: §14-739 me
8/13/2023 3:42:20 PM

CANDAESA .YUCA
CASSAVE FRAIS CONGELE

CASHIER 1

$11.99 -
Feng ;
CORTANDRE $1.99
CRIOUA YOUL! POTATO $7.99
SH
MELANGE 3 LEGUMES $2.99
Viande AYER $8.22
Viande pysy $11.65
TOTAL $44.83
Debit card $44.83
Tten count: ¢
8/13/2023 3:42:20 py CASHIER 1
trans: 760650

Terminal :050001002-001002

x MARCHE FU TAT
6709 DE LA COTE-DES-NETGE
MONTREAL ac
Nid ACHAT
1 Conte INTERAC DEF AL) 
Tota} DEFAUT $44.83
i
HERG CARTE UEKI T
pe lye3 19:42:45 |
raf -001-001-605-9
CODE Appa. H84107293-0 esceae
jitorac
AoddOGog79
8oBd00ggQ9 20

00 APPROUVEE — MERCY 001

Cope CLIENT
Trans: 760650 Terminal :050001002-001002
Aucun Remboursenent et Seulen
Chang2z Dang 24 Heures
Merci Da! Nouveau

LYRE D Pit ys Ly SEAR ae Cra ee
, HANA LRETSiokeniee
PRT ese: wy

70 Whi.

MARCHE FU TAT

DTE-DES- HCI

TOTAL
Debit

80 APPmouvEE - MERCK 001
    '''
    invoice_parsed = ReceiptParser(document_text)
    print(invoice_parsed.parse())
