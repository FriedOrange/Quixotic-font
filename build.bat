@rem build OpenType fonts
@cd source
python %USERPROFILE%\AppData\Local\Programs\Python\Python310\Scripts\gftools-builder.py config.yaml
@cd ..

@rem patch in additional name table entries
for %%f in (source\patch\*.ttx) do (
	ttx -o fonts\ttf\%%~nf.ttf -m fonts\ttf\%%~nf.ttf %%f
	ttx -o fonts\webfonts\%%~nf.woff2 -m fonts\webfonts\%%~nf.woff2 %%f
)

@rem generate proof documents
@cd fonts\ttf
set PYTHONUTF8=1
python %USERPROFILE%\AppData\Local\Programs\Python\Python310\Scripts\gftools-gen-html.py proof -o ..\proof QuixoticFourteen-Regular.ttf QuixoticSeven-Bold.ttf QuixoticSeven-Light.ttf QuixoticSeven-Medium.ttf QuixoticSeven-Regular.ttf QuixoticSeven-Semibold.ttf QuixoticSixteen-Regular.ttf QuixoticFourteen-Italic.ttf QuixoticSeven-BoldItalic.ttf QuixoticSeven-LightItalic.ttf QuixoticSeven-MediumItalic.ttf QuixoticSeven-Italic.ttf QuixoticSeven-SemiboldItalic.ttf QuixoticSixteen-Italic.ttf
@cd ..\..