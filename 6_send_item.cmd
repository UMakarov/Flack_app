set item_id=4
set user_id=2

set token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNjMwNDE0Mjc4fQ.xtBMGQj2yEcgMml1Xg-ujsmsFuTKLGaa8DmIeproxiQ

curl -i -H "Content-Type: application/json" -X POST -d "{"""item_id""":"""%item_id%""","""user_id""":"""%user_id%""","""token""":"""%token%"""}" http://localhost:5000/api/send

pause