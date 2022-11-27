import curses
sfrom random import randint
#setup windows
curses.initscr()
win=curses.newwin(20,60,0,0)#y,x
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(0)#-1

#sarpele si marul
snake=[(4,10),(4,8),(4,9)]
food=(10,20)
win.addch(food[0],food[1],'@')
#logica jocului
score=0


ESC=27
key=curses.KEY_RIGHT
while key!=ESC:
    win.addstr(0,2,'score '+str(score)+' ')
    win.timeout(150-(len(snake))//5+len(snake)//10%120)#mareste viteza sarpelui


    prev_key=key
    event=win.getch()
    key=event if event!=-1 else prev_key
    if key not in [curses.KEY_LEFT,curses.KEY_RIGHT,curses.KEY_UP,curses.KEY_DOWN,ESC]:
        key=prev_key
    #calculam coordonatele urmatoare ale sarpelui
    y=snake[0][0]
    x=snake[0][1]
    if key == curses.KEY_DOWN:
        y+=1
    if key == curses.KEY_UP:
        y-=1
    if key == curses.KEY_LEFT:
        x-=1
    if key == curses.KEY_RIGHT:
        x+=1
    snake.insert(0,(y,x))    
    #verificam daca a lovit peretii
    if y==0:break
    if y==19:break
    if x==0:break
    if x==59:break
    #daca sarpele se loveste de el insusi
    if snake[0] in snake[1:]:break

    if snake[0]==food:
        #mananca mancarea
        score+=1
        food=()
        while food==():
            food=(randint(1,18),randint(1,58))
            if food in snake:
                food=()
        win.addch(food[0],food[1],'@')
    else:
        #misca sarpele
        last=snake.pop()
        win.addch(last[0],last[1],' ')
   
    win.addch(snake[0][0],snake[0][1],'*')

curses.endwin()
print(f"Scorul Final={score}")
