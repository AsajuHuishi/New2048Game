## New 2048 Game
Our New 2048 Game is mainly implemented by Python List. It is based on [Python 利用列表就可以实现新2048游戏（代码可以直接运行)](https://blog.csdn.net/qq_36937684/article/details/105488387)

* '2048' is a classic game, but the constant change of the graphics in the matrix makes it difficult.
* The New 2048 takes a card-like approach, with each column descending as the number of CARDS increases, which can be done with a list.

* Suppose there are 5 columns in total where CARDS can be played. As the new CARDS arrive, they need to be placed below the lowest card in any column. When the new CARDS are equal to the original lowest card:
1. Two CARDS disappear
2. Add the two values to create a new card value
3. If it is consistent with the original penultimate sheet, continue step 1.2.
* Every time a new card appears, it's  any one of the 2,4,8,16,32,64,bombs, every time it's eliminated, you get a score.
* You get points for each elimination; For each 2048 created, gain extra points and clear all CARDS in the column; Every time you get a bomb, all the CARDS in that column disappear.
* When all the columns reach the maximum length, the player judges negative. When all card values have been issued and the player still has room to properly enter the card, the player wins.

## Requirements
* Python
* Numpy

## How to Play
You can run it directly:
```python
python new2048.py
```
You can change the total number of cards and the max length of each column.
```python
demo = New2048(card_num=100）
demo = New2048(card_num=100,max_len=6)
```
## Results
<div align="center">
<img src=https://img-blog.csdnimg.cn/2020041315314089.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2OTM3Njg0,size_16,color_FFFFFF,t_70>
</div>

**Enjoy it now!**

## Reference
<div align="center">
<img src="https://img-blog.csdnimg.cn/20200413151456559.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2OTM3Njg0,size_16,color_FFFFFF,t_70" width="50%">
</div>