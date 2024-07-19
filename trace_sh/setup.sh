#!/bin/bash
#打开open office这个软件
# openoffice4
sleep 1
#进入ppt界面
for i in {1..2}; do
	xdotool key Down
	sleep 0.5
done
xdotool key Enter
sleep 2
xdotool mousemove 890 547 click 1
sleep 2
xdotool mousemove 643 245 click 1
sleep 2
echo "finish enter"
