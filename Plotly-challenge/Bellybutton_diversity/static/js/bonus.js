
let buildGauge = wfreq => {
    // Enter a speed between 0 and 180
    let level = wfreq;

    // Trig to calc meter point
    let radius = .5;
    let radians = (1 - wfreq / 9) * Math.PI;
    let x = radius * Math.cos(radians);
    let y = radius * Math.sin(radians);

    // Path: may have to change to create a better triangle
    let mainPath = 'M -.0 -0.025 L .0 0.025 L ',
        pathX = String(x),
        space = ' ',
        pathY = String(y),
        pathEnd = ' Z';
    let path = mainPath.concat(pathX, space, pathY, pathEnd);

    let test =  ['8-9', '7-8', '6-7', '5-6', '4-5', '3-4', '2-3', '1-2', '0-1', ''];

    let data = [{
        type: 'scatter',
        x: [0], y: [0],
        marker: { size: 28, color: '850000' },
        showlegend: false,
        name: 'speed',
        text: level,
        hoverinfo: 'text+name'
    },
    {
        values: [50 / 9, 50 / 9, 50 / 9, 50 / 9, 50 / 9, 50 / 9, 50 / 9, 50 / 9, 50 / 9, 50],
        rotation: 90,
        text: test,
        textinfo: 'text',
        textposition: 'inside',
        marker: {
            colors: [
                'rgba(14, 127, 0, .5)',
                'rgba(41, 139, 25, .5)',
                'rgba(68, 151, 50, .5)', 
                'rgba(96, 164, 75, .5)', 
                'rgba(123, 176, 101, .5)',
                'rgba(150, 189, 126, .5)', 
                'rgba(177, 201, 151, .5)',
                'rgba(204, 214, 176, .5)', 
                'rgba(232, 226, 202, .5)',
                'rgba(255, 255, 255, 0)']
        },
        labels:test,
        hoverinfo: 'label',
        hole: .5,
        type: 'pie',
        showlegend: false
    }];

    let layout = {
        shapes: [{
            type: 'path',
            path: path,
            fillcolor: '850000',
            line: {
                color: '850000'
            }
        }],
        title: '<b>Belly Button Washing Frequency</b> <br>Scrubs per Week',
        height: 500,
        width: 500,
        xaxis: {
            zeroline: false, showticklabels: false,
            showgrid: false, range: [-1, 1]
        },
        yaxis: {
            zeroline: false, showticklabels: false,
            showgrid: false, range: [-1, 1]
        }
    };

    Plotly.newPlot('gauge', data, layout);
}

