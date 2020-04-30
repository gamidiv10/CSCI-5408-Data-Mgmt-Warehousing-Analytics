const express = require('express');
const caseStudyApplication = express();
const path = require('path');
const router = express.Router();
var mysql = require('mysql');
var bodyParser = require('body-parser');
var startTime,endTime;

router.get('/',function(req,res){
  res.sendFile(path.join(__dirname+'/CaseStudy.html'));
});

caseStudyApplication.use(bodyParser.urlencoded({ extended: true })); 
caseStudyApplication.use('/', router);
caseStudyApplication.listen(8080);
console.log('Running at Port 8080');
caseStudyApplication.post('/', (req, res) => {

  var databaseSelected = req.body.Db;
  if(databaseSelected == "MySQL")
  {
  var mySqlConnection = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "vamsigamidi",
  database: "mydb"
  });
mySqlConnection.connect(function(err) {
  if (err) throw err;
  startTime = Date.now();
  mySqlConnection.query(`SELECT * FROM job_statistics left outer join geo g on g.geo = job_statistics.geo left outer join uom on uom.uom_id = job_statistics.uom_id 
  left outer join scalar_factor on scalar_factor.scalar_id = job_statistics.scalar_id
  where job_statistics.geo = "${req.body.geo}"`, (err, result, fields) =>{
    if (err) throw err;
    endTime = Date.now();
    //let data = JSON.stringify(result);
    res.writeHeader(200, {"Content-Type": "text/html"});
    res.write(`<h1><b>MySQL</b><h1>`)
    res.write(`<h2><b> Time Taken : ${(endTime-startTime)/1000} Seconds </b><h2>`);
    res.write(`<style>
    h1, h2{
      font-family:verdana;
      text-align:center
    }
    table, th, td {
      border: 1px solid black;
      border-collapse: collapse
    }
    th, td {
      padding: 15px
    }
    th, td {
      text-align: left
    }
    table tr:nth-child(even) {
      background-color: #eee
    }
    table tr:nth-child(odd) {
     background-color: #fff
    }
    table th {
      background-color: black;
      color: white
    }
    </style>
    <table><th> Id </th> <th> Location </th> <th> DGUID </th> <th> REF_DATE </th>
      <th> Job vacancy statistics </th> <th> NAICS  </th> <th> UOM </th> <th> UOM_ID </th>  <th> Scalar_Factor </th> <th> SCALAR_ID </th>
     <th> Vector </th> <th> Coordinate </th> <th> Value </th> <th> Status </th> <th> Decimals </th>`);
        result.forEach( (geo) => {
            res.write(`<tr><td> ${geo.Id} </td>    <td> ${geo.GEO} </td>  <td> ${geo.DGUID} </td>  <td> ${geo.REF_DATE} </td>
             <td> ${geo.job_vacancy_statistics} </td>   <td> ${geo.NAICS} </td> <td> ${geo.UOM} </td> 
            <td> ${geo.UOM_ID} </td>  <td> ${geo.Scalar_Factor} </td>    <td> ${geo.SCALAR_ID} </td>      <td> ${geo.VECTOR} </td>  
             <td> ${geo.COORDINATE} </td>   <td> ${geo.VALUE} </td>     <td> ${geo.STATUS} </td>    <td> ${geo.DECIMALS} </td>
            
            </tr>`);
        });
        res.write(`</table>`);
        res.end();
  
  });

});

}

  else
  {
    
var MongoClient = require('mongodb').MongoClient;
var mongoURL = "mongodb://localhost:27017/";

MongoClient.connect(mongoURL,{ useUnifiedTopology: true, useNewUrlParser: true }, function(err, mongoDb) {
  if (err) throw err;
  var databaseObject = mongoDb.db("CaseStudy");
  startTime = Date.now();
  databaseObject.collection("Data").find({GEO: { $eq: `${req.body.geo}` }}).toArray(function(err, result) {
    if (err) throw err;
    endTime = Date.now();
    res.writeHeader(200, {"Content-Type": "text/html"});
    res.write(`<h1><b>MongoDb</b><h1>`)
    res.write(`<h2><b> Time Taken : ${(endTime-startTime)/1000} Seconds </b><h2>`)
    res.write(`<style>
    h1,h2{
      font-family:verdana;
      text-align:center
    }
    table, th, td {
      border: 1px solid black;
      border-collapse: collapse
    }
    th, td {
      padding: 15px
    }
    th {
      text-align: left
    }
    table tr:nth-child(even) {
      background-color: #eee
    }
    table tr:nth-child(odd) {
     background-color: #fff
    }
    table th {
      background-color: black;
      color: white
    }
    </style><table><th> Location </th>  <th> REF_DATE </th> <th> DGUID </th> 
     <th> Job vacancy statistics </th> <th> NAICS  </th> <th> UOM </th>  <th> UOM_ID </th>  <th> Scalar_Factor </th> <th> SCALAR_ID </th>
     <th> Vector </th> <th> Coordinate </th> <th> Value </th> <th> Status </th> <th> Decimals </th>`)
        result.forEach( (geo) => {
            res.write(`<tr><td> ${geo.GEO} </td>    <td> ${geo.REF_DATE} </td>
             <td> ${geo.DGUID} </td>   <td> ${geo.Job_vacancy_statistics} </td>   <td> ${geo.NAICS} </td>
            <td> ${geo.UOM} </td>    <td> ${geo.UOM_ID} </td>    <td> ${geo.SCALAR_FACTOR} </td>  
             <td> ${geo.SCALAR_ID} </td>      <td> ${geo.VECTOR} </td>   <td> ${geo.COORDINATE} </td>   
             <td> ${geo.VALUE} </td>     <td> ${geo.STATUS} </td>    <td> ${geo.DECIMALS} </td>
            </tr>`);
        });
        res.write(`</table>`);
        res.end();
    mongoDb.close();
  });
});
  }
});
