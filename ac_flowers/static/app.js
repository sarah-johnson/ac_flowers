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

var renderBayesUX = (currentFlower, flowerData)=> {
    var appContent = d3.select("#app-content")

    var aboutBayes = appContent.append("div").attr("id", "about-bayes")
    fetch("static/about_bayes.html")
        .then(response=>response.text())
        .then(text=> aboutBayes.html(text))

    // Variables to use in calculation
    var bayesFlowerColors = {
        "parent1": "",
        "parent2": "",
        "target": "",
    }
    var childrenColors = []

    var bayesUX = appContent.append("div").attr("id", "bayes-ux")

    // Add parent elements
    Object.keys(bayesFlowerColors).forEach( (flower)=> {
        var flowerDisplayId = "bayes-" + flower + '-display'

        var flowerUX = bayesUX.append("div").attr("id", "bayes-" + flower)
        flowerUX.append("h3").text("Select " + flower + " color:")
        var selector = flowerUX.append("select")
            .attr("id", "bayes-" + flower + "-select")
            .attr("class", "flower-color-list")
            .on("change", ()=> {
                var color = d3.event.target.value

                // update calc variable
                bayesFlowerColors[flower] = color

                // update UI
                var flowerDisplay = d3.select("#" + flowerDisplayId).html("").attr("class", color)
                flowerDisplay.append("h4").text("Prior Probabilities for " + flower)
                var flowerInfo = flowerData["flower_info"].filter((row)=> {
                    return row.color === color
                })
                var prior_p = 1/flowerInfo.length
                prior_p = prior_p.toFixed(2)
                flowerInfo = flowerInfo.map((row)=> {
                    return {"genotype": row.genotype, "seed": row.seed, "p": prior_p}
                })
                createFlowerTable("#" + flowerDisplayId, flowerInfo)
            })

        selector.selectAll("option")
            .data(["Choose " + flower].concat(flowerData.colors)).enter()
            .append("option")
            .attr("value", (color)=> { return color })
            .text((color)=> { return color })

        var flowerDisplay = flowerUX.append("div").attr("id", flowerDisplayId)
    })

    // Add children elements
    var childrenUX = bayesUX.append("div")
        .attr("id", "bayes-children-ux")
    childrenUX.append("h3").text("Add or change offspring:")
    childrenUX.append("button").text("Add Offspring")
        .attr("id", "bayes-add-offspring")
        .on("click", ()=> {
            var observedColor = window.prompt("What color offspring did you observe?", "");
            while (!flowerData['colors'].includes(observedColor)) {
                observedColor = window.prompt(observedColor + " is not a valid color. Please try again:", "")
            }
            // Update calc variable
            childrenColors.push(observedColor)

            // Update UI
            childrenDisplay.append("div").attr("class", observedColor + " flower-child")

        })

    childrenUX.append("button").text("Clear Offspring")
        .attr("id", "bayes-clear-offspring")
        .on("click", ()=> {
            // Update calc variable
            childrenColors = []

            // Update UI
            childrenDisplay.html("")
            childrenDisplay.append("h4").text("Observed Children")
        })

    var childrenDisplay = childrenUX.append("div").attr("id", "bayes-children-display")
    childrenDisplay.append("h4").text("Observed Children")

    // Fetch and format results
    var resultsDisplay = bayesUX.append("div").attr("id", "bayes-results-display")

    // Given a genotype return the phenotype
    var assignColor = (tableElement)=> {
        var filtered = flowerData.flower_info.filter((row)=> {
            return row.genotype === tableElement.value
        })
        if (filtered.length > 0) {
            return filtered.pop().color
        }
        return ""
    }

    var formatBayesResults = (data)=> {
        var resultsDisplay = d3.select("#bayes-results-display").html("")
        var posteriors = data.posteriors
        resultsDisplay.append("h4").text("Posterior probabilities for parent combinations")
        if (posteriors.length > 0) {
            createFlowerTable("#bayes-results-display", posteriors)

            // Add colors to the parent posteriors table
            resultsDisplay.select("table")
                .select("tbody")
                .selectAll("tr")
                .selectAll("td")
                .attr("class", (cell)=> {
                    return assignColor(cell)
                })
            if (data.total_target_p) {
                resultsDisplay.append("h1").text("Total Target Flower Probability is " + data.total_target_p)
            }
        } else {
            resultsDisplay.append("h4").text("No possible paths for given parents/children 😢")
        }
    }

    appContent.append("button").text("Calculate!")
        .attr("id", "bayes-calculate")
        .on("click", ()=> {
            var requestData = {
                "flower_type": currentFlower,
                "parent1": bayesFlowerColors.parent1,
                "parent2": bayesFlowerColors.parent2,
                "children": childrenColors
            }
            if (bayesFlowerColors.target.length > 0) {
                requestData["target_color"] = bayesFlowerColors.target
            }
            fetch("api/bayes", {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(requestData)
            })
                .then(response=>response.json())
                .then(data=>formatBayesResults(data))
        })
}

var renderExploreUX = (currentFlower, flowerData)=> {
    createFlowerTable("#app-content", flowerData['flower_info'])
}

var setAppContent = (currentFlower, flowerData)=> {
    var moduleSelector = document.getElementById("module-select")
    var moduleName = moduleSelector.value

    var appTitle = document.getElementById("app-title")
    appTitle.innerHTML = moduleName + " " + currentFlower

    var display = document.getElementById("app-content")
    display.innerHTML = "" // always start with a fresh display
    if (moduleName === "explore") {
        renderExploreUX(currentFlower, flowerData)
    } else if (moduleName === "bayes") {
        renderBayesUX(currentFlower, flowerData)
    } else {
        display.innerHTML = "Unexpected input. :("
    }   
}

var initializeApp = ()=> {
    var flowerSelector = document.getElementById("flower-select")
    var currentFlower = flowerSelector.value
    fetch("/api/" + currentFlower)
        .then(response=>response.json())
        .then(flowerData=>setAppContent(currentFlower, flowerData))
}

// Populate the initial flower-selector dropdown
fetch("/api/list-flowers")
    .then(response=>response.json())
    .then(data=>populateFlowerSelector(data.flowers))

// Trigger actions when the flower-selector dropdown or module list are changed
d3.select("#flower-select").on("change", ()=> {initializeApp()})
d3.select("#module-select").on("change", ()=> {initializeApp()})
