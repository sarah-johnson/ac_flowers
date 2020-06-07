import pandas as pd
import random

# Data taken from https://docs.google.com/spreadsheets/d/11pRCX8G0xGizSYWgVhoUSu7pE-MV7AOprBcgSY1whB4/
genotype_map = {
    "cosmo": {
        (0, 0, 0): "white",
        (0, 0, 1): "white",
        (0, 0, 2): "white",
        (0, 1, 0): "yellow",
        (0, 1, 1): "yellow",
        (0, 1, 2): "white",
        (0, 2, 0): "yellow",
        (0, 2, 1): "yellow",
        (0, 2, 2): "yellow",
        (1, 0, 0): "pink",
        (1, 0, 1): "pink",
        (1, 0, 2): "pink",
        (1, 1, 0): "orange",
        (1, 1, 1): "orange",
        (1, 1, 2): "pink",
        (1, 2, 0): "orange",
        (1, 2, 1): "orange",
        (1, 2, 2): "orange",
        (2, 0, 0): "red",
        (2, 0, 1): "red",
        (2, 0, 2): "red",
        (2, 1, 0): "orange",
        (2, 1, 1): "orange",
        (2, 1, 2): "red",
        (2, 2, 0): "black",
        (2, 2, 1): "black",
        (2, 2, 2): "red",
    },
    "hyacinth": {
        (0, 0, 0): "white",
        (0, 0, 1): "white",
        (0, 0, 2): "blue",
        (0, 1, 0): "yellow",
        (0, 1, 1): "yellow",
        (0, 1, 2): "white",
        (0, 2, 0): "yellow",
        (0, 2, 1): "yellow",
        (0, 2, 2): "yellow",
        (1, 0, 0): "red",
        (1, 0, 1): "pink",
        (1, 0, 2): "white",
        (1, 1, 0): "orange",
        (1, 1, 1): "yellow",
        (1, 1, 2): "yellow",
        (1, 2, 0): "orange",
        (1, 2, 1): "yellow",
        (1, 2, 2): "yellow",
        (2, 0, 0): "red",
        (2, 0, 1): "red",
        (2, 0, 2): "red",
        (2, 1, 0): "blue",
        (2, 1, 1): "red",
        (2, 1, 2): "red",
        (2, 2, 0): "purple",
        (2, 2, 1): "purple",
        (2, 2, 2): "purple",
    },
    "lily": {
        (0, 0, 0): "white",
        (0, 0, 1): "white",
        (0, 0, 2): "white",
        (0, 1, 0): "yellow",
        (0, 1, 1): "white",
        (0, 1, 2): "white",
        (0, 2, 0): "yellow",
        (0, 2, 1): "yellow",
        (0, 2, 2): "white",
        (1, 0, 0): "red",
        (1, 0, 1): "pink",
        (1, 0, 2): "white",
        (1, 1, 0): "orange",
        (1, 1, 1): "yellow",
        (1, 1, 2): "yellow",
        (1, 2, 0): "orange",
        (1, 2, 1): "yellow",
        (1, 2, 2): "yellow",
        (2, 0, 0): "black",
        (2, 0, 1): "red",
        (2, 0, 2): "pink",
        (2, 1, 0): "black",
        (2, 1, 1): "red",
        (2, 1, 2): "pink",
        (2, 2, 0): "orange",
        (2, 2, 1): "orange",
        (2, 2, 2): "white",
    },
    "mum": {
        (0, 0, 0): "white",
        (0, 0, 1): "white",
        (0, 0, 2): "purple",
        (0, 1, 0): "yellow",
        (0, 1, 1): "yellow",
        (0, 1, 2): "white",
        (0, 2, 0): "yellow",
        (0, 2, 1): "yellow",
        (0, 2, 2): "yellow",
        (1, 0, 0): "pink",
        (1, 0, 1): "pink",
        (1, 0, 2): "pink",
        (1, 1, 0): "yellow",
        (1, 1, 1): "red",
        (1, 1, 2): "pink",
        (1, 2, 0): "purple",
        (1, 2, 1): "purple",
        (1, 2, 2): "purple",
        (2, 0, 0): "red",
        (2, 0, 1): "red",
        (2, 0, 2): "red",
        (2, 1, 0): "purple",
        (2, 1, 1): "purple",
        (2, 1, 2): "red",
        (2, 2, 0): "green",
        (2, 2, 1): "green",
        (2, 2, 2): "red",
    },
    "pansy": {
        (0, 0, 0): "white",
        (0, 0, 1): "white",
        (0, 0, 2): "blue",
        (0, 1, 0): "yellow",
        (0, 1, 1): "yellow",
        (0, 1, 2): "blue",
        (0, 2, 0): "yellow",
        (0, 2, 1): "yellow",
        (0, 2, 2): "yellow",
        (1, 0, 0): "red",
        (1, 0, 1): "red",
        (1, 0, 2): "blue",
        (1, 1, 0): "orange",
        (1, 1, 1): "orange",
        (1, 1, 2): "orange",
        (1, 2, 0): "yellow",
        (1, 2, 1): "yellow",
        (1, 2, 2): "yellow",
        (2, 0, 0): "red",
        (2, 0, 1): "red",
        (2, 0, 2): "purple",
        (2, 1, 0): "red",
        (2, 1, 1): "red",
        (2, 1, 2): "purple",
        (2, 2, 0): "orange",
        (2, 2, 1): "orange",
        (2, 2, 2): "purple",
    },
    "rose": {
        (0, 0, 0, 0): "white",
        (0, 0, 0, 1): "white",
        (0, 0, 0, 2): "white",
        (0, 0, 1, 0): "white",
        (0, 0, 1, 1): "white",
        (0, 0, 1, 2): "white",
        (0, 0, 2, 0): "purple",
        (0, 0, 2, 1): "purple",
        (0, 0, 2, 2): "purple",
        (0, 1, 0, 0): "yellow",
        (0, 1, 0, 1): "yellow",
        (0, 1, 0, 2): "yellow",
        (0, 1, 1, 0): "white",
        (0, 1, 1, 1): "white",
        (0, 1, 1, 2): "white",
        (0, 1, 2, 0): "purple",
        (0, 1, 2, 1): "purple",
        (0, 1, 2, 2): "purple",
        (0, 2, 0, 0): "yellow",
        (0, 2, 0, 1): "yellow",
        (0, 2, 0, 2): "yellow",
        (0, 2, 1, 0): "yellow",
        (0, 2, 1, 1): "yellow",
        (0, 2, 1, 2): "yellow",
        (0, 2, 2, 0): "white",
        (0, 2, 2, 1): "white",
        (0, 2, 2, 2): "white",
        (1, 0, 0, 0): "red",
        (1, 0, 0, 1): "pink",
        (1, 0, 0, 2): "white",
        (1, 0, 1, 0): "red",
        (1, 0, 1, 1): "pink",
        (1, 0, 1, 2): "white",
        (1, 0, 2, 0): "red",
        (1, 0, 2, 1): "pink",
        (1, 0, 2, 2): "purple",
        (1, 1, 0, 0): "orange",
        (1, 1, 0, 1): "yellow",
        (1, 1, 0, 2): "yellow",
        (1, 1, 1, 0): "red",
        (1, 1, 1, 1): "pink",
        (1, 1, 1, 2): "white",
        (1, 1, 2, 0): "red",
        (1, 1, 2, 1): "pink",
        (1, 1, 2, 2): "purple",
        (1, 2, 0, 0): "orange",
        (1, 2, 0, 1): "yellow",
        (1, 2, 0, 2): "yellow",
        (1, 2, 1, 0): "orange",
        (1, 2, 1, 1): "yellow",
        (1, 2, 1, 2): "yellow",
        (1, 2, 2, 0): "red",
        (1, 2, 2, 1): "pink",
        (1, 2, 2, 2): "white",
        (2, 0, 0, 0): "black",
        (2, 0, 0, 1): "red",
        (2, 0, 0, 2): "pink",
        (2, 0, 1, 0): "black",
        (2, 0, 1, 1): "red",
        (2, 0, 1, 2): "pink",
        (2, 0, 2, 0): "black",
        (2, 0, 2, 1): "red",
        (2, 0, 2, 2): "pink",
        (2, 1, 0, 0): "orange",
        (2, 1, 0, 1): "orange",
        (2, 1, 0, 2): "yellow",
        (2, 1, 1, 0): "red",
        (2, 1, 1, 1): "red",
        (2, 1, 1, 2): "white",
        (2, 1, 2, 0): "black",
        (2, 1, 2, 1): "red",
        (2, 1, 2, 2): "purple",
        (2, 2, 0, 0): "orange",
        (2, 2, 0, 1): "orange",
        (2, 2, 0, 2): "yellow",
        (2, 2, 1, 0): "orange",
        (2, 2, 1, 1): "orange",
        (2, 2, 1, 2): "yellow",
        (2, 2, 2, 0): "blue",
        (2, 2, 2, 1): "red",
        (2, 2, 2, 2): "white",
    },
    "tulip": {
        (0, 0, 0): "white",
        (0, 0, 1): "white",
        (0, 0, 2): "white",
        (0, 1, 0): "yellow",
        (0, 1, 1): "yellow",
        (0, 1, 2): "white",
        (0, 2, 0): "yellow",
        (0, 2, 1): "yellow",
        (0, 2, 2): "yellow",
        (1, 0, 0): "red",
        (1, 0, 1): "pink",
        (1, 0, 2): "white",
        (1, 1, 0): "orange",
        (1, 1, 1): "yellow",
        (1, 1, 2): "yellow",
        (1, 2, 0): "orange",
        (1, 2, 1): "yellow",
        (1, 2, 2): "yellow",
        (2, 0, 0): "black",
        (2, 0, 1): "red",
        (2, 0, 2): "red",
        (2, 1, 0): "black",
        (2, 1, 1): "red",
        (2, 1, 2): "red",
        (2, 2, 0): "purple",
        (2, 2, 1): "purple",
        (2, 2, 2): "purple",
    },
    "windflower": {
        (0, 0, 0): "white",
        (0, 0, 1): "white",
        (0, 0, 2): "blue",
        (0, 1, 0): "orange",
        (0, 1, 1): "orange",
        (0, 1, 2): "blue",
        (0, 2, 0): "orange",
        (0, 2, 1): "orange",
        (0, 2, 2): "orange",
        (1, 0, 0): "red",
        (1, 0, 1): "red",
        (1, 0, 2): "blue",
        (1, 1, 0): "pink",
        (1, 1, 1): "pink",
        (1, 1, 2): "pink",
        (1, 2, 0): "orange",
        (1, 2, 1): "orange",
        (1, 2, 2): "orange",
        (2, 0, 0): "red",
        (2, 0, 1): "red",
        (2, 0, 2): "purple",
        (2, 1, 0): "red",
        (2, 1, 1): "red",
        (2, 1, 2): "purple",
        (2, 2, 0): "pink",
        (2, 2, 1): "pink",
        (2, 2, 2): "purple",
    },
}

