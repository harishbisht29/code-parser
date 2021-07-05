// Empty JS for your own code to be here
function make_random_color(alpha = 1) {
    alpha = alpha * 100
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    // console.log(color+20)
    return color + alpha;
}

chart_obj_template =
{
    type: '__your__type',
    data: {
        labels: '__label__list',
        datasets: [{
            label: '',
            data: [12, 19, 3, 5, 12, 19, 3, 5],
            backgroundColor: [
            ],
            borderColor: [
            ],
            borderWidth: 1
        }]
    },
    options: {
        plugins: {
            title: {
                display: true,
                text: 'Custom Chart Title',
                position: 'bottom'
            },
            legend: {
                display: false
            }
        },
        indexAxis: 'x',
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
}

function create_chart_object(type, data, label, title, props) {
    // deep copy the chart_obj_template
    obj= JSON.parse(JSON.stringify(chart_obj_template))

    obj['type'] = type
    obj['data']['datasets'][0]['data'] = data
    obj['data']['labels'] = label
    obj['options']['plugins']['title']['text'] = title

    if(type.toLowerCase() == 'bar'){
        if(props['axis'] == 'h'){
            obj['options']['indexAxis'] = 'y'
        }
    }
    if (type.toLowerCase() == 'pie' || type.toLowerCase() == 'doughnut'){
        obj['options']['plugins']['legend']['display']= true
    }

    background_color= []
    border_color= []
    for( var i=0; i< data.length; i++){
        background_color.push(make_random_color(.2))
        border_color.push(make_random_color(.7))
    }
    // console.log(background_color)
    // console.log(border_color)
    obj['data']['datasets'][0]['backgroundColor']= background_color
    obj['data']['datasets'][0]['borderColor']= border_color
    
    return obj
}
