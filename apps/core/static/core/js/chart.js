function renderize_chart_films(url) {
    fetch(url, {
        method: 'get'
    }).then(function(result) {
        return result.json()
    }).then(function(response) {
        var ctx = document.getElementById("chartFilms");
        // <block:setup:1>
        const data = {
            labels: [
            'Gostaria de Assistir',
            'Assistidos'
            ],
            datasets: [{
            label: 'Gráfico de seus filmes',
            data: response.data,
            backgroundColor: [
                'rgb(255, 99, 132)',
                'rgb(54, 162, 235)',
            ],
            hoverOffset: 4
            }]
        };
        // </block:setup>
        
        // <block:config:0>
        const config = {
            type: 'pie',
            data: data,
            options: {
                responsive: false,
            }
        };
        // </block:config>

        var chart = new Chart(ctx, config)
    })
}