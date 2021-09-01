set user=John:1234
rem set user=Nick:4321
rem set user=Mike:2345
curl -u%user% http://localhost:5000/api/login

@echo Copy this token into 3,4,5,6 cmd files
pause