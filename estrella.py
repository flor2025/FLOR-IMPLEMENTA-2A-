from turtle import *
color('blue', 'pink')
begin_fill()
while True:
    forward(250)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
done()
