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

var renderBayesUX = (flowerData)=> {
    var display = document.getElementById("app-content")
    // Get the basic bayes UX HTML template
    fetch("/bayes")
      .then(response=>response.text())
      .then(data=>display.innerHTML = data)
      .then(_=>updateBayesUX(flowerData))
}

var updateBayesUX = (flowerData)=> {
    updateColorSelectors(flowerData.colors)

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
        parentColor = e.target.value
        var parentGeneticsContainer = document.getElementById("bayes-parent1-genetic-p")
        possibleGenotypes = flowerData['flower_info'].filter((row)=> {
            row['color'] === parentColor
        })
        console.log("Parent 1 changed to " + e.target.value)
        console.log("Possible genotypes are " + possibleGenotypes)
    })

    var parent2Select = document.getElementById("bayes-parent2-select")
    parent2Select.addEventListener("change", (e)=> {
        console.log("Parent 2 changed to " + e.target.value)
    })
}

var renderExploreUX = (flower, flowerData)=> {
    var data = flowerData['flower_info']
    var table = d3.select("#app-content").append("table").attr("id", "flowerGenetics")
    var columns = d3.keys(data[0])
    var headers = table.append('thead')
        .append('tr')
        .selectAll('th')
        .data(columns).enter()
        .append('th')
        .attr("class", "header")
        .text((column)=> { return column })

    var rows = table.append("tbody").selectAll("tr")
        .data(data)
        .enter()
        .append('tr')
        .attr("class", (row)=> {
            return row['color']
        })

    rows.selectAll('td')
        .data((row)=> {
            return columns.map((column)=> {
                return { 'value': row[column], 'name': column};
            })
        }).enter()
        .append('td')
        .attr('data-th', function (d) {
            return d.name;
        })
        .text((d)=> {
            return d.value;
        })

    // provide sort functionality
    var sortAscending = true
    headers.on('click', (column)=> {
        if (sortAscending) {
            rows.sort((a, b)=> {
                if (a[column] < b[column]) { return -1 }
                else if (a[column] > b[column]) { return 1 }
                else { return 0 }
            })
            sortAscending = false
        } else {
            rows.sort((a, b)=> {
                if (a[column] < b[column]) { return 1 }
                else if (a[column] > b[column]) { return -1 }
                else { return 0 }
            })
            sortAscending = true
        }
    })
}

var setAppContent = (flower, flowerData)=> {
    var moduleSelector = document.getElementById("module-select")
    moduleName = moduleSelector.value

    var appTitle = document.getElementById("app-title")
    appTitle.innerHTML = moduleName + " " + flower

    var display = document.getElementById("app-content")
    display.innerHTML = "" // always start with a fresh display
    if (moduleName === "explore") {
        renderExploreUX(flower, flowerData)
    } else if (moduleName === "bayes") {
        renderBayesUX(flowerData)
    } else {
        display.innerHTML = "Unexpected input. :("
    }   
}

var initializeApp = ()=> {
    var flowerSelector = document.getElementById("flower-select")
    flower = flowerSelector.value
    fetch("/api/" + flower)
      .then(response=>response.json())
      .then(flowerData=>setAppContent(flower, flowerData))
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
