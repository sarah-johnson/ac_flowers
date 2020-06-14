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

var renderBayesUX = (flowerData)=> {
    var appContent = d3.select("#app-content")

    var aboutBayes = appContent.append("div").attr("id", "about-bayes")
    fetch("static/about_bayes.html")
        .then(response=>response.text())
        .then(text=> aboutBayes.html(text))

    var bayesUX = appContent.append("div").attr("id", "bayes-ux")

    var parents = ["parent1", "parent2"]
    parents.forEach( (flower)=> {
        var flowerDisplayId = "bayes-" + flower + "-display"
        var flowerDisplay = bayesUX.append("div").attr("id", flowerDisplayId)

        var flowerUXId = "bayes-" + flower + "-ux"
        var flowerUX = bayesUX.append("div").attr("id", flowerUXId)
        flowerUX.append("h3").text("Select " + flower + " color:")
        var selector = flowerUX.append("select")
            .attr("id", "bayes-" + flower + "-select")
            .attr("class", "flower-color-list")
            .on("change", ()=> {
                var color = d3.event.target.value
                var flowerDisplay = d3.select("#" + flowerDisplayId).html("").attr("class", color)
                flowerDisplay.append("h4").text("Prior Probabilities for " + flower)
                var flowerInfo = flowerData["flower_info"].filter((row)=> {
                    return row.color === color
                })
                var prior_p = 1/flowerInfo.length
                prior_p = prior_p.toFixed(2)
                flowerInfo = flowerInfo.map((row)=> {
                    return {
                        "genotype": row.genotype,
                        "seed": row.seed,
                        "p": prior_p
                    }
                })

                createFlowerTable(
                    "#" + flowerDisplayId,
                    flowerInfo
                )
            })

        selector.selectAll("option")
            .data(["Choose " + flower].concat(flowerData.colors)).enter()
            .append("option")
            .attr("value", (color)=> { return color })
            .text((color)=> { return color })
    })

    var childrenUX = bayesUX.append("div")
        .attr("id", "bayes-children-ux")

    childrenUX.append("button").text("Add Offspring")
        .attr("id", "bayes-add-offspring")
        .on("click", ()=> {
            console.log("Add Offspring clicked!")
        })

    childrenUX.append("button").text("Clear Offspring")
        .attr("id", "bayes-clear-offspring")
        .on("click", ()=> {
            console.log("Clear Offspring clicked!")
        })

    childrenDisplay = bayesUX.append("div")
        .attr("id", "bayes-children-display")

    childrenDisplay.append("h4").text("Observed Children")

    appContent.append("button").text("Calculate!")
        .attr("id", "bayes-calculate")
        .on("click", ()=> {
            console.log("Calculate clicked!")
        })

    //     })
    // }

    //   <div class="flowerbed" id="bayes-parents-genetic-p">
    //     Parent Genes Probabilities
    //     <div id="bayes-parent1-genetic-p"></div>
    //     <div id="bayes-parent2-genetic-p"></div>
    //   </div>
    //   <div class="flowerbed" id="bayes-parents-flowerbed">Parents Colors
    //     <div class="flowerbox" id="bayes-parent1-flowerbox">
    //       Choose Parent 1 Color
    //       <select id="bayes-parent1-select" class="flower-color-list">
    //         <option>---</option>
    //       </select>
    //     </div>
    //     <div class="flowerbox" id="bayes-parent2-flowerbox">
    //       Choose Parent 2 Color
    //       <select id="bayes-parent2-select" class="flower-color-list">
    //         <option>---</option>
    //       </select>
    //     </div>
    //   </div>
    //   <div class="flowerbed" id="bayes-observed-offspring-flowerbed">Children Observed Colors</div>
    //   <div class="flowerbed" id="bayes-future-offspring-p-flowerbed">Future Children Probabilities</div>

    // </div>
}

var renderExploreUX = (flowerData)=> {
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
        renderExploreUX(flowerData)
    } else if (moduleName === "bayes") {
        renderBayesUX(flowerData)
    } else {
        display.innerHTML = "Unexpected input. :("
    }   
}

var initializeApp = ()=> {
    var flowerSelector = document.getElementById("flower-select")
    var flower = flowerSelector.value
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
