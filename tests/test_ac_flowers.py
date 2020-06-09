import itertools
import unittest

from ac_flowers.flower import Flower, FlowerInstance, all_flowers_genotype_map, seed_genotypes


class TestFlowers(unittest.TestCase):
    def setUp(self):
        self.flower_types_and_colors = {
            "cosmo": ["red", "yellow", "white", "orange", "pink", "black"],
            "hyacinth": ["red", "yellow", "white", "orange", "pink", "blue", "purple"],
            "lily": ["red", "yellow", "white", "pink", "black", "orange"],
            "mum": ["red", "yellow", "white", "pink", "purple", "green"],
            "pansy": ["red", "yellow", "white", "orange", "blue", "purple"],
            "rose": [
                "red",
                "yellow",
                "white",
                "blue",
                "black",
                "purple",
                "orange",
                "pink",
            ],
            "tulip": ["red", "yellow", "white", "orange", "pink", "black", "purple"],
            "windflower": ["red", "orange", "white", "pink", "blue", "purple"],
        }

    def test_all_flowers_defined(self):
        self.assertListEqual(
            list(all_flowers_genotype_map), list(self.flower_types_and_colors),
        )

    def test_each_flower_defines_all_genotypes(self):
        for flower, genotype_map in all_flowers_genotype_map.items():
            n = 4 if flower == "rose" else 3
            possible_genotypes = {i for i in itertools.product(range(3), repeat=n)}
            self.assertSetEqual(
                set(genotype_map),
                possible_genotypes,
                "Incorrect genotypes for {}".format(flower),
            )
            possible_colors = set(self.flower_types_and_colors[flower])
            self.assertSetEqual(
                possible_colors,
                set(genotype_map.values()),
                "Incorrect colors for {}".format(flower),
            )

    def test_seed_genotypes(self):
        for flower, seed_data in self.flower_types_and_colors.items():
            seed_data = seed_genotypes[flower]
            seed_colors = {"red", "white"}

            if flower == "windflower":
                seed_colors.add("orange")
            else:
                seed_colors.add("yellow")

            if flower == "rose":
                n_alleles = 4
            else:
                n_alleles = 3

            self.assertSetEqual(
                seed_colors, set(seed_data),
            )
            for seed_genotype in seed_data.values():
                self.assertEqual(
                    len(seed_genotype),
                    n_alleles,
                    "Incorrect seed genotype for {}".format(flower),
                )
                self.assertTrue(set(seed_genotype).issubset({0, 1, 2}))

    def test_child_color_probability(self):
        rose = Flower("rose")
        result = rose.child_color_probability(
            rose.seed_genotypes["red"], rose.seed_genotypes["white"], "pink"
        )
        self.assertEqual(result, 0.50)

        windflower = Flower("windflower")
        result = windflower.child_color_probability(
            windflower.seed_genotypes["red"],
            windflower.seed_genotypes["orange"],
            "pink",
        )
        self.assertEqual(result, 1.0)

        tulip = Flower("tulip")
        result = tulip.child_color_probability(
            tulip.seed_genotypes["yellow"], tulip.seed_genotypes["white"], "black"
        )
        self.assertEqual(result, 0.0)
