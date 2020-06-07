import ac_flowers
import itertools
import unittest


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
            list(ac_flowers.genotype_map), list(self.flower_types_and_colors),
        )

    def test_each_flower_defines_all_genotypes(self):
        for flower, genotype_map in ac_flowers.genotype_map.items():
            n = 4 if flower == "rose" else 3
            possible_genotypes = [i for i in itertools.product(range(3), repeat=n)]
            self.assertListEqual(
                list(genotype_map),
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
            seed_data = ac_flowers.seed_genotypes[flower]
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
