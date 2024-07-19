#!/bin/bash
# 增加文本框，加入文本
xdotool mousemove 142 726 click --repeat 2 1
sleep 1
xdotool mousemove 348 275
xdotool mousedown 1
sleep 1
xdotool mousemove 858 356
sleep 1
xdotool mouseup 1
sleep 1
xdotool type "We Bare Bears is an American animated sitcom created by Daniel Chong for Cartoon Network. The show follows three bear brothers, Grizzly, Panda, and Ice Bear, and their awkward attempts at integrating with the human world in the San Francisco Bay Area."
sleep 7
#修改文本
xdotool mousemove 590 321 click 1
sleep 1
xdotool key ctrl+End
sleep 1
xdotool type "The series was based on Chong's webcomic The Three Bare Bears, and the pilot episode made its world premiere at the KLIK! Amsterdam Animation Festival, where it won in the "Young Amsterdam Audience" category."
sleep 7
#删除所有的文本
xdotool key ctrl+a
sleep 1
xdotool key Delete
sleep 1
#从别的地方读取文本并拷贝进这个文件
xdotool key super
sleep 1
xdotool mousemove 943 402 click 1
sleep 1
xdotool mousemove 818 348 click 1
sleep 1
xdotool key Ctrl+End
sleep 1
xdotool key ctrl+a
sleep 1
xdotool key ctrl+c
sleep 2
xdotool mousemove 252 311 click 1
sleep 1
xdotool mousemove 142 726 click --repeat 2 1
sleep 1
xdotool mousemove 348 275
xdotool mousedown 1
sleep 1
xdotool mousemove 858 356
sleep 1
xdotool mouseup 1
xdotool key ctrl+v
sleep 3
xdotool key ctrl+a
sleep 1
xdotool mousemove 213 125 click 1
sleep 1
# 修改字号
for i in 1 2 3,4; do
	xdotool click 5
	sleep 0.5
done
xdotool key Enter
echo "finish text edir"
