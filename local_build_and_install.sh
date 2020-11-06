rm -f dist/*;
python setup.py sdist;
pip install dist/clangast*