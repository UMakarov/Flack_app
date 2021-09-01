set token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MiwiZXhwIjoxNjMwNDE0MzY4fQ.DWg-dyHqR4vccFL6Df-Lxs2nGH0QLalDXHfoYgEvFzE
set item_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzZW5kZXJfaWQiOjEsInVzZXJfaWQiOiIyIiwiaXRlbV9pZCI6IjQifQ.5Gc-6J6wThladYoaIydPIog-U9sBPuUr-tCtR_gyUIw

curl -i -H "Content-Type: application/json" -X POST -d "{"""token""":"""%token%""","""item_token""":"""%item_token%"""}" http://localhost:5000//api/receive

pause