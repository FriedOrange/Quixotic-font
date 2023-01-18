set PYTHONUTF8=1
mkdir fonts\fontbakery
fontbakery check-googlefonts -C -l PASS --html fonts\fontbakery\fontbakery-report.html fonts\ttf\*.ttf > fonts\fontbakery\test.log