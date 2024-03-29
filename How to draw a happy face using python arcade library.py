import arcade
#specify the parameters
w=600
h=600
t="Happy face"
#Open the window.Set the window title and dimensions
arcade.open_window(w,h,t)
#Set the background color
arcade.set_background_color(arcade.color.BLACK)
#start render process
arcade.start_render()
#Draw the face
x=300
y=300
r=200
arcade.draw_circle_filled(x,y,r,arcade.color.YELLOW)
#Draw the right eye
x=370
y=350
r=20
arcade.draw_circle_filled(x,y,r,arcade.color.BLACK)
#Draw left eye
x=230
y=350
r=20
arcade.draw_circle_filled(x,y,r,arcade.color.BLACK)
#Draw nose
x=415
y=300
w=120
h=120
s=180
e=190
arcade.draw_arc_filled(x,y,w,h,arcade.color.BLACK,s,e,20)
#Draw the smile
x=300
y=250
width=120
height=100
start_angle=190
end_angle=350
arcade.draw_arc_outline(x,y,width,height,arcade.color.BLACK,start_angle,end_angle,30)
#finish drawing
arcade.finish_render()
