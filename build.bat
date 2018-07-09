SET file_name="Marvelous-Mechanical-Mouse"

del dist
del build

cd .\%file_name%

pyinstaller ./%file_name%.py

mkdir .\dist\%file_name%\main\var
move dist ..\dist
move build ..\build
del %file_name%.spec