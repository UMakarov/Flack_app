curl -i -H "Content-Type: application/json" -X POST -d "{"""name""":"""John""","""password""":"""1234"""}" http://localhost:5000/api/register

curl -i -H "Content-Type: application/json" -X POST -d "{"""name""":"""Nick""","""password""":"""4321"""}" http://localhost:5000/api/register

curl -i -H "Content-Type: application/json" -X POST -d "{"""name""":"""Mike""","""password""":"""2345"""}" http://localhost:5000/api/register

curl -i http://localhost:5000/api/users

pause