seed_genotypes = {
    "cosmo": {"red": (2, 0, 0), "white": (0, 0, 1), "yellow": (0, 2, 1),},
    "hyacinth": {"red": (2, 0, 1), "white": (0, 0, 1), "yellow": (0, 2, 0),},
    "lily": {"red": (2, 0, 1), "white": (0, 0, 2), "yellow": (0, 2, 0),},
    "mum": {"red": (2, 0, 0), "white": (0, 0, 1), "yellow": (0, 2, 0),},
    "pansy": {"red": (2, 0, 0), "white": (0, 0, 1), "yellow": (0, 2, 0),},
    "rose": {"red": (2, 0, 0, 1), "white": (0, 0, 1, 0), "yellow": (0, 2, 0, 0),},
    "tulip": {"red": (2, 0, 1), "white": (0, 0, 1), "yellow": (0, 2, 0),},
    "windflower": {"red": (2, 0, 0), "orange": (0, 2, 0), "white": (0, 0, 1),},
}


class Flower:
    @staticmethod
    def get_binary_gene(x):
        genes = {0: (0, 0), 1: (1, 0), 2: (1, 1)}
        return genes[x]

    def select_allele(self, parent_1, parent_2):
        return random.choice(self.get_binary_gene(parent_1)) + random.choice(
            self.get_binary_gene(parent_2)
        )


