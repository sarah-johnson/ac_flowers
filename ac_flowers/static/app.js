// Populate the flower-select dropdown
var populateFlowerSelector = (flowerList)=> {
    var flowerSelector = document.getElementById('flower-select')
    flowerSelector.innerHTML = ""
    var option = document.createElement("option")
    option.innerHTML = "Select a flower"
    option.value = 0
    flowerSelector.appendChild(option)
    flowerList.map(flower=> {
        var option = document.createElement("option")
        option.innerHTML = flower
        option.value = flower
        flowerSelector.appendChild(option)
    })
}

var updateColorSelectors = (colorList)=> {
    var colorSelectors = document.getElementsByClassName("flower-color-list")
    Array.from(colorSelectors).forEach((colorSelector) => {
        colorSelector.innerHTML = ""
        colorList.map(color=> {
            var option = document.createElement("option")
            option.innerHTML = color
            option.value = color
            colorSelector.appendChild(option)
        })
    })
}

var renderBayesUX = (colorList)=> {
    var display = document.getElementById("app-content")
    // Get the basic bayes UX HTML template
    fetch("/bayes")
      .then(response=>response.text())
      .then(data=>display.innerHTML = data)
      .then(_=>updateBayesUX(colorList))
}

var updateBayesUX = (colorList)=> {
    updateColorSelectors(colorList)

    var bayesCalculateButton = document.getElementById('bayes-calculate')
    bayesCalculateButton.addEventListener("click", ()=> {
        console.log("Calculate clicked!")
    })

    var bayesAddOffspringButton = document.getElementById('bayes-add-offspring')
    bayesAddOffspringButton.addEventListener("click", ()=> {
        console.log("Add Offspring clicked!")
    })

    var bayesClearOffspringButton = document.getElementById('bayes-clear-offspring')
    bayesClearOffspringButton.addEventListener("click", ()=> {
        console.log("Clear Offspring clicked!")
    })

    var parent1Select = document.getElementById("bayes-parent1-select")
    parent1Select.addEventListener("change", (e)=> {
        console.log("Parent 1 changed to " + e.target.value)
    })

    var parent2Select = document.getElementById("bayes-parent2-select")
    parent2Select.addEventListener("change", (e)=> {
        console.log("Parent 2 changed to " + e.target.value)
    })
}

var updateParentPossibilities = (parent, possibilities)=> {
    console.log("updating the possibilities of " + parent + " to " + possibilities)
}

// For a given flower, create a table of genotype and phenotype possibilities.
var createGenotypeTable = (flower, flowerData)=> {
    var display = document.getElementById("app-content")
    display.innerHTML = ""
    
    var table = document.createElement("TABLE")
    table.setAttribute("id", "flowerGenetics")
    var headerRow = document.createElement("TR")
    table.appendChild(headerRow)

    var columnHeaders = ["Genotype", "Phenotype", "Seed"]
    columnHeaders.map(column=> {
        var c = document.createElement("TH")
        c.innerHTML = column
        headerRow.appendChild(c)
    })

    flowerData.map(data_row=> {
        var row = document.createElement("TR")
        row.setAttribute("class", data_row[1]) // phenotype
        table.appendChild(row)

        data_row.map(column=> {
            var c = document.createElement("TD")
            c.innerHTML = column
            row.appendChild(c)
        })
    })

    display.appendChild(table)
}

var setAppContent = (flower, data)=> {
    var moduleSelector = document.getElementById("module-select")
    moduleName = moduleSelector.value

    var appTitle = document.getElementById("app-title")
    appTitle.innerHTML = moduleName + " " + flower

    var display = document.getElementById("app-content")
    if (moduleName === "explore") {
        createGenotypeTable(flower, data.flower_info)
    } else if (moduleName === "bayes") {
        renderBayesUX(data.colors)
    } else {
        display.innerHTML = "Unexpected input. :("
    }   
}

var initializeApp = ()=> {
    var flowerSelector = document.getElementById("flower-select")
    flower = flowerSelector.value
    fetch("/api/" + flower)
      .then(response=>response.json())
      .then(data=>setAppContent(flower, data))
}

// Populate the initial flower-selector dropdown
fetch("/api/list-flowers")
  .then(response=>response.json())
  .then(data=>populateFlowerSelector(data.flowers))

// Trigger actions when the flower-selector dropdown is changed
var flowerSelector = document.getElementById("flower-select")
flowerSelector.addEventListener("change", (e)=> {
    initializeApp()
})

// Trigger actions when the module list is changed
var moduleSelector = document.getElementById("module-select")
moduleSelector.addEventListener("change", (e)=> {
    initializeApp()
})
