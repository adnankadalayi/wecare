//Radial Chart 1
var options = {
    series: [93],
    chart: {
        height: 220,
        type: 'radialBar',
    },
    colors: ['#396cf0'],
    plotOptions: {
        radialBar: {
            track: {
              background: '#b9c1d4',
              opacity: 0.5,            
            },
            hollow: {
                size: '70%',
            },
            dataLabels: {
                name: {
                  show: false,
                },
                value: {
                  fontSize: '20px',
                  offsetY: 10,
                },
            },
        },
    },
    stroke: {
        lineCap: 'round',
    },
};

var chart = new ApexCharts(document.querySelector("#rchart-1"), options);
chart.render();

//chart 2
var options = {
    series: [{
        data: [10, 25, 30, 54, 45, 39, 15]
    }],
    chart: {
        type: 'area',
        height: 90,
        width: '100%',
        sparkline: {
            enabled: true
        }
    },
    stroke: {
        curve: 'smooth',
        width: 3,
    },
    colors: ['#53c797'],
    fill: {
        type: 'gradient',
        gradient: {
            shadeIntensity: 1,
            inverseColors: false,
            opacityFrom: 0.45,
            opacityTo: 0.05,
            stops: [20, 100, 100, 100]
        },
    },
    tooltip: {
        fixed: {
            enabled: false
        },
        x: {
            show: false
        },
        y: {
            title: {
                formatter: function (seriesName) {
                    return ''
                }
            }
        },
        marker: {
            show: false
        }
    }
};

var chart = new ApexCharts(document.querySelector("#rchart-2"), options);
chart.render();


//Chart 3
var options = {
    series: [{
        data: [15, 20, 10, 45, 20, 10, 5]
    }],
    chart: {
        type: 'area',
        height: 90,
        width: '100%',
        sparkline: {
            enabled: true
        }
    },
    stroke: {
        curve: 'smooth',
        width: 3,
    },
    colors: ['#f0735a'],
    fill: {
        type: 'gradient',
        gradient: {
            shadeIntensity: 1,
            inverseColors: false,
            opacityFrom: 0.45,
            opacityTo: 0.05,
            stops: [20, 100, 100, 100]
        },
    },
    tooltip: {
        fixed: {
            enabled: false
        },
        x: {
            show: false
        },
        y: {
            title: {
                formatter: function (seriesName) {
                    return ''
                }
            }
        },
        marker: {
            show: false
        }
    }
};

var chart = new ApexCharts(document.querySelector("#rchart-3"), options);
chart.render();


//Radial Chart 4
var options = {
    series: [90],
    chart: {
        height: 220,
        type: 'radialBar',
    },
    colors: ['#f1b561'],
    plotOptions: {
        radialBar: {
            track: {
              background: '#b9c1d4',
              opacity: 0.5,            
            },
            hollow: {
                size: '70%',
            },
            dataLabels: {
                name: {
                  show: false,
                },
                value: {
                  fontSize: '20px',
                  offsetY: 10,
                },
            },
        },
    },
    stroke: {
        lineCap: 'round',
    },
};

var chart = new ApexCharts(document.querySelector("#rchart-4"), options);
chart.render();