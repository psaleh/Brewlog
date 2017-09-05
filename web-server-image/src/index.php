<?php
 $con = mysqli_connect('brewlog_db_1','brewlog','brewlog','brewlog');
?>
<!DOCTYPE HTML>
<html>
<head>
 <meta charset="utf-8">
 <title>
Bomb Shelter Brewery Monitor
 </title>
 <script type="text/javascript" src="https://www.google.com/jsapi"></script>
 <script type="text/javascript">
 google.load("visualization", "1", {packages:["corechart"]});
 google.setOnLoadCallback(drawChart);
 google.setOnLoadCallback(drawChart2);
 function drawChart() {
 var data = google.visualization.arrayToDataTable([

 ['Date', 'Temperature'],
 <?php 
 $query = "SELECT time, temp FROM testtable ORDER BY time";

 $exec = mysqli_query($con,$query);
 while($row = mysqli_fetch_array($exec)){

 echo "['".$row['time']."',".$row['temp']."],";
 }
 ?>
 
 ]);

 var options = {
 title: 'Fermentation Temperature'
 };
 var chart = new google.visualization.LineChart(document.getElementById("temp_chart"));
 chart.draw(data, options);
 }
 function drawChart2() {
 var data = google.visualization.arrayToDataTable([

 ['Date', 'SG'],
 <?php 
 $query = "SELECT time, sg FROM testtable ORDER BY time";

 $exec = mysqli_query($con,$query);
 while($row = mysqli_fetch_array($exec)){

 echo "['".$row['time']."',".$row['sg']."],";
 }
 ?>
 
 ]);

 var options = {
 title: 'Specific Gravity'
 };
 var chart = new google.visualization.LineChart(document.getElementById("sg_chart"));
 chart.draw(data, options);
 }
 </script>
</head>
<body>
 <h3>Temperature</h3>
 <div id="temp_chart" style="width: 900px; height: 500px;"></div>
 <h3>Specific Gravity</h3>
 <div id="sg_chart" style="width: 900px; height: 500px;"></div>
</body>
</html>
