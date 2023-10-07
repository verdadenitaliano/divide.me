from backend.src.ReceiptParser import ReceiptParser
def test_get_items():

    rp = ReceiptParser(document_text)
    rp.get_items()


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

def test_parse(document_text):
    record_receipt = document_text.parse()
    assert record_receipt['description'[0]] == '1'