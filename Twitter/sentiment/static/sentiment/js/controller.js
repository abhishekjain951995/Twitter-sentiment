var app = angular.module('TwitterSentiment',[]);

app.controller('GraphCtrl',['$scope',function($scope){
  var testdata = [
      {key: "One", y: 5},
      {key: "Two", y: 2},
      {key: "Three", y: 9},
      {key: "Four", y: 7},
      {key: "Five", y: 4},
      {key: "Six", y: 3},
      {key: "Seven", y: 0.5}
  ];

  var height = 350;
  var width = 350;
  var chart1;
  nv.addGraph(function() {
      var chart1 = nv.models.pieChart()
          .x(function(d) { return d.key })
          .y(function(d) { return d.y })
          .donut(true)
          .width(width)
          .height(height)
          .padAngle(.08)
          .cornerRadius(5)
          .id('donut1'); // allow custom CSS for this one svg

      chart1.title("100%");
      chart1.pie.donutLabelsOutside(true).donut(true);

      d3.select("#test1")
          .datum(testdata)
          .transition().duration(1200)
          .call(chart1);

      return chart1;

  });

}])


app.controller('LineGraphCtrl',['$scope',function($scope){
  // Wrapping in nv.addGraph allows for '0 timeout render', stores rendered charts in nv.graphs, and may do more in the future... it's NOT required
  var chart;
  var data;
  var legendPosition = "top";

  var randomizeFillOpacity = function() {
      var rand = Math.random(0,1);
      for (var i = 0; i < 100; i++) { // modify sine amplitude
          data[4].values[i].y = Math.sin(i/(5 + rand)) * .4 * rand - .25;
      }
      data[4].fillOpacity = rand;
      chart.update();
  };

  var toggleLegend = function() {
      if (legendPosition == "top") {
          legendPosition = "bottom";
      } else {
          legendPosition = "top";
      }
      chart.legendPosition(legendPosition);
      chart.update();
  };

  nv.addGraph(function() {
      chart = nv.models.lineChart()
          .options({
              duration: 300,
              useInteractiveGuideline: true
          })
      ;

      // chart sub-models (ie. xAxis, yAxis, etc) when accessed directly, return themselves, not the parent chart, so need to chain separately
      chart.xAxis
          .axisLabel("Time (s)")
          .tickFormat(d3.format(',.1f'))
          .staggerLabels(true)
      ;

      chart.yAxis
          .axisLabel('Voltage (v)')
          .tickFormat(function(d) {
              if (d == null) {
                  return 'N/A';
              }
              return d3.format(',.2f')(d);
          })
      ;

      data = sinAndCos();

      d3.select('#chart1').append('svg')
          .datum(data)
          .call(chart);

      nv.utils.windowResize(chart.update);

      return chart;
  });

  function sinAndCos() {
      var sin = [],
          sin2 = [],
          cos = [],
          rand = [],
          rand2 = []
          ;

      for (var i = 0; i < 100; i++) {
          sin.push({x: i, y: i % 10 == 5 ? null : Math.sin(i/10) }); //the nulls are to show how defined works
          sin2.push({x: i, y: Math.sin(i/5) * 0.4 - 0.25});
          cos.push({x: i, y: .5 * Math.cos(i/10)});
          rand.push({x:i, y: Math.random() / 10});
          rand2.push({x: i, y: Math.cos(i/10) + Math.random() / 10 })
      }

      return [
          {
              area: true,
              values: sin,
              key: "Sine Wave",
              color: "#ff7f0e",
              strokeWidth: 4,
              classed: 'dashed'
          },
          {
              values: cos,
              key: "Cosine Wave",
              color: "#2ca02c"
          },
          {
              values: rand,
              key: "Random Points",
              color: "#2222ff"
          },
          {
              values: rand2,
              key: "Random Cosine",
              color: "#667711",
              strokeWidth: 3.5
          },
          {
              area: true,
              values: sin2,
              key: "Fill opacity",
              color: "#EF9CFB",
              fillOpacity: .1
          }
      ];
  }

}])
