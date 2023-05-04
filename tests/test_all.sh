echo "Start xvfb"
Xvfb :1 -screen 0 1024x768x16 &> xvfb.log  &

DISPLAY=:1.0
export DISPLAY

echo "Run tests"

annotate-output "+%D %H:%M:%S"  pytest --pylint --pylint-rcfile=./tests/pylintrc --black  2>&1 | tee /proc/1/fd/1

rcode=$?
echo "Stop xvfb"
kill $(pgrep -f Xvfb)
exit ${rcode}
