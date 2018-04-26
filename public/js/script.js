(() => {
  document.addEventListener('DOMContentLoaded', () => {
    window.addEventListener('load', function(event) {
      let width = 1000;
      let height = 800;
      let inputValue = null;

      let svg = d3
        .select('.d3')
        .append('svg')
        .attr('width', width)
        .attr('height', height)
        .attr('translate', width / 3);

      let g = svg.append('g');

      let earthProjection = d3.geoAlbersUsa();

      let geoPath = d3.geoPath().projection(earthProjection);

      g
        .selectAll('path')
        .data(northAmerica.features)
        .enter()
        .append('path')
        .attr('fill', '#eee')
        .attr('stroke', '#aaa')
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
          d3.select('.d3-data').text(d.properties.place);
          d3.select(this).attr('class', 'incident hover');
        })
        .on('mouseout', function(d) {
          d3
            .select('.d3-data')
            .text('(hover over data points to view earthquake info)');
          d3.select(this).attr('class', 'incident');
        });
    });
  });
})();