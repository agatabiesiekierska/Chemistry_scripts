import chemparse
import pandas as pd

class molar_mass:
    def __init__(self, compound):
        self.compound = compound
        self.path = r'C:\Python - skrypty\Własne Projekty\Bilansowanie reakcji\Periodic Table of Elements.csv'
        self.comp_dict = self.compound_to_dict()

    def compound_to_dict(self):
        return chemparse.parse_formula(self.compound)
about:blank#blocked
    def calculate_molar_mass(self):
        df = pd.read_csv(self.path)
        elements = pd.DataFrame(columns = ['Symbol', 'AtomicMass', 'Quantity'])
        for ind in df.index:
            if df['Symbol'][ind] in self.comp_dict.keys():
                new_row = [df['Symbol'][ind], df['AtomicMass'][ind], self.comp_dict[df['Symbol'][ind]]]
                elements.loc[len(elements)] = new_row
        elements['Mass'] = elements['AtomicMass'] * elements['Quantity']
        total = elements['Mass'].sum()
        return f'Total mass of a compound {self.compound}: {total} g/mol.'




compound = molar_mass('CH')
print(compound.calculate_molar_mass())
