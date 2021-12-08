rm -R docs
make html
make latexpdf
cp build/latex/ctsimu-scenario*.pdf build/html/
cp -R build/html .
mv html docs
touch docs/.nojekyll