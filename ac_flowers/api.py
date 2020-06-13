from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

from .flower import all_flowers_genotype_map, seed_genotypes

api = Blueprint('api', __name__, template_folder='templates')

@api.route('/api/list-flowers')
def list_flowers():
    """
    List all possible flowers
    """
    return {"flowers" : list(all_flowers_genotype_map)}

@api.route('/api/<flower>')
def get_flower_info(flower):
    """
    Return all the "baseline" information regarding a given flower
    """
    flower_info = []
    seed_flowers = seed_genotypes[flower].values()

    for genotype, phenotype in all_flowers_genotype_map[flower].items():
        if genotype in seed_flowers:
            seed = "seed"
        else:
            seed = ""
        flower_info.append((str(genotype), phenotype, seed))

    return {
        "flower_info": flower_info,
        "colors": list(set(all_flowers_genotype_map[flower].values()))
    }
