#!/bin/bash
#打开open office这个软件
# openoffice4
echo "Current time: $(date '+%Y-%m-%d %H:%M:%S')"
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
#保存文件
xdotool mousemove 311 253 click 1
sleep 2
xdotool key ctrl+s
sleep 2
xdotool mousemove 820 607 click 1
sleep 2
xdotool key ctrl+a
sleep 2
xdotool type "example"
sleep 2
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
xdotool key ctrl+s
sleep 2
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
xdotool key ctrl+shift+s
echo "save Current time: $(date '+%Y-%m-%d %H:%M:%S')"
sleep 2
xdotool mousemove 794 602 click 1
sleep 1
xdotool key ctrl+a
sleep 1
xdotool key Delete
sleep 1
xdotool type "new_example"
sleep 3
xdotool key Enter
sleep 1
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
sleep 1
xdotool key F5
sleep 1
xdotool key Enter
sleep 1
xdotool key Enter
sleep 1
xdotool key ctrl+shift+s
echo "save Current time: $(date '+%Y-%m-%d %H:%M:%S')"
sleep 1
xdotool mousemove 1191 481
sleep 1
xdotool mousedown 1
sleep 1
xdotool mousemove 1192 546
sleep 1
xdotool mouseup 1
sleep 1
xdotool mousemove 751 529 click 3
sleep 1
xdotool mousemove 788 537 click 1
sleep 1
xdotool mousemove 531 447 click 1
sleep 1
xdotool mousemove 764 544 click 3
sleep 1
xdotool mousemove 813 551 click 1
sleep 1
xdotool mousemove 525 446 click 1
sleep 1
xdotool mousemove 1200 368 click 1
sleep 1
xdotool mousemove 1346 46 click 1
sleep 1
xdotool mousemove 693 436 click 1
