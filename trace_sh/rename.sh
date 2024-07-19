#!/bin/bash
#rename
xdotool key ctrl+shift+s
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
echo "finish rename"
