# AC Flowers
Modeling Animal Crossing New Horizons flower breeding.
Data taken from https://docs.google.com/spreadsheets/d/11pRCX8G0xGizSYWgVhoUSu7pE-MV7AOprBcgSY1whB4/


# Example Usage
```
import ac_flowers

# What happens if you breed blue and orange hyacinths?
ac_flowers.utilities.simulate_breeding_from_phenotype('hyacinth', 'blue', 'orange', 100, 100)

# What genotypes can you produce from seed roses after 2 generations?
ac_flowers.utilities.combinations_from_seed('rose', generations=2)

# What are all of the possible ways to use red cosmos in production of black cosmos?
cosmo = ac_flowers.flower.Flower('cosmo')
cosmo.all_possible_parents('black', required_parent_color='red')

# Bayesian probability for genotypes if you observe a breeding pair and 0 or more of their offspring
ac_flowers.utilities.bayes('hyacinth', 'blue', 'blue', ['blue', 'blue', 'blue'])
```

There is also a flask app and UI which is under development

# Dev Roadmap
 - Bayes UI needs colors on the posteriors table
 - Bayes UI should also show "possible future offspring" and allow you to select a "target color" to work backwards from
 - build a module for simulating genetic diversity from starting seeds
