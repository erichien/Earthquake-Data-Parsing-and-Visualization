(() => {
  document.addEventListener('DOMContentLoaded', () => {
    window.addEventListener('load', function(event) {
      let width = 1200;
      let height = 600;

      let inputValue = null;

      let svg = d3
        .select('.d3')
        .append('svg')
        .attr('width', width)
        .attr('height', height);

      let g = svg.append('g');

      let earthProjection = d3
        .geoAlbersUsa()
        .translate([width / 2, height / 2]);

      let geoPath = d3.geoPath().projection(earthProjection);

      g
        .selectAll('path')
        .data(northAmerica.features)
        .enter()
        .append('path')
        .attr('fill', '#eee')
        .attr('stroke', '#888')
        .attr('d', geoPath);

      let rodents = svg.append('g');

      let path = rodents
        .selectAll('path')
        .data(caliData.features)
        .enter()
        .append('path')
        .attr('fill', 'rgb(255, 180,0)')
        .attr('stroke', '#ddd')
        .attr('d', geoPath)
        .attr('class', 'incident')
        .on('mouseover', function(d) {
          d3.select('h2').text(d.properties.place);
          d3.select(this).attr('class', 'incident hover');
        })
        .on('mouseout', function(d) {
          d3.select('h2').text('');
          d3.select(this).attr('class', 'incident');
        });
    });

    // let grid = document.querySelector('.grid');
    //
    // _assignCellColor = (cell, i, j) => {
    //   if ((i + j) % 2 == 0) {
    //     cell.style.backgroundColor = '#B7D65C';
    //     // cell.style.backgroundColor = '#B6D856';
    //   } else {
    //     cell.style.backgroundColor = '#AFCF55';
    //     // cell.style.backgroundColor = '#A1CB4A';
    //   }
    // };

    // let cells = document.querySelectorAll('[data-pos]');
    //
    // for (let cell of cells) {
    //   let pos = cell.dataset.pos.split(',').map(Number);
    //   let sum = pos.reduce((i, j) => i + j);
    //
    //   if (sum % 2 == 0) {
    //     cell.style.backgroundColor = '#B6D856';
    //   } else {
    //     cell.style.backgroundColor = '#A1CB4A';
    //   }
    // }
  });
})();
