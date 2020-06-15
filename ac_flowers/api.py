import logging

from flask import Blueprint, request

from .flower import all_flowers_genotype_map, seed_genotypes, Flower, FlowerInstance
from .utilities import bayes

logger = logging.getLogger(__name__)
api = Blueprint("api", __name__, template_folder="templates")


@api.route("/api/list-flowers")
def list_flowers():
    """
    List all possible flowers
    """
    return {"flowers": list(all_flowers_genotype_map)}


@api.route("/api/<flower>")
def get_flower_info(flower):
    """
    Return all the "baseline" information regarding a given flower
    """
    flower_info = [
        {
            "genotype": str(genotype),
            "color": phenotype,
            "seed": "seed" if genotype in seed_genotypes[flower].values() else "",
        }
        for genotype, phenotype in all_flowers_genotype_map[flower].items()
    ]

    return {
        "flower_info": flower_info,
        "colors": list(set(all_flowers_genotype_map[flower].values())),
    }


@api.route("/api/bayes", methods=["POST"])
def api_bayes():
    """
    Input data: type of flower, colors of both parents, and any observed children.
    Optioanlly include a target flower color
    Returns a breakdown of all possible children with probabilities
    """
    flower_type = request.json["flower_type"]
    assert flower_type in all_flowers_genotype_map, "Invalid flower"

    valid_colors = set(all_flowers_genotype_map[flower_type].values())
    flower_factory = Flower(flower_type)

    parent1_color = request.json["parent1"]
    parent2_color = request.json["parent2"]
    target_color = request.json.get("target_color")
    assert parent1_color in valid_colors, "Invalid color for parent 1"
    assert parent2_color in valid_colors, "Invalid color for parent 2"
    if target_color:
        assert target_color in valid_colors, "Invalid color for target"

    children = request.json.get("children", [])

    posteriors = bayes(
        flower_type=flower_type,
        color1=parent1_color,
        color2=parent2_color,
        observed_children_colors=children,
    )

    results_table = []
    for parents, posterior_p in posteriors.items():
        row = {}
        row["parent1"] = str(parents[0])
        row["parent2"] = str(parents[1])
        row["posterior_p"] = round(posterior_p, 3)

        # Returns dictionary of flowerInstances and probabilities
        child_p = flower_factory.create(parents[0]).all_children_with_weights(
            flower_factory.create(parents[1]))
        row['all_child_p'] = {str(child.genotype): p for child, p in child_p.items()}

        if target_color:
            row['target_color_p'] = round(sum([
                p for child, p in child_p.items()
                if child.phenotype == target_color
            ]), 3)
        results_table.append(row)

    response = {"posteriors": results_table}

    if target_color:
        response["total_target_p"] = round(sum([
            row['target_color_p'] * row["posterior_p"]
        ]), 3)

    return response
