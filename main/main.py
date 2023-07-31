import basicConfig as bC
import electroConfig as eC
import traceback

pta = bC.PeriodicTableAnalyzer()
eleC = eC.ElectronicConfigurator()


class DetailsPreviewer:
    def __init__(self, atomicSymbol):
        self.atomic_symbol = atomicSymbol

    def dataAssemble(self):
        try:
            json_val, basicDetail = pta.find_key_value(self.atomic_symbol)

            fb = pta.find_block(json_val, self.atomic_symbol)
            basicDetail.update(fb)

            sc = eleC.stimulated_calibre(json_val[self.atomic_symbol]["Atomic Number"])
            basicDetail.update(sc)

            for key, value in basicDetail.items():
                print(f'{key.rjust(25)} : {value}')

        except ValueError:
            print(traceback.format_exc())

        except Exception as e:
            print(f"{e}")
            print(traceback.format_exc())


if __name__ == "__main__":
    while True:
        atomic_symbol = input('\n>> ').capitalize()

        if atomic_symbol == 'Exit':
            exit()
        elif atomic_symbol == 'Periodic':
            pta.periodic_view()
        else:
            dp = DetailsPreviewer(atomic_symbol)
            dp.dataAssemble()
