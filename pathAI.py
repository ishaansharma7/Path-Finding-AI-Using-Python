from tkinter import *
import backend
def god():
    root = Tk()
    root.iconbitmap('Logo.ico')
    root.title('PathAI')
    root.geometry('800x780')
    #root.resizable(width=FALSE, height=FALSE)
    count = 0
    button_list = []
                                                        # root is divide into two parts 
    frame_up = LabelFrame(root, text='options')         # upper part containing options for chossing starting, end point etc..
    frame_down = LabelFrame(root, text='path')          # contains the grid of numbered buttons from 0 to 399
    frame_up.pack()
    frame_down.pack()
    global supply_mode                                  # choose between start point, obstacles and destination point
    supply_mode = 0
    global src
    src = 0
    global obstacle_list                                # will contains the obstacles entered by user by clicking numbered buttons
    obstacle_list = []
    global dest                                         # stores the final destination point enterd by user
    dest = 1000

    def button_mode(mode):
        global supply_mode
        supply_mode = mode
        print(supply_mode)

    def button_click(but_no):
        #print(but_no)
        global supply_mode
        if supply_mode == 1:                                # for starting point
            button_list[but_no].config(bg='#ffe525')
            global src
            src = but_no
            start_button['state'] = DISABLED
            supply_mode = 0
        if supply_mode == 2:                                # for obstacles
            button_list[but_no].config(bg='#b4b4b4')
            global obstacle_list
            obstacle_list.append(but_no)
            print(obstacle_list)
        if supply_mode == 3:                                # for destination
            button_list[but_no].config(bg='#7dcf21')
            global dest
            dest=but_no
            destination_button['state'] = DISABLED
            supply_mode = 0


    start_button = Button(frame_up, text='select start point', command=lambda: button_mode(1))
    obstacle_button = Button(frame_up, text='select obstacles', command=lambda: button_mode(2))
    destination_button = Button(frame_up, text='select destination', command=lambda: button_mode(3))


    start_button.grid(row=0, column=1, sticky="ew", padx=10, pady=5)
    obstacle_button.grid(row=0, column=2, sticky="ew", padx=10, pady=5)
    destination_button.grid(row=0, column=3, sticky="ew", padx=10, pady=5)


    for i in range(20):
        for j in range(20):
            button_list.append(Button(frame_down, text=f'{count}', padx=5, pady=5, command=lambda x=count: button_click(x)))
            button_list[count].grid(row=i, column=j, sticky="ew")
            count += 1

    def solution():
        parent = backend.backened(src, obstacle_list, dest)
        for value in parent:
            button_list[value].config(bg='#00c5ff')         # path color
        button_list[src].config(bg='#ffe525')


    go_button = Button(frame_up, text='go', command=solution)
    go_button.grid(row=0, column=4, padx=10, pady=5)

    def restart():
        root.destroy()
        god()
        

    restart_button = Button(frame_up, text='restart', command=restart)
    restart_button.grid(row=0, column=5, padx=10, pady=5)

    def level_tut():
        already_generated_obstacle = [40, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 41, 61, 81, 101, 121, 141, 161, 181, 182, 201, 221, 241, 261, 281, 301, 321, 341, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 339, 338, 318, 298, 278, 258, 238, 239, 219, 199, 179, 159, 139, 119, 99, 79, 59, 39, 43, 63, 83, 103, 45, 65, 85, 123, 105, 143, 144, 145, 146, 186, 185, 184, 183, 122, 106, 108, 88, 68, 48, 26, 90, 110, 49, 50, 51, 52, 53, 91, 92, 93, 95, 115, 135, 155, 175, 195, 215, 235, 255, 172, 212, 152, 151, 150, 149, 148, 187, 189, 188, 169, 230, 231, 232, 229, 228, 227, 54, 55, 56, 77, 57, 117, 97, 118, 156, 176, 196, 216, 236, 178, 173, 174, 225, 224, 223, 243, 263, 283, 323, 324, 325, 326, 327, 328, 329, 309, 289, 269, 249, 265, 285, 286, 287, 267, 297, 296, 295, 294, 293, 292, 252, 253, 291, 330, 331, 332, 333, 334, 335, 336, 337, 264, 288]
        global obstacle_list
        obstacle_list = already_generated_obstacle
        for every in already_generated_obstacle:
            button_list[every].config(bg='#b4b4b4')

    level_button = Button(frame_up, text='tutorial', command=level_tut)
    level_button.grid(row=0, column=6, padx=10, pady=5)

    mainloop()
god()
