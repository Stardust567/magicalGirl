import pygame,sys,math,time
import easygui 
import pygame.freetype


#游戏设置
pygame.init()
icon = pygame.image.load("3_LI.jpg")
pygame.display.set_icon(icon)
vInfo  = pygame.display.Info()
size = width,height = vInfo.current_w-1000,vInfo.current_h-400

speed = [2,2]
sw = [3,2]
sb = [2,3]
BLACK = 0,0,0
WHITE = 255,255,255
BLUE = 0,0,255
YELLOW = 255,255,0
ORANGE = 255,165,0
RED = 234,48,39
GOLD = 255,251,0
PURPLE = 128,0,128
screen = pygame.display.set_mode(size,pygame.RESIZABLE)
pygame.display.set_caption("魔女之夜")
filename='music\Iceloki - 魔法少女の宿命.mp3'
pygame.mixer.init()
pygame.mixer.music.load(filename)
pygame.mixer.music.play(-1)

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
bw = pygame.image.load("1.png")
bwrect = bw.get_rect()
bb = pygame.image.load("2.png")
bbrect = bb.get_rect()
fps = 300
fclock = pygame.time.Clock()
bgcolor = pygame.Color("black")
still = False
game_active = False
f1 = pygame.freetype.Font("Fonts\方正静蕾体.fon",36)
yes = 0
no =0
num = 0
live = 0
save_you = 0
able = 18
sl = 1
start = time.clock()
triangle_pos = (460,340)
circle_pos = (460,340)


def RGBChannel(a):
    return 0 if a<0 else (255 if a>255 else int(a))

def absadd(x,num):
    return x+num if x>=0 else x-num

def distance(point):
    a = (point[0][0]-point[1][0])*(point[0][0]-point[1][0])
    b = (point[0][1]-point[1][1])*(point[0][1]-point[1][1])
    s = math.sqrt(a+b)
    return s

#Yes = easygui.buttonbox("   和我签订契约 成为魔法少女吧！", image="魔法少女.gif",choices = ['和我一起踏上新的旅程吧!'])

while True:

    uevent = pygame.event.Event(pygame.KEYDOWN,{"unicode":123,"key":pygame.K_SPACE,"mod":pygame.KMOD_ALT})
    
#事件判断
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.display.set_caption("   和我签订契约 成为魔法少女吧！")
            if sl > 0:
                time.sleep(1)
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_a:
                if ballrect.left>300  and able > 0:
                    ballrect.x -= 300
                    able -= 1
            if event.key == pygame.K_d:        
                if ballrect.right + 300 < width and able > 0:
                    ballrect.x += 300
                    able -= 1
            if event.key == pygame.K_w:
                if ballrect.top>300 and able > 0:
                    ballrect.y -= 300
                    able -= 1
            if event.key ==pygame.K_s:
                if ballrect.bottom + 300 <height and able > 0:
                    ballrect.y += 300
                    able -= 1
            
            if event.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0])-1)*int(speed[0]/abs(speed[0]))
            if event.key == pygame.K_RIGHT:
                speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] - 1
            if event.key == pygame.K_UP:
                speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
            if event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1])-1)*int(speed[1]/abs(speed[1]))

            if event.key == pygame.K_ESCAPE:
                pygame.display.set_caption("  和我签订契约 成为魔法少女吧！")
                if sl > 0 :
                    time.sleep(1)
                sys.exit()

        #    print ("[KEYDOWN]:",event.unicode,event.key,event.mod)

        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[0] ==2:
                ballrect = ballrect.move(event.pos[0] - ballrect.left,event.pos[1] - ballrect.top)
                
        #    print ("[MOUSEMOTION]:",event.pos,event.rel,event.buttons)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 2:
                still = False
                ballrect = ballrect.move(event.pos[0] - ballrect.left,event.pos[1] - ballrect.top)
                
        #    print ("[MOUSEBUTTONUP]:",event.pos,event.button)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 2:
                still = True
            if event.button == 3:
                triangle_pos = event.pos
            if event.button == 1:
                circle_pos = event.pos
                
        #   print ("[MOUSEBUTTONDOWN]:",event.pos,event.button)
                
        elif event.type == pygame.VIDEORESIZE:
            size = width,height = event.size[0],event.size[1]
            screen = pygame.display.set_mode(size,pygame.RESIZABLE)
            
