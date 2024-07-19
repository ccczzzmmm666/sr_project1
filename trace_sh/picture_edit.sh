#!/bin/bash
#增加插入图片的功能
xdotool mousemove 311 253 click 1
sleep 2
xdotool mousemove 113 71 click 1
sleep 2
xdotool mousemove 141 99
for i in {1..13}; do
	xdotool key Down
	sleep 0.5
done
sleep 2
xdotool key Right
sleep 2
xdotool key Enter
sleep 2
xdotool mousemove 536 482 click 1
sleep 1
xdotool key ctrl+a
sleep 1
xdotool type "/home/czm/Downloads/11677.jpg"
sleep 1
xdotool key Enter
sleep 1
#实现图片放缩
xdotool mousemove 983 629
sleep 1
xdotool mousedown 1
sleep 1
xdotool mousemove 579 424
sleep 1
xdotool mouseup 1
sleep 1
xdotool key ctrl+z
sleep 1
xdotool key ctrl+y
sleep 1
#实现图片位置的移动
xdotool mousemove 535 388 click 1
sleep 1
xdotool mousedown 1
sleep 1
xdotool mousemove 453 636
sleep 3
xdotool mouseup 1
sleep 1
echo "finish picture edit"
