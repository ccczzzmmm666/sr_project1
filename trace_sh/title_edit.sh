#!/bin/bash
#插入修改标题
xdotool type "We Bare Bears"
sleep 2
xdotool key ctrl+a
sleep 2
xdotool mousemove 213 125 click 1
sleep 2
# 修改字号
for i in 1 2 3; do
	xdotool click 5
	sleep 0.5
done
xdotool key Enter
sleep 2
#修改字体
xdotool mousemove 498 245 click 1
sleep 2
xdotool key ctrl+a
sleep 2
xdotool mousemove 103 127 click 1
sleep 2
xdotool key ctrl+a
sleep 2
xdotool key BackSpace
sleep 2
xdotool type "CPMono_v07 Bold"
sleep 2
xdotool key Enter
sleep 2
echo "finish title edit"
