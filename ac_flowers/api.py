import logging

from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound

from .flower import all_flowers_genotype_map, seed_genotypes
from .utilities import bayes

logger = logging.getLogger(__name__)

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
    flower_info = [
        {
            'genotype': str(genotype),
            'color': phenotype,
            'seed': 'seed' if genotype in seed_genotypes[flower].values() else ''
        }
        for genotype, phenotype in all_flowers_genotype_map[flower].items()
    ]

    return {
        "flower_info": flower_info,
        "colors": list(set(all_flowers_genotype_map[flower].values()))
    }


@api.route("/api/bayes", methods=["POST"])
def api_bayes():
    posteriors = bayes(
        flower_type=request.json['flower_type'],
        color1=request.json['parent1'],
        color2=request.json['parent2'],
        observed_children_colors=request.json['children'],
    )
    return {
        'posteriors': posteriors
    }