#游戏逻辑
    end = time.clock()

    if int(end - start) > 3:
        point = (ballrect.center,bwrect.center)
        if 68< distance(point) <70:
            sw[0] = -sw[0]
            sw[1] = -sw[1]
            yes = yes + 1
            #print(s)
        point = (ballrect.center,bbrect.center)
        if 68< distance(point) <70:
            sb[0] = -sb[0]
            sb[1] = -sb[1]
            no = no + 1
            #print(s)

    if no > yes :
        soul = 0
        dark = no - yes
    elif no < yes:
        soul = yes - no
        dark = 0
    else:
        soul = dark = 0

#胜利条件&结局
    if dark > 10:
        speed[0] = 0
        speed[1] = 0
        screen.fill(WHITE)
        e2 = pygame.image.load("CG\灵魂宝石2.jpg")
        e2rect = e2.get_rect()
        screen.blit(e2,e2rect)
        bad_end2 = f1.render_to(screen,(750,280),"CRAZY AND OVER.BUT AGAIN.",fgcolor = RED,size = 80)
        pygame.display.update()
        pygame.mixer.music.stop()
        pygame.mixer.music.load('music\梶浦由記 - Sis puella magica!.mp3')
        if sl > 0 :
            time.sleep(1)
        pygame.mixer.music.play(-1)
        pygame.display.set_caption("  和我签订契约 成为魔法少女吧！")
        if sl > 0 :
            time.sleep(5)
        yes = no = 0
        speed[0] = speed[1] = 2
        bwrect.x=bbrect.x=bwrect.y=bbrect.y=0
        triangle_pos = circle_pos = (460,340)
        able = 18

    elif soul > 10:
        screen.fill(WHITE)
        e1 = pygame.image.load("CG\灵魂宝石1.jpg")
        e1rect = e1.get_rect()
        screen.blit(e1,e1rect)
        happy_end = f1.render_to(screen,(650,280),"YOU WIN.AND THIS IS YOUR FATE.",fgcolor = PURPLE,size = 80)
        pygame.display.update()
        pygame.mixer.music.stop()
        pygame.mixer.music.load('music\梶浦由記 - another episode.mp3')
        if sl > 0:
            time.sleep(1)
        pygame.mixer.music.play(-1)
        if sl > 0:
            time.sleep(3)
        screen.fill(BLACK)
        pygame.display.update()
        if sl > 0:
            time.sleep(1)
        true_end1 = f1.render_to(screen,(100,280),"你愿意抹去自己在这个世界上的存在",fgcolor = RED,size = 80)
        true_end2 = f1.render_to(screen,(100,380),"去为其他的魔法少女带来希望吗？",fgcolor = RED,size = 80)
        pygame.display.update()
        if save_you == 0:
            if sl > 0:
                time.sleep(4)
            truend2 = pygame.image.load("CG\save.jpg")
            truend2rect = truend2.get_rect()
            screen.blit(truend2,truend2rect)
            pygame.display.update()
            if sl > 0:
                time.sleep(4)
            save_you += 1
            yes = no = 0
            speed[0] = speed[1] = 2
            bwrect.x=bbrect.x=bwrect.y=bbrect.y=0
            triangle_pos = circle_pos = (460,340)
            able = 18
            pygame.mixer.music.stop()
            pygame.mixer.music.load('music\まらしぃ - コネクト.mp3')
            if sl > 0:
                time.sleep(1)
            pygame.mixer.music.play(-1)
        else:
            if sl > 0:
                time.sleep(6)
            Yes_or_No = easygui.buttonbox("认真的再问你一遍，你真的愿意抹去自己的存在只为了给其他的魔法少女带来希望?", image="CG\圆神.gif",choices = ['Yes','No'])
            if sl > 0:
                time.sleep(1)
        
            if Yes_or_No == 'Yes' :
                pygame.display.set_caption("  圆环之理")
                screen.fill(WHITE)
                truend = pygame.image.load("CG\圆环之理.jpg")
                truendrect = truend.get_rect()
                screen.blit(truend,truendrect)
                true_end1 = f1.render_to(screen,(600,130),"TRUE END.",fgcolor = PURPLE,size = 60)
                true_end2 = f1.render_to(screen,(600,230),"你成为了超越这个宇宙的某种概念性的存在。",fgcolor = PURPLE,size = 40)
                true_end3 = f1.render_to(screen,(600,330),"带走了历史上存在过的所有魔法少女所沾染的绝望。",fgcolor = PURPLE,size = 40)
                true_end4 = f1.render_to(screen,(600,430),"你的人生将既无开始，也无结束。",fgcolor = PURPLE,size = 40)
                true_end5 = f1.render_to(screen,(600,530),"曾活在这世上的证明和记忆将不会残留在任何地方。",fgcolor = PURPLE,size = 40)
                pygame.display.update()
                time.sleep(12)
                screen.fill(BLACK)
                will_end1 = f1.render_to(screen,(600,180),"PLEASE DON'T FORGET",fgcolor = WHITE,size = 50)
                will_end2 = f1.render_to(screen,(600,280),"ALWAYS SOMEWHERE",fgcolor = WHITE,size = 50)
                will_end3 = f1.render_to(screen,(600,380),"SOMEONE IS FIGHTING FOR YOU",fgcolor = WHITE,size = 50)
                will_end4 = f1.render_to(screen,(600,480),"AS LONG AS YOU REMEMBER HER",fgcolor = WHITE,size = 50)
                will_end5 = f1.render_to(screen,(600,580),"YOU ARE NOT ALONE",fgcolor = WHITE,size = 50)
                pygame.display.update()
                if sl > 0:
                    time.sleep(16)
                sys.exit()
            else:
                screen.fill(BLACK)
                con_tinue = pygame.image.load("CG\continue.png")
                con_tinuerect = con_tinue.get_rect()
                screen.blit(con_tinue,con_tinuerect)
                con_end1 = f1.render_to(screen,(650,280),"THIS IS AN ENDLESS CIRCLE.",fgcolor = RED,size = 80)
                con_end2 = f1.render_to(screen,(650,380),"CONTINUE?  YES or YES.",fgcolor = RED,size = 80)
                pygame.display.update()

                pygame.mixer.music.stop()
                pygame.mixer.music.load('music\TAMUSIC - “コネクト”の主题による即兴曲 Piano ver.mp3')
                if sl > 0:
                    time.sleep(1)
                pygame.mixer.music.play(-1)
                if sl > 0:
                    time.sleep(6)
                eend = pygame.image.load("CG\end.jpg")
                eendrect = eend.get_rect()
                screen.blit(eend,eendrect)
                pygame.display.update()
                if sl > 0:
                    time.sleep(8)
                yes = no = 0
                speed[0] = speed[1] = 2
                bwrect.x=bbrect.x=bwrect.y=bbrect.y=0
                triangle_pos = circle_pos = (460,340)
                able = 18

