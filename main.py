# -*- coding: utf-8 -*-

# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。
    str = '[微笑][色][发呆][酷拽][抠鼻][流泪][捂脸][发怒][呲牙][尬笑][害羞][调皮][舔屏][看][爱心][比心][赞][鼓掌][感谢][抱抱你][玫瑰][灵机一动][耶][打脸][大笑][机智][送心][666][闭嘴][来看我][一起加油][哈欠][震惊][晕][衰][困][疑问][泣不成声][小鼓掌][大金牙][偷笑][石化][思考][吐血][可怜][嘘][撇嘴][笑哭][奸笑][得意][憨笑][坏笑][抓狂][泪奔][钱][恐惧][愉快][快哭了][翻白眼][互粉][我想静静][委屈][鄙视][飞吻][再见][紫薇别走][听歌][求抱抱][绝望的凝视][不失礼貌的微笑][不看][裂开][干饭人][吐舌][呆无辜][白眼][熊吉][猪头][冷漠][微笑袋鼠][凝视][暗中观察][二哈][菜狗][黑脸][展开说说][蜜蜂狗][摸头][皱眉][擦汗][红脸][做鬼脸][强][如花][吐][惊喜][敲打][奋斗][吐彩虹][大哭][嘿哈][加好友][惊恐][惊讶][囧][难过][斜眼][阴险][悠闲][咒骂][吃瓜群众][绿帽子][真的会谢][达咩][敢怒不敢言][投降][求求了][眼含热泪][叹气][好开心][不是吧][动动脑子][表面微笑][表面呲牙][鞠躬][躺平][九转大肠][敲木鱼][不你不想][一头乱麻][kisskiss][你不大行][噢买尬][宕机][还得是我][6][脸疼][他急了][苦涩][逞强落泪][强壮][碰拳][OK][击掌][左上][握手][抱拳][勾引][拳头][弱][胜利][右边][左边][亚运鼓掌][金牌][手花][嘴唇][心碎][凋谢][啤酒][咖啡][蛋糕][礼物][撒花][加一][减一][okk][V5][绝][给力][红包][屎][发][我太难了][18禁][炸弹][去污粉][西瓜][加鸡腿][我酸了][握爪][太阳][月亮][给跪了][蕉绿][扎心][胡瓜][yyds][emo][开心兔][招财兔][年兽兔][打call][栓Q][无语][雪人][雪花][圣诞树][平安果][圣诞帽][气球][干杯][烟花][福][candy][糖葫芦][虎头][饺子][鞭炮][元宝][灯笼][锦鲤][巧克力][汤圆][情书][iloveyou][戒指][小黄鸭][棒棒糖][纸飞机][必胜][粽子]'
    temp = ''
    k = 0
    for s in str:
        temp += s
        if s == ']':
            k += 1
            if k == 7:
                k = 0
                print(temp)
                temp = ''
    print(temp)


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')
