rmdir /S /Q docs
copy build/latex/ctsimu-scenario*.pdf build/html/
xcopy /E /I /H build\html .\docs
echo. > docs\.nojekyll