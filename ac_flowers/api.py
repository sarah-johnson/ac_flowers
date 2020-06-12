from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

from .flower import all_flowers_genotype_map, seed_genotypes

api = Blueprint('api', __name__, template_folder='templates')

@api.route('/api/list-flowers')
def list_flowers():
    return {"flowers" : list(all_flowers_genotype_map)}

@api.route('/api/<flower>')
def get_flower_info(flower):
    return {"flower_info": {str(k): v for k, v in all_flowers_genotype_map[flower].items()}}

@api.route('/api/<flower>/seeds')
def get_flower_seeds(flower):
    return {"seeds": seed_genotypes[flower]}


