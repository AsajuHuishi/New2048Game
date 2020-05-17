# -*- coding: utf-8 -*-
#2048是一款经典的游戏，但矩阵中图形的不断变化造成其实现有一定难度。
#新2048采用类似纸牌的方式，每一列随着牌数增加而不断向下延伸，这可以用列表来实现。
#假设共有5列位置可以放牌，随着新出的牌到达，需要将其放在任意一列的最下一张牌的下面，当新置牌其与原最下一张牌相等时：
#1.两张牌消失 2.二者的值相加，产生新的牌值 3.若其与原倒数第二张一致，继续步骤1.2
#新牌每次的出现为【2,4,8,16,32,64,bomb之任意一张】,每消去一次，获得得分
import numpy as np
#random.seed(2019)

class New2048():
    def __init__(self,card_num=100,max_len=7):
        c1,c2,c3,c4,c5=[],[],[],[],[]#5列牌
        self.player_dict = {'1':c1,'2':c2,'3':c3,'4':c4,'5':c5}
        self.score = 0  #统计得分
        self.card = [2,4,8,16,32,64,'bomb']#炸弹清空该列
        self.max_len = max_len #每列最大容纳长度
        self.card_num = card_num   #新牌数量
        #随机初始化新牌,设置不同概率(从哪抽,抽多少张,从哪里抽的概率)#但数字会变成字符串
        self.new = np.random.choice(self.card,self.card_num,p=[0.15,0.15,0.15,0.15,0.15,0.15,0.1])
        self.new = [i if i=='bomb' else int(i) for i in self.new] #将除了bomb的字符串改成数字
#        print(self.new)
            
    def player_dict_show(self):#显示当前玩家牌分布
        print('player_cards'.center(20,'-'))
        for key in sorted(self.player_dict.keys(),reverse=False):
            print(self.player_dict[key])
        print(''.center(20,'-'))
        
    #每次显示三张新牌(从左到右)
    def visual(self,i):
        if (i+2)<self.card_num:
            visual = [self.new[i],self.new[i+1],self.new[i+2]]
        elif i+2==self.card_num:
            visual = [self.new[i],self.new[i+1]]
        else:
            visual = [self.new[i]]
        reverse = visual[::-1]  #list翻转数组
        reverse = [str(i) for i in reverse] #转str        
        print('接下来的牌:'+'->'.join(reverse))
        print('当前牌',self.new[i]) 
        
    #玩家选择新牌的放置位置    
    def choice_loc(self,i):
        change = 0
        p_loc = input('放置位置(1-5)/按r退出:')
        #判断新牌放置位置是否合法
        while p_loc not in self.player_dict.keys() and p_loc!='r':
            print('放置位置不合法--请重新选择放置位置')
            p_loc = input('放置位置(1-5)/按r退出::')
        if p_loc=='r':
            return False
        #判断是否所有列都满了
        all_list = list(self.player_dict.values())#每一列的情况
        if [len(x) for x in all_list]==[self.max_len]*5:
            print('所有列已满,您输了!')
            return False
        #判断新牌放置列是否已满
        tmplist = self.player_dict[p_loc]  
        while len(tmplist)==self.max_len:
            print('第'+str(p_loc)+'列已经满了--请重新选择放置位置')
            p_loc = input('放置位置:')
            tmplist = self.player_dict[p_loc]
        #给定列增加新牌
        tmplist.append(self.new[i])
        #显示当前牌分布
        self.player_dict_show()
        #判断新置牌是否为bomb
        if tmplist[-1]=='bomb':
            tmplist[:] = []
            change=1
        #判断新置牌其与原最下一张牌是否相等
        if len(tmplist)>=2:
            while(tmplist[-1]==tmplist[-2]):#.两张牌消失 二者的值相加，产生新的牌值
                change=1
                tmplist[-2]<<=1
                tmplist.pop()
                self.score+=1
                if len(tmplist)==1:
                    break 
        #判断是否存在2048，如果存在，清空该列
        if 2048 in tmplist:
            change=1
            tmplist[:] = []#注意：用tmplist=[]不能清空player_dict的内存
            self.score+=10
        #显示本轮当前牌最终分布
        if change==1:
            self.player_dict_show()
        return True
    
    def run(self): 
        flag = 1
        print('每列最大容纳长度:',self.max_len)
        self.player_dict_show()
        for i in range(self.card_num):
            if flag:
                self.visual(i)
                flag = self.choice_loc(i)
            else:
                print('游戏结束!')
                break
        print('游戏结束!')
        self.show_score()
        
    def show_score(self):    
        print('您的分数:',self.score)
        
def main():        
    demo = New2048()
    demo.run() 

if __name__=="__main__":
    main()
       
    