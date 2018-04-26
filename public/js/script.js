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
  });
})();
