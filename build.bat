@REM mkdir fonts
@REM cd fonts
@REM fontmake ..\source\QuixoticSeven.designspace -o variable
@REM fontmake ..\source\QuixoticSeven.designspace -i
@REM cd ..

@cd source
python %USERPROFILE%\AppData\Local\Programs\Python\Python310\Scripts\gftools-builder.py config.yaml
@cd ..