class FlowerInstance(Flower):
    """
    Instance of an Animal Crossing flower
    Must subclass and implement a flower_type
    """

    def __str__(self):
        return "{} ({})".format(self.genotype, self.phenotype)

    def __repr__(self):
        return "{} ({})".format(self.genotype, self.phenotype)

    @classmethod
    def create(cls, genes):
        flower_type_mapping = {
            # 'cosmo': CosmoInstance,
            "hyacinth": HyacinthInstance,
            # 'lily': LilyInstance,
            # 'mum': MumInstance,
            # 'pansy': PansyInstance,
            # 'rose': RoseInstance,
            # 'tulip': TulipInstance,
            # 'windflower': WindflowerInstance,
        }
        return flower_type_mapping[cls.flower_type](*genes)

    def breed(self, other):
        """
        Must only breed two FlowerInstances of the same Flower Type
        """
        return self.create(
            *[
                self.select_allele(p1, p2)
                for p1, p2 in zip(self.genotype, other.genotype)
            ]
        )

    @property
    def phenotype(self):
        return self.genotype_phenotype_map[self.genotype]

    def all_children_with_weights(self, other):
        child_genes_and_weights = []
        for p1_allele, p2_allele in zip(self.genotype, other.genotype):
            allele_values = {}
            for g1 in self.get_binary_gene(p1_allele):
                for g2 in self.get_binary_gene(p2_allele):
                    child_allele = g1 + g2
                    try:
                        allele_values[child_allele] += 0.25
                    except KeyError:
                        allele_values[child_allele] = 0.25
            child_genes_and_weights.append(allele_values)

        # TODO This won't work for the Rose
        r_weights, y_weights, w_weights = child_genes_and_weights
        all_children = {}
        for r_gene, p_r_gene in r_weights.items():
            for y_gene, p_y_gene in y_weights.items():
                for w_gene, p_w_gene in w_weights.items():
                    p_gene = p_r_gene * p_y_gene * p_w_gene
                    try:
                        all_children[(r_gene, y_gene, w_gene)] += p_gene
                    except KeyError:
                        all_children[(r_gene, y_gene, w_gene)] = p_gene
        all_children = {self.create(k): v for k, v in all_children.items()}
        return all_children


