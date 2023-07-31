import json
import electroConfig as eleC

ec = eleC.ElectronicConfigurator()


class PeriodicTableAnalyzer:
    def __init__(self):
        self.periodic_element = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S',
                                 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn',
                                 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru',
                                 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce',
                                 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf',
                                 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn',
                                 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm',
                                 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Uut', 'Fl',
                                 'Uup', 'Lv', 'Uus', 'Uuo']

    @staticmethod
    def find_block(json_value, atomic_symbol):
        e_block = ''
        e_group = ''
        try:
            g = (json_value[atomic_symbol]["Group"])

            try:
                e_group = int(g)
            except:
                e_group = g
            finally:
                if e_group == '-':
                    e_block = 'f'
                elif e_group < 3:
                    e_block = 's'
                elif e_group >= 13:
                    e_block = 'p'
                elif 2 < e_group < 13:
                    e_block = 'd'

                return {"Block": f"{e_block}"}

        except KeyError:
            print(f"[ Block not detected ] Unknown Element '{atomic_symbol}'")
        except IndexError as ie:
            print(f"[+ find_block ] (May be some list should be clear !); Error : ", ie)
        except Exception as e:
            print('[+ find_block ] Error : ', e)

    @staticmethod
    def find_key_value(atomic_symbol):
        try:
            with open('../source_file/periodic_tbl.json', 'r') as fh:
                json_str = fh.read()
                json_value = json.loads(json_str)
                j_v = json_value[atomic_symbol]

                return json_value, j_v

        except KeyError:
            print(f"[ Details not detected ] Unknown Element '{atomic_symbol}'")
            return KeyError

        except Exception as e:
            print('[+ find_key_value ]Error : ', e)

    @classmethod
    def periodic_view(cls):
        print('''
                          Elements of Periodic Table
        
            1  2  3  4  5  6  7  8  9  10 11 12 13  14 15  16 17  18

            H                                                     He
            Li Be                               B   C  N   O  F   Ne
            Na Mg                               Al  Si P   S  Cl  Ar
            K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga  Ge As  Se Br  Kr
            Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In  Sn Sb  Te I   Xe
            Cs Ba    Hf Ta W  Re Os Ir Pt Au Hg Tl  Pb Bi  Po At  Rn
            Fr Ra    Rf Db Sg Bh Hs Mt Ds Rg Cn Uut Fl Uup Lv Uus Uuo

                     La Ce Pr Nd Pm Sm Eu Gd Tb Dy  Ho Er  Tm Yb  Lu
                     Ac Th Pa U  Np Pu Am Cm Bk Cf  Es Fm  Md No  Lr
                     
                                          - Dimitri Mendeleev (1981)

        ''')


print("""
    [+] Write as "Periodic" for view Periodic Table
    [+] Write the Symbol of the Element which you need to get details
    [+] Write as "Exit" for Exit from the Program    
""")
