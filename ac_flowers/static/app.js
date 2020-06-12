// Populate the flower-select dropdown
var populateFlowerList = (flowerList)=> {
    var flowerSelector = document.getElementById('flower-select')
    flowerSelector.innerHTML = ""
    flowerList.map(flower=> {
        var option = document.createElement("option")
        option.innerHTML = flower
        option.value = flower
        flowerSelector.appendChild(option)
    })
}

var markSeedFlowers = (seeds)=> {
    // Take the flowerGenetics table, look for any trs that
    // have a seed genotype, and add some icon for a seed bag
}

// For a given flower, create a table of genotype and phenotype possibilities.
var formatGeneticsDisplay = (flower, flowerData)=> {
    var display = document.getElementById('flower-genetics-display')
    display.innerHTML = ""
    
    var table = document.createElement("TABLE")
    table.setAttribute("id", "flowerGenetics")
    var headerRow = document.createElement("TR")
    table.appendChild(headerRow)
    var c = document.createElement("TH")
    c.innerHTML = "GENOTYPE"
    headerRow.appendChild(c)
    var c = document.createElement("TH")
    c.innerHTML = "PHENOTYPE"
    headerRow.appendChild(c)

    for (genotype in flowerData) {
        phenotype = flowerData[genotype]

        var row = document.createElement("TR")
        row.setAttribute("class", phenotype)
        table.appendChild(row)
        
        var genotypeColumn = document.createElement("TD")
        genotypeColumn.innerHTML = genotype
        row.appendChild(genotypeColumn)
        
        var phenotypeColumn = document.createElement("TD")
        phenotypeColumn.innerHTML = phenotype
        row.appendChild(phenotypeColumn)
    }

    display.appendChild(table)

    fetch("/api/" + flower + "/seeds")
        .then(response=>response.json())
        .then(data=>markSeedFlowers(data.seeds))
}

// Populate the first dropdown
fetch("/api/list-flowers")
  .then(response=>response.json())
  .then(data=>populateFlowerList(data.flowers))

// Trigger actions when the dropdown is touched
var flowerSelector = document.getElementById('flower-select')
flowerSelector.addEventListener("change", (e)=> {
    var currentFlower = document.getElementById('current-flower')
    currentFlower.innerHTML = e.target.value
    fetch("/api/" + e.target.value)
        .then(response=>response.json())
        .then(data=>formatGeneticsDisplay(e.target.value, data.flower_info))
})
