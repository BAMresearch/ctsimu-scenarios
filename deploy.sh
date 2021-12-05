rm -R docs
cp -R build/html .
mv html docs
touch docs/.nojekyll