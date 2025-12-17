# Elisa KAING 21128809

import re
from .atom import Atom


class Molecule:
    """
    Classe qui représente une molécule (ex: la molécule H20)

    Attributs:
        formula (str): la formule de l'atome (ex: "H2O")
        atoms (dict[Atom, int]): dictionnaire des atomes dans la molecule (ex: {H:2, O:1})
        weight (float): masse de la molécule, c'est la somme des atomes la composant
    """

    def __init__(self, formula: str):

        self.formula = formula

        self.atoms = self.parse_formula()

        self.weight = 0.0

        for atom, count in self.atoms.items():
            self.weight += atom.weight * count

    def __repr__(self):
        return self.formula

    def __str__(self):
        return f"({self.formula}, {self.atoms}, {self.weight})"

    def __eq__(self, other_mol):
        return self.formula == other_mol.formula

    def parse_formula(self):
        """On sépare la chaine self.formula de sorte que
        chaque lettre suivie d'un nombre soient regroupés"""
        regex_result = re.findall(r"([A-Z][a-z]*)(\d*)", self.formula)
        res = {}
        for element, nombre in regex_result:
            # Si le nombre est vide, c'est 1, sinon on convertit le texte en entier
            at = Atom.from_str(element)

            qte = 1
            if nombre != "":
                qte = int(nombre)

            if at in res:
                res[at] += qte
            else:
                res[at] = qte

        return res