#运动条件
    if int(end - start) > 3:
        if bwrect.left<0 or bwrect.right > width:
            sw[0] = -sw[0]
        if bwrect.top<0 or bwrect.bottom > height:
            sw[1] = -sw[1]
        bbrect = bbrect.move(sb[0],sb[1])
        if bbrect.left<0 or bbrect.right > width:
            sb[0] = -sb[0]
        if bbrect.top<0 or bbrect.bottom > height:
            sb[1] = -sb[1]
        bwrect = bwrect.move(sw[0],sw[1])
        
    if pygame.display.get_active() and not still:
            ballrect = ballrect.move(speed[0],speed[1])
            
    if ballrect.left<0 or ballrect.right > width:
        speed[0] = -speed[0]
    #    print (ballrect.left,ballrect.right,width)
    if ballrect.top<0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    #    print (ballrect.top,ballrect.bottom,height)

    screen.fill(bgcolor)
    point = (ballrect.center,circle_pos)
    if 50< distance(point) < 80 :
        speed[0] = -absadd(speed[0],1)
        speed[1] = -absadd(speed[1],1)
        ru = 30
        for i in range(10):
            rcircle1 = pygame.draw.circle(screen,WHITE,circle_pos,ru,1)
            ru += 10
            pygame.display.update()
    elif distance(point) < 50 :
        rcircle1 = pygame.draw.circle(screen,RED,circle_pos,50,1)
        speed[0] = speed[1] = 3
        pygame.display.update()
        rcircle1 = pygame.draw.circle(screen,RED,circle_pos,80,1)
        pygame.display.update()
        rcircle1 = pygame.draw.circle(screen,RED,circle_pos,110,1)
        pygame.display.update()
        frect4 = f1.render_to(screen,(30,280),"加速魔法暴走，务必尽快转移加速点 ! ! !",fgcolor = RED,size = 30)
    point = (ballrect.center,triangle_pos)
    if  distance(point) < 50 :
        speed[0] = 2 if speed[0]>0 else -2
        speed[1] = 2 if speed[1]>0 else -2
        tu = 20
        for i in range(3):
            t1 = (triangle_pos[0],triangle_pos[1]-tu*1.4)
            t2 = (triangle_pos[0]-tu,triangle_pos[1]+tu*0.6)
            t3 = (triangle_pos[0]+tu,triangle_pos[1]+tu*0.6)
            rtriangle = pygame.draw.polygon(screen,PURPLE,[t1,t2,t3],1)
            tu += 10
            pygame.display.update()

