# ABC

## 1. Packages:
https://docs.python.org/3/tutorial/modules.html#packages
- ech folder contain an empty `__init__.py` file
- root dir should be included in PYTHONPATH
- Example:<br>
  - Create `__init__.py` in "sound", "effect" folders
  
  - Add parent dir of "sound" folder to PYTHONPATH
  
  - Import echo.py file:<br>
    - `import sound.effects.echo`<br>
    - usage: `sound.effects.echo.echofilter()`<br>
  
  - Import echo.py file:<br>  
    - `from sound.effects import echo`<br>
    - usage: `echo.echofilter()`<br>
    
  - Import function echofilter:<br>
    - `from sound.effects.echo import echofilter`<br>
    - usage: echofilter()
