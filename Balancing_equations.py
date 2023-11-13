import chemparse
import numpy as np

class Equation:
    # Base class for all chemical equasions
    def __init__(self,equation):
        # Creates an instance of a class
        self.equation = equation

    def compound_to_dict(self,compound):
        # This converts an input compound (ex. H2O) into dict, 
        # where the keys represents symbols/elements and values represents quantity of single elements (ex. {'H': 2, 'O': 1})
        return chemparse.parse_formula(compound)
    
    def input(self):
        self.data = []
        self.right = []
        subs_and_prod = list(self.equation.split('->'))
        for i in range(0,2): 
            reagents = [x for x in subs_and_prod[i].split('+')]
            for substance in reagents:
                elements = self.compound_to_dict(substance)
                self.data.append(elements)
                if i == 1:
                    self.right.append(elements)
        return self.data 
    
    def solve(self):
        keys = set()
        values_matrix_A = []
        values_matrix_B = []
        for reagents in self.data:
            for i in reagents.keys():
                keys.add(i)

        for reagent in range(0,len(self.data)-1):
            for i in keys:
                if i in self.data[reagent] and self.data[reagent] not in self.right:
                    values_matrix_A.append(self.data[reagent][i])
                elif i in self.data[reagent] and self.data[reagent] in self.right:
                    values_matrix_A.append(self.data[reagent][i]*(-1))
                else: values_matrix_A.append(0)

        for i in keys:
            if i in self.data[-1]:
                values_matrix_B.append(self.data[-1][i])
            else: values_matrix_B.append(0)        
        

        matrix_A = np.matrix(values_matrix_A).reshape(len(keys),len(keys))
        matrix_A = matrix_A.transpose()

        matrix_B = np.matrix(values_matrix_B).reshape(len(keys),1)
        det_A = np.linalg.det(matrix_A)
        inv_mat_A = np.linalg.inv(matrix_A)

        solution = inv_mat_A*matrix_B*det_A
        solution = solution.tolist()
        solution.append([det_A])

        return f'stoichiometric coefficients: {solution}'

# This would create objects of Equation class
reaction_1=Equation('H2+O2->H2O')
reaction_2=Equation('SnO2+H2->Sn+H2O')

reaction_1.input()
print(reaction_1.solve())

reaction_2.input()
print(reaction_2.solve())