#速度条件        
    if abs (speed[0]) >7 or abs (speed[0]) >7 :
        bgcolor = RED
        screen.fill(bgcolor)
        num = num + 1
        str1 = "超速预警 * " + str (num)
        rect_w = f1.render_to(screen,(350,280),str1,fgcolor = YELLOW,size = 80)
        pygame.display.update()
        if sl > 0:
            time.sleep(2)
        speed[0] = 2
        speed[1] = 2
        circle_pos = (460,340)
        ballrect.x = 0
        ballrect.y = 0
        if num == 3:
            screen.fill(WHITE)
            e3 = pygame.image.load("CG\灵魂宝石3.jpg")
            e3rect = e3.get_rect()
            screen.blit(e3,e3rect)
            bad_end3 = f1.render_to(screen,(750,280),"DEAD AND OVER.BUT ALIVE.",fgcolor = RED,size = 80)
            pygame.display.update()
            pygame.mixer.music.stop()
            pygame.mixer.music.load('music\梶浦由記 - fateful #1.mp3')
            if sl > 0:
                time.sleep(1)
            pygame.mixer.music.play(-1)
            pygame.display.set_caption("  和我签订契约 成为魔法少女吧！")            
            if sl > 0:
                time.sleep(4)
            truend3 = pygame.image.load("CG\speed.jpg")
            truend3rect = truend3.get_rect()
            screen.blit(truend3,truend3rect)
            pygame.display.update()
            yes = no = num = 0
            speed[0] = speed[1] = 2
            bwrect.x=bbrect.x=bwrect.y=bbrect.y=0
            triangle_pos = circle_pos = (460,340)
            able = 18
            if sl > 0:
                time.sleep(8)
    elif abs (speed[0]) == 7:
        bgcolor = 255,105,180
    elif abs (speed[0]) == 6:
        bgcolor = 238,130,238
    elif abs (speed[0]) == 5:
        bgcolor = 255,174,183
    elif abs (speed[0]) == 4:
        bgcolor = Honeydew = 198,226,255
    elif abs (speed[0]) == 3:
        bgcolor = 255,187,255
    else:
        bgcolor = 221,160,221

#绘图条件
    t1 = (triangle_pos[0],triangle_pos[1]-20)
    t2 = (triangle_pos[0]-13,triangle_pos[1]+8)
    t3 = (triangle_pos[0]+13,triangle_pos[1]+8)
    rtriangle = pygame.draw.polygon(screen,PURPLE,[t1,t2,t3],2)
    rcircle1 = pygame.draw.circle(screen,WHITE,circle_pos,30,3)
            
    #r1rect = pygame.draw.rect(screen,BLUE,(100,100,200,100),1)
    #r2rect = pygame.draw.polygon(screen,WHITE,[(100,200),(300,300),(100,150)],5)
    #r3rect = pygame.draw.circle(screen,RED,(100,100),30,3)
    #r4rect = pygame.draw.ellipse(screen,PURPLE,(100,100,200,100),5)
    #r5rect = pygame.draw.arc(screen,WHITE,(100,100,200,100),0,3.14,5)
    #r6rect = pygame.draw.line(screen,BLUE,(100,100),(200,100),10)

    frect1 = f1.render_to(screen,(30,30),"鼠标左击：释放撞击加速魔法",fgcolor = WHITE,size = 30)
    frect2 = f1.render_to(screen,(30,80),"鼠标右击：释放时间减速魔法",fgcolor = WHITE,size = 30)
    frect3 = f1.render_to(screen,(30,130),"WASD键：释放瞬移魔法 注意限制",fgcolor = WHITE,size = 30)
    frect4 = f1.render_to(screen,(30,180),"被选中的魔法少女啊，拼尽全力收集悲叹之种来洗净沾染上的绝望吧~",fgcolor = WHITE,size = 30)
    if save_you > 0:
        frect5 = f1.render_to(screen,(30,230),"无论多少次我都会轮回，寻找把你从绝望中拯救出来的道路，相信我吧!",fgcolor = WHITE,size = 30)
    
#游戏刷新
    screen.blit(ball,ballrect)
    screen.blit(bw,bwrect)
    screen.blit(bb,bbrect)
    title = "魔女之夜              soul : " + str (soul) +"        dark : " + str (dark) + "     speed : " + str(abs(speed[0])) +"/7     magic : " + str(able) + "/18"
    pygame.display.set_caption(title)
    pygame.display.update()
    fclock.tick(fps)
