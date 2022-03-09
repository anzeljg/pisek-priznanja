call .\venv\Scripts\activate.bat
::  Pokličemo priznanja.py in dodamo argument 'dist',
::  ki pove, v kateri podmapi so zunanje datoteke ...
python .\priznanja.py dist
pause
call .\venv\Scripts\deactivate.bat
