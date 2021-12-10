function actualizarChart(valores,chartdiv){
    console.log(valores)
    AmCharts.makeChart(chartdiv,
{
    "type": "serial",
    "categoryField": "category",
    "startDuration": 0,
    "addClassNames": true,
    "categoryAxis": {
        "axisThickness": 0,
        "color": "#333333",
        "dashLength": 5,
        "gridAlpha": 0.11,
        "tickLength": 0
    },
    "chartCursor": {
        "enabled": true,
        "bulletsEnabled": true,
        "bulletSize": 20,
        "categoryBalloonColor": "#FCD6A9",
        "color": "#000000",
        "cursorColor": "#FCD6A9",
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
            "balloonColor": "#FCD6A9",
            "bullet": "round",
            "bulletBorderAlpha": 1,
            "bulletBorderColor": " #2684FC",
            "bulletColor": "#FFFFFF",
            "color": " #2684FC",
            "cursorBulletAlpha": 0,
            "customBullet": "",
            "fillAlphas": 0.1,
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
            "maximum": 30,
            "minimum": 15,
            "axisThickness": 0,
            "color": "#333333",
            "dashLength": 5,
            "gridAlpha": 0.05,
            "labelFrequency": 2,
            "tickLength": 0,
            "title": ""
        }
    ],
    "allLabels": [],
    "balloon": {},
    "legend": {
        "enabled": true,
        "align": "right",
        "position": "top",
        "useGraphSettings": true
    },
    "titles": [],
    "dataProvider": [
        {
            "category": valores[9].timestamp,
            "column-1": valores[9].valor,
        },
        {
            "category": valores[8].timestamp,
            "column-1": valores[8].valor,
        },
        {
            "category": valores[7].timestamp,
            "column-1": valores[7].valor,
        },
        {
            "category": valores[6].timestamp,
            "column-1": valores[6].valor,
        },
        {
            "category": valores[5].timestamp,
            "column-1": valores[5].valor,
        },
        {
            "category": valores[4].timestamp,
            "column-1": valores[4].valor,
        },
        {
            "category": valores[3].timestamp,
            "column-1": valores[3].valor,
        },
        {
            "category": valores[2].timestamp,
            "column-1": valores[2].valor,
        },
        {
            "category": valores[1].timestamp,
            "column-1": valores[1].valor,
        },
        {
            "category": valores[0].timestamp,
            "column-1": valores[0].valor,
        },
    ]
}
);
}