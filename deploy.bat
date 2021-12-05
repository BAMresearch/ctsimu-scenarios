rmdir /S /Q docs
xcopy /E /I /H build\html .\docs
echo. > docs\.nojekyll