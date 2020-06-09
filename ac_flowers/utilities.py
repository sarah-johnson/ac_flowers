import click

from ac_flowers.flower import Flower, FlowerInstance


def simulate_breeding(flower_type, genotype_1, genotype_2, n):
    f1 = FlowerInstance(flower_type, genotype_1)
    f2 = FlowerInstance(flower_type, genotype_2)
    click.echo(
        "Simulating {} breedings between {} {} and {}".format(
            n, flower_type, genotype_1, genotype_2
        )
    )
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
            click.echo(
                "Results of breeding parents {} and {}".format(parent_1, parent_2)
            )
            for k, v in results.items():
                click.echo(
                    "{:12}{:7}{:6.2f}%".format(repr(k.genotype), k.phenotype, v * 100)
                )


def simulate_breeding_from_phenotype(flower_type, color1, color2, n_pairs, n_breedings):
    click.echo(
        "Simulating the breeding of {} random pairs of {} and {} {}, {} times each.".format(
            n_pairs, color1, color2, flower_type, n_breedings
        )
    )
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
        p1, p2 = [flower.create(genotype) for genotype in k]
        click.echo("results for breeding pair {} and {}".format(p1, p2))
        results_df = pd.DataFrame([(c.phenotype, c.genotype) for c in v])
        results_df.columns = ["phenotype", "genotype"]
        grouped = results_df.groupby("phenotype")["genotype"].value_counts()
        click.echo(grouped)
        click.echo("______")


def combinations_from_seed(flower_type, generations=1):
    click.echo("Running report on starting from seeds with {}".format(flower_type))
    flower = Flower(flower_type)
    starting_flowers = [
        flower.create(genes) for genes in flower.seed_genotypes.values()
    ]

    available_flowers = starting_flowers
    for generation in range(generations):
        click.echo("Calculating offspring for generation {}".format(generation))
        current_generation_flowers = []
        for parent_1, parent_2 in itertools.combinations_with_replacement(
            available_flowers, 2
        ):
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
    p_parent_pair = 1.0 / (len(possible_parent1) * len(possible_parent2))
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
            p_child = flower.child_color_probability(
                p1_genotype, p2_genotype, child_color
            )
            event_probabilities[key] = p_child
            posteriors[key] *= p_child

        posteriors = {k: v / sum(posteriors.values()) for k, v in posteriors.items()}

    click.echo(
        "Given {} with parent phenotypes {} {} and known offspring {}, the following genotypes "
        "and probabilities are assigned:".format(
            flower_type, color1, color2, observed_children_colors
        )
    )
    for k, v in posteriors.items():
        if v == 0:
            continue
        click.echo("{}: {:.2f}%".format(k, v * 100))
