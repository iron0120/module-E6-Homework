\\\\\\At ChatBoard_dir directory, start and adjust virtual environment
```bash
python -m venv venv
venvCB\scripts\activate
cd .\ChatBoard\ 
pip install -r requirements.txt
```

Mark ChatBoard directory as Sources root

Create superuser
```
python manage.py createsuperuser
``` 

Start server
```bash
python manage.py runserver
```

Main page works at url http://127.0.0.1:8000/ - local host that server advises you at start message

