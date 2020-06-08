"""
Modeling Animal Crossing Flowers for Bayesian Stats on determining genotype
Data taken from https://docs.google.com/spreadsheets/d/11pRCX8G0xGizSYWgVhoUSu7pE-MV7AOprBcgSY1whB4/
"""

import click
import itertools
import pandas as pd
import random

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

    def all_possible_genotypes(self, phenotype):
        return [
            FlowerInstance(self.flower_type, genes)
            for genes, color in self.genotype_map.items()
            if color == phenotype
        ]

    def create(self, genotype):
        return FlowerInstance(self.flower_type, genotype)

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
        self.genotype_map = genotype_map[flower_type]
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
        assert self.flower_type == other.flower_type, "Two flowers of different types cannot breed"
        child_genes = tuple([
            self.select_allele(parent_1, parent_2)
            for parent_1, parent_2 in zip(self.genotype, other.genotype)
            ])
        return FlowerInstance(flower_type=self.flower_type, genotype=child_genes)


    def all_children_with_weights(self, other):
        assert self.flower_type == other.flower_type, "Two flowers of different types cannot breed"
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
        for child_genotype in itertools.product(*[gene.keys() for gene in child_genes_and_weights]):
            child_flower = self.create(child_genotype)
            p_gene = 1.0
            for i in range(len(child_genotype)):
                p_allele = child_genes_and_weights[i][child_genotype[i]]
                p_gene *= p_allele
            all_children[child_flower] = p_gene

        return all_children


def simulate_breeding(flower_type, genotype_1, genotype_2, n):
    f1 = FlowerInstance(flower_type, genotype_1)
    f2 = FlowerInstance(flower_type, genotype_2)
    click.echo("Simulating {} breedings between {} {} and {}".format(
        n, flower_type, genotype_1, genotype_2))
    results = [f1.breed(f2) for _ in range(n)]
    results_df = pd.DataFrame([(c.phenotype, c.genotype) for c in results])
    results_df.columns = ["phenotype", "genotype"]
    grouped = results_df.groupby("phenotype")["genotype"].value_counts()
    click.echo(grouped)


def find_all_phenotype_combinations(flower_type, color1, color2):
    flower = Flower(flower_type)
    possible_color1 = flower.all_possible_genotypes(color1)
    possible_color2 = flower.all_possible_genotypes(color2)
    for parent_1 in possible_color1:
        for parent_2 in possible_color2:
            results = parent_1.all_children_with_weights(parent_2)
            click.echo("Results of breeding parents {} and {}".format(parent_1, parent_2))
            for k, v in results.items():
                click.echo(
                    "{:12}{:7}{:6.2f}%".format(repr(k.genotype), k.phenotype, v * 100)
                )


def simulate_breeding_from_phenotype(flower_type, color1, color2, n_pairs, n_breedings):
    click.echo(
        "Simulating the breeding of {} random pairs of {} and {} {}, {} times each.".format(
            n_pairs, color1, color2, flower_type, n_breedings
    ))
    flower = Flower(flower_type)
    possible_color1 = flower.all_possible_genotypes(color1)
    possible_color2 = flower.all_possible_genotypes(color2)
    results = {}
    for _ in range(n_pairs):
        parent_1 = random.choice(possible_color1)
        parent_2 = random.choice(possible_color2)
        key = tuple(sorted((parent_1.genotype, parent_2.genotype)))
        results.setdefault(key, [])
        for _ in range(100):
            results[key].append(parent_1.breed(parent_2))

    click.echo("______")
    for k, v in results.items():
        click.echo("results for breeding pair {}".format(k))
        results_df = pd.DataFrame([(c.phenotype, c.genotype) for c in v])
        results_df.columns = ["phenotype", "genotype"]
        grouped = results_df.groupby("phenotype")["genotype"].value_counts()
        click.echo(grouped)
        click.echo("______")


def combinations_from_seed(flower_type, generations=1):
    click.echo("Running report on starting from seeds with {}".format(flower_type))
    flower = Flower(flower_type)
    starting_flowers = [flower.create(genes) for genes in flower.seed_genotypes.values()]

    available_flowers = starting_flowers
    for generation in range(generations):
        click.echo("Calculating offspring for generation {}".format(generation))
        current_generation_flowers = []
        for parent_1, parent_2 in itertools.combinations_with_replacement(available_flowers, 2):
            click.echo("Possible children of {} and {}:".format(parent_1, parent_2))
            offspring = parent_1.all_children_with_weights(parent_2)
            for k, v in offspring.items():
                click.echo(
                    "{:12}{:7}{:6.2f}%".format(repr(k.genotype), k.phenotype, v * 100)
                )
            current_generation_flowers.extend(offspring.keys())
        available_flowers.extend(current_generation_flowers)


def genotypes_for_phenotype(flower_type, color):
    flower = Flower(flower_type)
    possible = flower.all_possible_genotypes(color)
    click.echo(
        "A random {} {} could have the following possible genotypes:".format(
            color, flower_type
        )
    )
    for p in possible:
        click.echo(p)


def bayes(flower_type, color1, color2, observed_children_colors=[]):
    flower = Flower(flower_type)
    possible_parent1 = flower.all_possible_genotypes(color1)
    possible_parent2 = flower.all_possible_genotypes(color2)

    priors = {}
    p_parent_pair = 1.0/(len(possible_parent1) * len(possible_parent2))
    for p1 in possible_parent1:
        for p2 in possible_parent2:
            key = tuple(sorted((p1.genotype, p2.genotype)))
            try:
                priors[key] += p_parent_pair
            except KeyError:
                priors[key] = p_parent_pair

    posteriors = priors
    for child_color in observed_children_colors:
        event_probabilities = {}

        for key, p_prior in priors.items():
            p1_genotype, p2_genotype = key
            p_child = flower.child_color_probability(p1_genotype, p2_genotype, child_color)
            event_probabilities[key] = p_child
            posteriors[key] *= p_child

        posteriors = {k: v/sum(posteriors.values()) for k, v in posteriors.items()}

    click.echo("Given {} with parent phenotypes {} {} and known offspring {}, the following genotypes "
        "and probabilities are assigned:".format(flower_type, color1, color2, observed_children_colors))
    for k, v in posteriors.items():
        if v == 0:
            continue
        click.echo("{}: {:.2f}%".format(k, v*100))
