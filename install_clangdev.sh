sudo apt-get update;
sudo apt-get install -y libclang-dev;
pip install -r ./clangast/requirements.txt;
dpkg -L $(dpkg --get-selections | grep libclang-) | grep libclang.so > clangast/path_to_so.txt