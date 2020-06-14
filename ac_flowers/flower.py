"""
Modeling Animal Crossing Flowers for Bayesian Stats on determining genotype
Data taken from https://docs.google.com/spreadsheets/d/11pRCX8G0xGizSYWgVhoUSu7pE-MV7AOprBcgSY1whB4/
"""

import itertools
import random

all_flowers_genotype_map = {
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

    def all_possible_genotypes(self, phenotype):
        return [
            self.create(genotype)
            for genotype, color in self.genotype_map.items()
            if color == phenotype
        ]

    def create(self, genotype):
        return FlowerInstance(self.flower_type, genotype)

    def all_possible_parents(self, target_color, required_parent_color=None):
        """
        Returns a dict where keys are tuples of parent FlowerInstances
        and values are the probability of that pair breeding the target color
        """
        all_possible_flowers = [
            self.create(k) for k, v in self.genotype_map.items() if v != target_color
        ]
        all_possible_parents = {}
        for parent1, parent2 in itertools.combinations_with_replacement(
            all_possible_flowers, 2
        ):
            p_child = self.child_color_probability(
                parent1.genotype, parent2.genotype, target_color
            )
            if p_child:
                if required_parent_color and required_parent_color in (
                    parent1.phenotype,
                    parent2.phenotype,
                ):
                    all_possible_parents[(parent1, parent2)] = p_child
                elif not required_parent_color:
                    all_possible_parents[(parent1, parent2)] = p_child
        return all_possible_parents

    def possible_parent_genotypes(self, parent1_color, parent2_color, target_color):
        """
        Returns a dict of parent genotypes that can produce the target color with the probability
        """
        possible_parent1 = self.all_possible_genotypes(parent1_color)
        possible_parent2 = self.all_possible_genotypes(parent2_color)
        possible_parents = {}
        for parent1 in possible_parent1:
            for parent2 in possible_parent2:
                p_child = self.child_color_probability(
                    parent1.genotype, parent2.genotype, target_color
                )
                if p_child:
                    possible_parents[(parent1, parent2)] = p_child
        return possible_parents

    def child_color_probability(self, parent1_genotype, parent2_genotype, child_color):
        """
        Returns the probability of a certain offspring color from two parents
        of known genotype
        """
        parent1 = self.create(parent1_genotype)
        parent2 = self.create(parent2_genotype)
        children_with_weights = parent1.all_children_with_weights(parent2)
        child_colors = {}
        for child_flower, p in children_with_weights.items():
            try:
                child_colors[child_flower.phenotype] += p
            except KeyError:
                child_colors[child_flower.phenotype] = p
        return child_colors.get(child_color, 0)

    def __init__(self, flower_type):
        self.flower_type = flower_type
        self.genotype_map = all_flowers_genotype_map[flower_type]
        self.seed_genotypes = seed_genotypes[flower_type]


class FlowerInstance(Flower):
    """
    Instance of an Animal Crossing flower
    """

    def __init__(self, flower_type, genotype):
        super().__init__(flower_type)
        self.genotype = genotype

    @property
    def phenotype(self):
        return self.genotype_map[self.genotype]

    def __str__(self):
        return "{} ({})".format(self.phenotype, self.genotype)

    def __repr__(self):
        return "{} ({})".format(self.phenotype, self.genotype)

    def breed(self, other):
        assert (
            self.flower_type == other.flower_type
        ), "Two flowers of different types cannot breed"
        child_genes = tuple(
            [
                self.select_allele(parent_1, parent_2)
                for parent_1, parent_2 in zip(self.genotype, other.genotype)
            ]
        )
        return FlowerInstance(flower_type=self.flower_type, genotype=child_genes)

    def all_children_with_weights(self, other):
        assert (
            self.flower_type == other.flower_type
        ), "Two flowers of different types cannot breed"
        child_genes_and_weights = []
        for p1_allele, p2_allele in zip(self.genotype, other.genotype):
            allele_values = {}
            # Calculate a punnet square for each pair of alleles in the genotype
            for g1 in self.get_binary_gene(p1_allele):
                for g2 in self.get_binary_gene(p2_allele):
                    child_allele = g1 + g2
                    try:
                        allele_values[child_allele] += 0.25
                    except KeyError:
                        allele_values[child_allele] = 0.25
            child_genes_and_weights.append(allele_values)

        all_children = {}
        for child_genotype in itertools.product(
            *[gene.keys() for gene in child_genes_and_weights]
        ):
            child_flower = self.create(child_genotype)
            p_gene = 1.0
            for i in range(len(child_genotype)):
                p_allele = child_genes_and_weights[i][child_genotype[i]]
                p_gene *= p_allele
            all_children[child_flower] = p_gene

        return all_children
