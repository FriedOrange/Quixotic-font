@REM mkdir fonts
@REM cd fonts
@REM fontmake ..\source\QuixoticSeven.designspace -o variable
@REM fontmake ..\source\QuixoticSeven.designspace -i
@REM cd ..

@cd source
python %USERPROFILE%\AppData\Local\Programs\Python\Python310\Scripts\gftools-builder.py config.yaml
@cd ..

@cd fonts\ttf
set PYTHONUTF8=1
python %USERPROFILE%\AppData\Local\Programs\Python\Python310\Scripts\gftools-gen-html.py proof -o ..\proof QuixoticFourteen.ttf QuixoticSeven-Bold.ttf QuixoticSeven-Light.ttf QuixoticSeven-Medium.ttf QuixoticSeven-Regular.ttf QuixoticSeven-Semibold.ttf QuixoticSixteen.ttf
@cd ..\..