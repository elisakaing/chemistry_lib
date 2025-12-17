# Elisa KAING 21128809

import numpy as np
import matplotlib.pyplot as plt

from .mol import Molecule


def valid_reaction(
    reactives: list[tuple[Molecule, int]], products: list[tuple[Molecule, int]]
):
    """
    Renvoie un bool indiquant si la réaction est possible (i.e autant d’atomes de même type
    dans les réactifs que dans les produits)

    Args:
        reactives: correspond aux réactifs de la réaction avec leur nombres associés
        products: correspond aux produits de la réaction avec leur nombres associés
    """
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
    """
    Renvoie une list[float], ou un np.array[float], de length steps,
    contenant [A](t) aux différents temps.
    Si figure_path n’est pas None, une image sera sauvegardée sous ce nom.
    Args:
        a0: concentration initiale de la molécule
        k: la constante de la réaction
        T: le temps total de la réaction que l’on veut modéliser (en secondes)
        steps: le nb de temps où l’on mesure la concentration
        figure_path: si cet argument n’est pas None (i.e est un str),alors la fonction plotera
                      l’évolution de la concentration en fonction du temps et sauvegardera la figure
                      sous ce nom figure path
    """
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
