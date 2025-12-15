import numpy as np
import matplotlib.pyplot as plt

from .mol import Molecule


def valid_reaction(
    reactives: list[tuple[Molecule, int]], products: list[tuple[Molecule, int]]
):

    reac = ""
    prod = ""

    for react in reactives:
        mol, coef = react
        for _ in range(coef):
            reac += mol.formula

    for produc in products:
        mol, coef = produc
        for _ in range(coef):
            prod += mol.formula

    dict_mol1 = Molecule(reac).parse_formula()
    dict_mol2 = Molecule(prod).parse_formula()
    return dict_mol1 == dict_mol2


def kinetic_decomp(
    a0: float, k: float, t: float, steps: int = 10, figure_path: str = None
):
    temps = np.linspace(0, t, steps)
    concentration = [a0 * np.exp(-k * t) for t in temps]
    if figure_path is not None:
        x = temps
        y = concentration
        plt.plot(x, y, "b")
        plt.title("Evolution de [A](t)")
        plt.xlabel("temps (en secondes)")
        plt.ylabel("[A](t) en mol.L-1")
        plt.savefig(figure_path)
    return concentration