class HyacinthMixin:
    def all_possible_genotypes(cls, phenotype):
        return [
            HyacinthInstance.create(k)
            for k, v in self.genotype_phenotype_map.items()
            if v == phenotype
        ]


class HyacinthInstance(FlowerInstance, HyacinthMixin):
    def __init__(self, r_gene, y_gene, w_gene):
        """
        :param genotype: tuple of trinary values representing the
        genes of the hyacinth.
        """
        self.genotype = (r_gene, y_gene, w_gene)


def simulate_hyacinth_breeding():
    f1 = HyacinthInstance(*HyacinthMixin.seed_white)
    f2 = HyacinthInstance(*HyacinthMixin.seed_white)
    n = 100
    print("Simulating 100 breedings between seed white and seed white Hyacinths")
    results = [f1.breed(f2) for _ in range(n)]
    results_df = pd.DataFrame([(c.phenotype, c.genotype) for c in results])
    results_df.columns = ["phenotype", "genotype"]
    grouped = results_df.groupby("phenotype")["genotype"].value_counts()
    print(grouped)


def hyacinth_genotypes_for_phenotype(color):
    hyacinth = HyacinthMixin(color)
    possible = hyacinth.all_possible_genotypes()
    print(
        "A random {} hyacinth could have the following possible genotypes:".format(
            color
        )
    )
    print([p.genotype for p in possible])


def simulate_hyacinth_matings_from_phenotype(color1, color2):
    print(
        "Simulating the mating of 100 random pairs of {} and {} hyacinths, 100 times each.".format(
            color1, color2
        )
    )
    possible_color1 = HyacinthColor(color1).all_possible_genotypes()
    possible_color2 = HyacinthColor(color2).all_possible_genotypes()
    mating_results = {}
    for _ in range(100):
        parent_1 = random.choice(possible_color1)
        parent_2 = random.choice(possible_color2)
        key = tuple(sorted((parent_1.genotype, parent_2.genotype)))
        mating_results.setdefault(key, [])
        for _ in range(100):
            mating_results[key].append(parent_1.breed(parent_2))

    print("______")
    for k, v in mating_results.items():
        print("results for mating pair {}".format(k))
        results_df = pd.DataFrame([(c.phenotype, c.genotype) for c in v])
        results_df.columns = ["phenotype", "genotype"]
        grouped = results_df.groupby("phenotype")["genotype"].value_counts()
        print(grouped)
        print("______")


def find_all_hyacinth_phenotype_combinations(color1, color2):
    possible_color1 = HyacinthColor(color1).all_possible_genotypes()
    possible_color2 = HyacinthColor(color2).all_possible_genotypes()
    for parent_1 in possible_color1:
        for parent_2 in possible_color2:
            results = parent_1.all_children_with_weights(parent_2)
            print("Results of breeding parents {} and {}".format(parent_1, parent_2))
            for k, v in results.items():
                print(
                    "{:12}{:7}{:6.2f}%".format(repr(k.genotype), k.phenotype, v * 100)
                )


if __name__ == "__main__":
    # simulate_matings_from_genotype()
    # simulate_matings_from_phenotype('pink', 'pink')
    # seed_red = HyacinthInstance(*Hyacinth.seed_red)
    # seed_yellow = HyacinthInstance(*Hyacinth.seed_yellow)
    # results = seed_red.all_children_with_weights(seed_yellow)
    # print(results)
    find_all_hyacinth_phenotype_combinations("purple", "purple")
