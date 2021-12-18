
function actualizarChart(valores,chartdiv){

    if (chartdiv== 'chartdivTemperatura'){
        min= 0;
        max= 50;
    }else {
        min= 20;
        max= 90;
    }  

    diccionario= {
        "type": "serial",
        "categoryField": "category",
        "startDuration": 0,
        "addClassNames": true,
        "backgroundColor": "#F5F3F5",
        "backgroundAlpha": 1,
        "categoryAxis": {
            "axisThickness": 2,
            "color": "#333333",
            "dashLength": 5,
            "gridAlpha": 2,
            "tickLength": 2
        },
        "chartCursor": {
            "enabled": true,
            "bulletsEnabled": true,
            "bulletSize": 20,
            "categoryBalloonColor": "blue"/*"#FCD6A9"*/,
            "color": "#000000",
            "cursorColor": "blue"/*"#FCD6A9"*/,
            "graphBulletAlpha": 0,
            "graphBulletSize": 0,
            "selectionAlpha": 0,
            "selectWithoutZooming": true,
            "valueLineAlpha": 0,
            "zoomable": false
        },
        "trendLines": [],
        "graphs": [
            {
                "balloonColor": "#0331c991"/*"#FCD6A9"*/,
                "bullet": "round",
                "bulletBorderAlpha": 1,
                "bulletBorderColor": "#2684FC",
                "bulletColor": "#FFFFFF",
                "color": " #2684FC",
                "cursorBulletAlpha": 0,
                "customBullet": "",
                "fillAlphas": 0.5,
                "fillToAxis": "x",
                "fontSize": 20,
                "id": "AmGraph-2",
                "title": chartdiv,
                "labelPosition": "bottom",
                "lineColor": " #2684FC",
                "lineThickness": 3,
                "type": "smoothedLine",
                "valueField": "column-1"
            }
        ],
        "guides": [],
        "valueAxes": [
            {
                "id": "ValueAxis-1",
                "minimum": min,
                'maximum': max,
                "axisThickness": 0,
                "color": "#333333",
                "dashLength": 5,
                "gridAlpha": 2,
                "labelFrequency": 2,
                "tickLength": 0,
                "title": ""
            }
        ],
        "allLabels": [],
        "balloon": {},
        "legend": {
            "enabled": false,
            "align": "right",
            "position": "top",
            "useGraphSettings": true
        },
        "titles": [],
        "dataProvider": []
    }
    for (let i in valores.reverse()) {
        minidiccionario= {
            "category": valores[i].timestamp,
            "column-1": valores[i].valor
        }
        diccionario.dataProvider.push(minidiccionario)
    }      

    AmCharts.makeChart(chartdiv,diccionario);
}