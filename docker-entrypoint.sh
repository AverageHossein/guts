flask db init
flask db migrate -m "Initial migration"
flask db upgrade
gunicorn -w 4 main:app -b 0.0.0.0:8000
