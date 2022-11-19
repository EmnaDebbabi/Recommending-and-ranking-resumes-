"use strict";$(document).ready(function(){nv.addGraph(function(){var chart=nv.models.lineChart().margin({top:50}).margin({left:100}).useInteractiveGuideline(true).showLegend(true).showYAxis(true).showXAxis(true);chart.xAxis.axisLabel('Time (ms)').tickFormat(d3.format(',r'));chart.yAxis.axisLabel('Voltage (v)').tickFormat(d3.format('.02f'));var myData=sinAndCos();d3.select('#linechart').append('svg').datum(myData).call(chart);nv.utils.windowResize(function(){chart.update()});return chart;});function sinAndCos(){var sin=[],sin2=[],cos=[];for(var i=0;i<100;i++){sin.pu"use strict";$(document).ready(function(){nv.addGraph(function(){var chart=nv.models.lineChart().margin({top:50}).margin({left:100}).useInteractiveGuideline(true).showLegend(true).showYAxis(true).showXAxis(true);chart.xAxis.axisLabel('Time (ms)').tickFormat(d3.format(',r'));chart.yAxis.axisLabel('Voltage (v)').tickFormat(d3.format('.02f'));var myData=sinAndCos();d3.select('#linechart').append('svg').datum(myData).call(chart);nv.utils.windowResize(function(){chart.update()});return chart;});function sinAndCos(){var sin=[],sin2=[],cos=[];for(var i=0;i<100;i++){sin.push({x:i,y:Math.sin(i/10)});sin2.push({x:i,y:Math.sin(i/10)*0.25+0.5});cos.push({x:i,y:.5*Math.cos(i/10)});}
return[{values:sin,key:'Sine Wave',color:'#4C5667'},{values:cos,key:'Cosine Wave',color:'#5FBEAA'},{values:sin2,key:'Another sine wave',color:'#FF9F55',area:true}];}
nv.addGraph(function(){var chart=nv.models.discreteBarChart().x(function(d){return d.label}).y(function(d){return d.value}).staggerLabels(true).showValues(true);d3.select('#barchart').append('svg').datum(barData()).call(chart);nv.utils.windowResize(chart.update);return chart;});function barData(){return[{key:"Cumulative Return",values:[{"label":"A","value":-29.765957771107,"color":"#FF9F55"},{"label":"B","value":10,"color":"#FEC811"},{"label":"C","value":32.807804682612,"color":"#4C5667"},{"label":"D","value":196.45946739256,"color":"#01C0C8"},{"label":"E","value":0.25434030906893,"color":"#FF0084"},{"label":"F","value":-98.079782601442,"color":"#007BB6"},{"label":"G","value":-13.925743130903,"color":"#3b5998"},{"label":"H","value":-5.1387322875705,"color":"#B2E0A2"}]}]}
nv.addGraph(function(){var chart=nv.models.scatterChart().showDistX(true).showDistY(true).color(d3.scale.category10().range());chart.xAxis.tickFormat(d3.format('.02f'));chart.yAxis.tickFormat(d3.format('.02f'));var myData=randomData(4,40);d3.select('#scatterchart').append('svg').datum(myData).call(chart);nv.utils.windowResize(chart.update);return chart;});function randomData(groups,points){var data=[],shapes=['circle','cross','triangle-up','triangle-down','diamond','square'],random=d3.random.normal();for(var i=0;i<groups;i++){data.push({key:'Group '+i,values:[]});for(var j=0;j<points;j++){data[i].values.push({x:random(),y:random(),size:Math.random(),shape:(Math.random()>0.95)?shapes[j%6]:"circle"});}}
return data;}
nv.addGraph(function(){var chart=nv.models.multiBarChart().reduceXTicks(true).rotateLabels(0).showControls(true).groupSpacing(0.1);chart.xAxis.tickFormat(d3.format(',f'));chart.yAxis.tickFormat(d3.format(',.1f'));d3.select('#stackedchart').append('svg').datum(stackedData()).call(chart);nv.utils.windowResize(chart.update);return chart;});function stackedData(){return stream_layers(3,10+Math.random()*100,.1).map(function(data,i){return{key:'Stream #'+i,values:data};});}
nv.addGraph(function(){var chart=nv.models.pieChart().x(function(d){return d.label}).y(function(d){return d.value}).showLabels(true);d3.select("#piechart").append('svg').datum(pieData()).transition().duration(350).call(chart);nv.utils.windowResize(chart.update);return chart;});nv.addGraph(function(){var chart=nv.models.pieChart().x(function(d){return d.label}).y(function(d){return d.value}).showLabels(true).labelThreshold(.05).labelType("percent").donut(true).donutRatio(0.35);d3.select("#donutchart").append('svg').datum(pieData()).transition().duration(350).call(chart);nv.utils.windowResize(chart.update);return chart;});function pieData(){return[{"label":"One","value":29.765957771107,"color":"#FB9678"},{"label":"Two","value":0,"color":"#FF9F55"},{"label":"Three","value":32.807804682612,"color":"#01C0C8"},{"label":"Four","value":196.45946739256,"color":"#00C292"},{"label":"Five","value":0.19434030906893,"color":"#4F5467"},{"label":"Six","value":98.079782601442,"color":"#4F5467"},{"label":"Seven","value":13.925743130903,"color":"#000000"},{"label":"Eight","value":5.1387322875705,"color":"#CB2027"}];}});