ATOMS = [
    (("O", 8, 16), ("1s2", "2s2", "2p4")),
    (("C", 6, 12), ("1s2", "2s2", "2p2")),
    (("H", 1, 1), ("1s1",)),
    (("P", 15, 31), ("1s2", "2s2", "2p6", "3s2", "3p3")),
    (("K", 19, 39), ("1s2", "2s2", "2p6", "3s2", "3p6", "4s1")),
    (("Na", 11, 23), ("1s2", "2s2", "2p6", "3s1")),
    (
        (
            "Cl",
            17,
            35.5,
        ),
        ("1s2", "2s2", "2p6", "3s2", "3p5"),
    ),
    (
        (
            "Mg",
            12,
            24.3,
        ),
        ("1s2", "2s2", "2p6", "3s2"),
    ),
    (
        (
            "Fe",
            26,
            55.8,
        ),
        ("1s2", "2s2", "2p6", "3s2", "3p6", "4s2", "3d6"),
    ),
    (
        (
            "Zn",
            30,
            65,
        ),
        ("1s2", "2s2", "2p6", "3s2", "3p6", "4s2", "3d10"),
    ),
    (
        (
            "Au",
            79,
            197.0,
        ),
        (
            "1s2",
            "2s2",
            "2p6",
            "3s2",
            "3p6",
            "4s2",
            "3d10",
            "4p6",
            "5s2",
            "4d10",
            "5p6",
            "6s2",
            "4f14",
            "5d9",
        ),
    ),
    (
        (
            "Fl",
            114,
            289.0,
        ),
        (
            "1s2",
            "2s2",
            "2p6",
            "3s2",
            "3p6",
            "4s2",
            "3d10",
            "4p6",
            "5s2",
            "4d10",
            "5p6",
            "6s2",
            "4f14",
            "5d10",
            "6p6",
            "7s2",
            "5f14",
            "6d10",
            "7p2",
        ),
    ),
    (
        (
            "Er",
            68,
            167.3,
        ),
        (
            "1s2",
            "2s2",
            "2p6",
            "3s2",
            "3p6",
            "4s2",
            "3d10",
            "4p6",
            "5s2",
            "4d10",
            "5p6",
            "6s2",
            "4f12",
        ),
    ),
    (
        (
            "Er",
            87,
            223.0,
        ),
        (
            "1s2",
            "2s2",
            "2p6",
            "3s2",
            "3p6",
            "4s2",
            "3d10",
            "4p6",
            "5s2",
            "4d10",
            "5p6",
            "6s2",
            "4f14",
            "5d10",
            "6p6",
            "7s1",
        ),
    ),
    (("N", 7, 14.0), ("1s2", "2s2", "2p3")),
    (("F", 9, 19.0), ("1s2", "2s2", "2p5")),
    (("S", 16, 32.1), ("1s2", "2s2", "2p6", "3s2", "3p4")),
    (("Ca", 20, 40.1), ("1s2", "2s2", "2p6", "3s2", "3p6", "4s2")),
    (("Co", 27, 58.9), ("1s2", "2s2", "2p6", "3s2", "3p6", "4s2", "3d7")),
    (
        ("Mo", 42, 95.9),
        ("1s2", "2s2", "2p6", "3s2", "3p6", "4s2", "3d10", "4p6", "5s2", "4d4"),
    ),
    (
        ("I", 53, 126.9),
        ("1s2", "2s2", "2p6", "3s2", "3p6", "4s2", "3d10", "4p6", "5s2", "4d10", "5p5"),
    ),
]

SORTED_ORB = [
    (1, 0),
    (2, 0),
    (2, 1),
    (3, 0),
    (3, 1),
    (4, 0),
    (3, 2),
    (4, 1),
    (5, 0),
    (4, 2),
    (5, 1),
    (6, 0),
    (4, 3),
    (5, 2),
    (6, 1),
    (7, 0),
    (5, 3),
    (6, 2),
    (7, 1),
]

str_atoms_list = [
    "C",
    "H",
    "O",
    "N",
    "Ca",
    "P",
    "K",
    "S",
    "Na",
    "Cl",
    "Fe",
    "I",
    "F",
    "Co",
    "Mo",
]


class Atom:
    def __init__(self, name: str, num_electron: int, weight: float):
        self.name = name
        self.num_electron = num_electron
        self.weight = weight

        for description, elec_config in ATOMS:
            name, num_electron, weight = description

            if (
                name == self.name
                and num_electron == self.num_electron
                and weight == self.weight
            ):
                self.elec_config = elec_config
                break

    def __repr__(self):
        return self.name

    def __str__(self):
        return f"({self.name}, {self.num_electron}, {self.weight})"

    def __eq__(self, other_atom):
        print(other_atom)
        return (self.name, self.num_electron, self.weight) == (
            other_atom.name,
            other_atom.num_electron,
            other_atom.weight,
        )

    def __hash__(self):
        return hash((self.name, self.num_electron, self.weight))

    def from_str(str_atom):
        """Convert str to Atom object"""
        index = str_atoms_list.index(str_atom)
        return atoms_list[index]


C = Atom(name="C", num_electron=6, weight=12)
O = Atom("O", 8, 16)
H = Atom("H", 1, 1)
N = Atom("N", 7, 14.0)  # nitrogen
Ca = Atom("Ca", 20, 40.1)  # calcium
P = Atom("P", 15, 31)
K = Atom("K", 19, 39)
S = Atom("S", 16, 32.1)  # sulfur
Na = Atom("Na", 11, 23)
Cl = Atom("Cl", 17, 35.5)
Fe = Atom("Fe", 26, 55.8)
I = Atom("I", 53, 126.9)  # iodine
F = Atom("F", 9, 19.0)  # fluorine
Co = Atom("Co", 27, 58.9)  # cobalt
Mo = Atom("Mo", 42, 95.9)  # molybdenum


atoms_list = [C, H, O, N, Ca, P, K, S, Na, Cl, Fe, I, F, Co, Mo]


def num_elec(l):
    """l est à valeurs dans 0,1,2 et 3
    Renvoie le nombre d'atomes sur une orbitale"""
    return (l * 2 + 1) * 2


def get_orbitales(z: int):
    # Z est le nombre d’électrons de notre atome
    sorted_orbitales = SORTED_ORB
    # On commence avec Z électrons à disposer , que l’on va soustraire au fil des orbitales
    atoms_free = z
    orbitales_atom = []
    i = 0
    while atoms_free > 0:
        # On sélectionne la bonne orbitale
        good_orbitale = sorted_orbitales[i]
        n, l = good_orbitale
        # Determiner le nombre d’atomes sur cette orbitale
        atoms_orb = num_elec(l)
        # Nombre d'atomes dans la couche actuelle
        num_atom = min(atoms_orb, atoms_free)

        atoms_free -= atoms_orb

        orbitales_atom.append((n, l, num_atom))
        i += 1
    return orbitales_atom
