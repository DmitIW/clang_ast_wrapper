sudo apt-get update;
sudo apt-get install -y libclang-dev;
pip install -r ./requirements.txt;
dpkg -L $(dpkg --get-selections | grep libclang-) | grep libclang.so