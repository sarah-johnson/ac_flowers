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
        var defaultOption = document.createElement("option")
        defaultOption.innerHTML = "Choose a color"
        defaultOption.value = 0
        colorSelector.appendChild(defaultOption)
        colorList.map(color=> {
            var option = document.createElement("option")
            option.innerHTML = color
            option.value = color
            colorSelector.appendChild(option)
        })

    })
}

var createFlowerTable = (parentElementId, tableData)=> {
    var table = d3.select(parentElementId)
        .append("table")
        .attr("class", "flower-genetics")
    var columns = d3.keys(tableData[0])
    var headers = table.append('thead')
        .append('tr')
        .selectAll('th')
        .data(columns).enter()
        .append('th')
        .attr("class", "header")
        .text((column)=> { return column })

    var rows = table.append("tbody").selectAll("tr")
        .data(tableData)
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
        .attr('data-th', (d)=> {
            return d.name
        })
        .text((d)=> {
            return d.value
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

var updateBayesParent = (color, number)=> {

}

var updateBayesUX = (flowerData)=> {
    d3.select("#bayes-calculate").on("click", ()=> {
        console.log("Calculate clicked!")
    })

    d3.select("#bayes-add-offspring").on("click", ()=> {
        console.log("Add Offspring clicked!")
    })

    d3.select("#bayes-clear-offspring").on("click", ()=> {
        console.log("Clear Offspring clicked!")
    })

    d3.select("#bayes-parent1-select").on("change", ()=> {
        parentColor = d3.event.target.value
        d3.select("#bayes-parent1-genetic-p").html("")
        createFlowerTable(
            "#bayes-parent1-genetic-p",
            flowerData['flower_info'].filter((row)=> {
                return row['color'] === parentColor
            })
        )
    })

    d3.select("#bayes-parent2-select").on("change", ()=> {
        parentColor = d3.event.target.value
        d3.select("#bayes-parent2-genetic-p").html("")
        createFlowerTable(
            "#bayes-parent2-genetic-p",
            flowerData['flower_info'].filter((row)=> {
                return row['color'] === parentColor
            })
        )
    })

    updateColorSelectors(flowerData.colors)
}

var renderBayesUX = (flowerData)=> {
    var display = document.getElementById("app-content")
    // Get the basic bayes UX HTML template
    fetch("/bayes")
      .then(response=>response.text())
      .then(data=>display.innerHTML = data)
      .then(_=>updateBayesUX(flowerData))
}

var renderExploreUX = (flower, flowerData)=> {
    var data = flowerData['flower_info']
    createFlowerTable("#app-content", flowerData['flower_info'])
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
