set token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MiwiZXhwIjoxNjMwNDkxMDkxfQ.AXxqimuLeBndo3fXcr8G-XboVygM_TMXb7GDZdUzzmc
set item_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzZW5kZXJfaWQiOjEsInVzZXJfaWQiOiIyIiwiaXRlbV9pZCI6IjQifQ.5Gc-6J6wThladYoaIydPIog-U9sBPuUr-tCtR_gyUIw

curl -i -H "Content-Type: application/json" -X GET http://localhost:5000//api/receive?token=%token%&item_token=%item_token%

rem curl -i -H "Content-Type: application/json" -X GET http://localhost:5000//api/receive?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MiwiZXhwIjoxNjMwNDkxMDkxfQ.AXxqimuLeBndo3fXcr8G-XboVygM_TMXb7GDZdUzzmc&item_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzZW5kZXJfaWQiOjEsInVzZXJfaWQiOiIyIiwiaXRlbV9pZCI6IjQifQ.5Gc-6J6wThladYoaIydPIog-U9sBPuUr-tCtR_gyUIw

pause

