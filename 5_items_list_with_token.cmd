set token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNjMwNDExMTI3fQ.IQMEghY0so2os2pR3InTI5WSjuhYvxE4_ZM7oFOgie8

curl -i -H "Content-Type: application/json" -X POST -d "{"""token""":"""%token%"""}" http://localhost:5000/api/items

pause