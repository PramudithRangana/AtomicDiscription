from Accessories import reversed_script as rs, script as sc


class ElectronicConfigurator:
    def __init__(self):
        self.sub_orbital_priority = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d',
                                     '5p', '6s', '4f', '5d', '6p', '7s', '5f', '6d', '7p', '8s']

        self.sub_orbital_calibration = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6, 2]

        self.atomic_calibre = []
        self.elem_calibre = []
        self.reformatted = []
        self.static_lst = []

    def stimulated_calibre(self, atomicNumber):
        atomicCalibration = self.orbital_filling(atomicNumber)

        try:
            j = 0
            for i in range(len(atomicCalibration)):
                x = ','.join([f'{self.sub_orbital_priority[j]}{sc.sup_script(atomicCalibration[j])}'])
                j = j + 1  # index increasing
                self.elem_calibre.append(x)

            last_quantum_no = ((self.elem_calibre[len(self.elem_calibre) - 1])[0])
            last_2_quantum_no = ((self.elem_calibre[len(self.elem_calibre) - 2])[0])

            for_d_block = ['2p²', '3p²', '4p²', '5p²', '6p²', '7p²', '2p⁵', '3p⁵', '4p⁵', '5p⁵', '6p⁵', '7p⁵',
                           '3d⁴', '4d⁴', '5d⁴', '6d⁴', '3d⁹', '4d⁹', '5d⁹', '6d⁹',
                           '4f⁶', '5f⁶', '4f¹³', '5f¹³']

            # check last two indexes are '4s and 4p or 4d or 5d etc.'
            if (self.elem_calibre[len(self.elem_calibre) - 1] in for_d_block) and \
                    ((self.elem_calibre[len(self.elem_calibre) - 2])[1]) == 's' and (
                    last_2_quantum_no > last_quantum_no):

                lst_1 = self.elem_calibre[len(self.elem_calibre) - 1]
                lst_2 = self.elem_calibre[len(self.elem_calibre) - 2]

                # get super script number(s) for resetting
                a1 = (int(rs.reversed_sup_script(lst_1[2:])) + 1)
                a2 = (int(rs.reversed_sup_script(lst_2[2:])) - 1)

                self.static_lst.append(a2)
                self.static_lst.append(a1)

                index_num = [lst_2[:2], lst_1[:2]]
                index = 0

                for i in self.static_lst:
                    x_1 = ','.join([f'{index_num[index]}{sc.sup_script(i)}'])
                    index += 1
                    self.reformatted.append(x_1)

                final_lst = (self.elem_calibre[:(len(self.elem_calibre) - 2)]) + self.reformatted

                return {f"Electronic Calibration": f"{', '.join([n for n in final_lst])}"}

            else:
                return {f"Electronic Calibration": f"{', '.join([n for n in self.elem_calibre])}"}
        except Exception as e:
            raise e

        finally:
            self.atomic_calibre.clear()
            self.elem_calibre.clear()
            self.reformatted.clear()
            self.static_lst.clear()

    def orbital_filling(self, nm):
        atom_num = int(nm)
        remainder = 0

        if atom_num <= 2:
            self.atomic_calibre.append(atom_num)
        else:
            for i in self.sub_orbital_calibration:
                atom_num = atom_num - i

                if atom_num < 0:
                    self.atomic_calibre.append(remainder)
                    break
                else:
                    if atom_num == 0:
                        continue
                    else:
                        remainder = atom_num
                        self.atomic_calibre.append(i)

        return self.atomic_calibre
