# #import datetime as dt
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# import psutil

# # Create figure for plotting
# #figurezize is used to control the size of the window
# fig1 = plt.figure(figsize=(5,5), facecolor='#DEDEDE')
# #This is to create the size of the plot (height, width, postion)
# ax = fig1.add_subplot(1, 1, 1)
# xs = []
# ys = []


# # This function is called periodically from FuncAnimation
# def animate(i, xs, ys):

#     #Grabing the cpu precent at an interval (this is where we would grab data from sensor)
#     cpu_percentage = psutil.cpu_percent(interval=1)

#     # Add y to lists
#     ys.append(cpu_percentage)

#     # Limit x and y lists to 20 items
#     xs = xs[-20:]
#     ys = ys[-20:]

#     # Draw x and y lists
#     plt.cla()
#     #change the the letter in'' to change color
#     plt.plot(ys, 'b')

#     # Format plot
#     #this control the angle of the x-units and direction
#     plt.xticks(rotation=30, ha='right')

#     plt.title('CPU Percentage over Time')
#     plt.ylabel('percentage ')

#     #this make the aspect ratio remain 1:1
#     plt.tight_layout()

# # Set up plot to call animate() function periodically
# ani = animation.FuncAnimation(fig1, animate, fargs=(xs, ys), interval=1000)
# plt.show()
