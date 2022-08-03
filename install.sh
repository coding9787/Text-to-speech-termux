echo "Updating system....."
apt update -y
apt upgrade -y
echo "Updating pakages......"
pkg update -y
pkg upgrade -y
echo "Install python......."
pkg install python -y
echo "Install mpv & gtts modules........"
pip install mpv
pip install gtts
echo "Starting Text To Speech Programe........"
python tts1.py
