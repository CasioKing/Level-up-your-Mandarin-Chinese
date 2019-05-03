import random
import time

# This is where your score will be kept

score = 0
total = 0

# Here is the data for all the characters/words used in the program

def word_1(word='水'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Shui')
    if answer.lower() == 'Shui'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return '"Empty your mind, be formless, shapeless-like water."-Bruce Lee\n'


def word_2(word='电视'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('DianShi')
    if answer.lower() == 'DianShi'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means TV\n'


def word_3(word='手机'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('ShouJi')
    if answer.lower() == 'ShouJi'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means cell phone\n'


def word_4(word='电脑'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('DianNao')
    if answer.lower() == 'DianNao'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means computer\n'


def word_5(word='避孕套'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('BiYunTao')
    if answer.lower() == 'BiYunTao'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'Your Parents Would Be Proud. This means condom\n'


def word_6(word='颜色'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('YanSe')
    if answer.lower() == 'YanSe'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'President Kennedy was the fastest random speaker in the world with upwards of 350 words per minute.\nThis' \
           ' means color\n'


def word_7(word='杯子'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('BeiZi')
    if answer.lower() == 'BeiZi'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This is cup\n'

def word_8(word='怎麽樣'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('ZenMeYang')
    if answer.lower() == 'ZenMeYang'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'The sound of E.T. walking was made by someone squishing her hands in jelly.\nThis is a way of asking ones' \
           ' opinion\n'

def word_9(word='飯店'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('FanDian')
    if answer.lower() == 'FanDian'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'The Earth Is Flat.\nThis is restaurant\n'

def word_10(word='碉堡了'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('DiaoBaoLe')
    if answer.lower() == 'DiaoBaoLe'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This is like saying amazing!\n'

def word_11(word='明天'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('MingTian')
    if answer.lower() == 'MingTian'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'Use this to say tomorrow!\n'

def word_12(word='昨天'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('ZuoTian')
    if answer.lower() == 'ZuoTian'.lower():
        print('correct')
        score +=1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'Use this to say yesterday!\n'

def word_13(word='笑'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Xiao')
    if answer.lower() == 'Xiao'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'Use this to say laugh!\n'

def word_14(word='能'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Neng')
    if answer.lower() == 'Neng'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means can\n'

def word_15(word='炒飯'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('ChaoFan')
    if answer.lower() == 'ChaoFan'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'Don\'t touch my fried rice.\n'

def word_16(word='變態'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('BianTai')
    if answer.lower() == 'BianTai'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This is how you say abnormal.\n'

def word_17(word='漂亮'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('PiaoLiang')
    if answer.lower() == 'PiaoLiang'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'Beautiful.\n'

def word_18(word='商店'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('ShangDian')
    if answer.lower() == 'ShangDian'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This is how you say store.\n'

def word_19(word='学习'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('XueXi')
    if answer.lower() == 'XueXi'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This is what you\'re doing aka learning or to study.\n'

def word_20(word='笔'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Bi')
    if answer.lower() == 'Bi'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This is how you say pen or pencil.\n'

def word_21(word='菜'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Cai')
    if answer.lower() == 'Cai'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This is how you say vegetable and dish depending on context.\n'

def word_22(word='茶'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Cha')
    if answer.lower() == 'Cha'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This is how you say tea.\n'

def word_23(word='常常'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('ChangChang')
    if answer.lower() == 'ChangChang'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This is how you say often.\n'

def word_24(word='周'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Zhou')
    if answer.lower() == 'Zhou'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This is how you say week.\n'

def word_25(word='周末'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('ZhouMo')
    if answer.lower() == 'ZhouMo'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This is how you say weekend.\n'

def word_26(word='做'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Zuo')
    if answer.lower() == 'Zuo'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This is to do.\n'

def word_27(word='都'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Dou')
    if answer.lower() == 'Dou'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This is how you say both or all.\n'

def word_28(word='难'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Nan')
    if answer.lower() == 'Nan'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This is how you say difficult.\n'

def word_29(word='更'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Geng')
    if answer.lower() == 'Geng'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This is an adverb that means more.\n'

def word_30(word='用'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Yong')
    if answer.lower() == 'Yong'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This is how you say use.\n'

def word_31(word='去'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Qu')
    if answer.lower() == 'Qu'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This is how you say go.\n'

def word_32(word='会'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Hui')
    if answer.lower() == 'Hui'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This is how you say can.\n'

def word_33(word='多'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Duo')
    if answer.lower() == 'Duo'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This adjective means many.\n'

def word_34(word='书包'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('ShuBao')
    if answer.lower() == 'ShuBao'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This is how you say backpack.\n'

def word_35(word='话'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Hua')
    if answer.lower() == 'Hua'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This is how you say talk.\n'

def word_36(word='活'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Huo')
    if answer.lower() == 'Huo'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This is how you say life and can also be used to mean saved a life.\n'

def word_37(word='星期'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('XingQi')
    if answer.lower() == 'XingQi'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means day of the week.\n'

def word_38(word='影片'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('YingPian')
    if answer.lower() == 'YingPian'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This is how you say video.\n'

def word_39(word='电玩'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('DianWan')
    if answer.lower() == 'DianWan'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This is how you say video game.\n'

def word_40(word='书'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Shu')
    if answer.lower() == 'Shu'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This is how you say book.\n'

def word_41(word='歌曲'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('GeQu')
    if answer.lower() == 'GeQu'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means song.\n'

def word_42(word='听'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Ting')
    if answer.lower() == 'Ting'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This is how you say listen.\n'

def word_43(word='唱'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Chang')
    if answer.lower() == 'Chang'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This is how you say sing.\n'

def word_44(word='跳'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Tiao')
    if answer.lower() == 'Tiao'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means jump.\n'

def word_45(word='看'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Kan')
    if answer.lower() == 'Kan'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This is how you say watch.\n'

def word_46(word='打'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Da')
    if answer.lower() == 'Da'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This is how you say strike or play.\n'

def word_47(word='球'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Qiu')
    if answer.lower() == 'Qiu'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This is how you say sphere or ball.\n'

def word_48(word='热'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Re')
    if answer.lower() == 'Re'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This is how you say hot.\n'

def word_49(word='音乐'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('YinYue')
    if answer.lower() == 'YinYue'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This is how you say music.\n'

def word_50(word='生活'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('ShengHuo')
    if answer.lower() == 'ShengHuo'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means life in a general way.\n'

def word_51(word='有的（时候）'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('YouDe(ShiHou)')
    if answer.lower() == 'YouDe'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means some（times）.\n'

def word_52(word='火'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Huo')
    if answer.lower() == 'Huo'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means fire or rage.\n'

def word_53(word='油'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('You')
    if answer.lower() == 'You'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means grease/oil.\n'

def word_54(word='加'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Jia')
    if answer.lower() == 'Jia'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means add.\n'

def word_55(word='帮'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Bang')
    if answer.lower() == 'Bang'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This is the verb help.\n'

def word_56(word='就'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Jiu')
    if answer.lower() == 'Jiu'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means to come near or just.\n'

def word_57(word='莫'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Mo')
    if answer.lower() == 'Mo'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means do not, can not, and is a negative word.\n'

def word_58(word='真'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Zhen')
    if answer.lower() == 'Zhen'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means true.\n'

def word_59(word='觉得'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('JueDe')
    if answer.lower() == 'JueDe'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means to think or feel.\n'

def word_60(word='别的'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('BieDe')
    if answer.lower() == 'BieDe'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means other.\n'

def word_61(word='睡觉'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('ShuiJiao')
    if answer.lower() == 'ShuiJiao'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means to sleep.\n'

def word_62(word='需要'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('XuYao')
    if answer.lower() == 'XuYao'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means need.\n'

def word_63(word='一般'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('YiBan')
    if answer.lower() == 'YiBan'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means the same.\n'

def word_64(word='一样'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('YiYang')
    if answer.lower() == 'YiYang'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means the same or alike.\n'

def word_65(word='其'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Qi')
    if answer.lower() == 'Qi'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means she, he, or it.\n'

def word_66(word='心'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Xin')
    if answer.lower() == 'Xin'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means heart.\n'

def word_67(word='入'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Ru')
    if answer.lower() == 'Ru'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means to enter.\n'

def word_68(word='牛'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Niu')
    if answer.lower() == 'Niu'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means cow.\n'

def word_69(word='妙'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Miao')
    if answer.lower() == 'Miao'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means wonderful.\n'

def word_70(word='全'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Quan')
    if answer.lower() == 'Quan'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means to make complete.\n'

def word_71(word='身'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Shen')
    if answer.lower() == 'Shen'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means ones body or oneself.\n'

def word_72(word='作'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Zuo')
    if answer.lower() == 'Zuo'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means work and the verb can mean to grow.\n'

def word_73(word='水平'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('ShuiPing')
    if answer.lower() == 'ShuiPing'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means standard or level.\n'

def word_74(word='从'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Cong')
    if answer.lower() == 'Cong'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means to join or follow.\n'

def word_75(word='床'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Chuang')
    if answer.lower() == 'Chuang'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means bed.\n'

def word_76(word='床單'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('ChuangDan')
    if answer.lower() == 'ChuangDan'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means bed sheet.\n'

def word_77(word='床墊'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('ChuangDian')
    if answer.lower() == 'ChuangDian'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means mattress.\n'

def word_78(word='毯子'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('TanZi')
    if answer.lower() == 'TanZi'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means blanket.\n'

def word_79(word='衣櫃'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('YiGui')
    if answer.lower() == 'YiGui'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means dresser.\n'

def word_80(word='枕頭'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('ZhenTou')
    if answer.lower() == 'ZhenTou'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means pillow.\n'

def word_81(word='木'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Mu')
    if answer.lower() == 'Mu'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means wood.\n'

def word_82(word='土'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Tu')
    if answer.lower() == 'Tu'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means earth or dirt; soil.\n'

def word_83(word='金'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('Jin')
    if answer.lower() == 'Jin'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means metal or gold.\n'

def word_84(word='臥室'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('WoShi')
    if answer.lower() == 'WoShi'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means bedroom.\n'

def word_85(word='浴室'):
    global total
    global score
    print(word)
    print('Can you tell me this character?')
    answer = input()
    if answer.lower() == 'idk'.lower():
        print('YuShi')
    if answer.lower() == 'YuShi'.lower():
        print('correct')
        score += 1
    else:
        print('wrong')
    total += 1
    time.sleep(1)
    return 'This means bathroom.\n'

# my_ListI is individual characters my_ListD is words with two characters
# and my_ListS is sentences

my_ListI = [word_1,word_13, word_14, word_20, word_21, word_22,word_24, word_26, word_27, word_28, word_29, word_30,
            word_31, word_32, word_33,word_35, word_36, word_40, word_42, word_43, word_44, word_45,word_46, word_47,
            word_48, word_52, word_53, word_54, word_55, word_56, word_57, word_58, word_65, word_66, word_67, word_68,
            word_69, word_70, word_71, word_72, word_74, word_75, word_81, word_82, word_83
            ]
my_ListD = [word_2, word_3, word_4, word_6, word_7, word_9, word_11, word_12, word_15, word_16, word_17, word_18,
            word_19, word_23, word_25, word_34, word_37, word_38, word_39, word_41, word_49, word_50, word_51, word_59,
            word_60, word_61, word_62, word_63, word_64, word_73, word_76, word_77, word_78, word_79, word_80, word_84,
            word_85
    ]
my_ListS = [word_5, word_8, word_10,

]


attempts = 0

# This is a function for randomly displaying individual characters

def the_ProblemI():
    global score
    global total
    global attempts
    while attempts <= 1:
        print(random.choice(my_ListI)())
        time.sleep(.5)
        print('Score=', score)
        print('Total=', total, '\n')
        time.sleep(1)
        while total == 20:
            print('Would you like to continue?')
            does_Continue = input()
            if does_Continue == 'yes'.lower():
                score = 0
                total = 0
                the_ProblemI()
            if does_Continue != 'yes'.lower():
                score = 0
                total = 0
                if score <= 11:
                    print('You Failed\n')
                    the_Quiz()
                if score <= 13:
                    print('You scored a D\n')
                    the_Quiz()
                if score <= 15:
                    print('You scored a C\n')
                    the_Quiz()
                if score <= 17:
                    print('You scored a B\n')
                    the_Quiz()
                if score >= 18:
                    print('Nice, you scored an A\n')
                    the_Quiz()


# This is a function for randomly displaying double characters

def the_ProblemD():
    global score
    global total
    global attempts
    while attempts <= 1:
        print(random.choice(my_ListD)())
        time.sleep(.5)
        print('Score=', score)
        print('Total=', total, '\n')
        time.sleep(1)
        while total == 20:
            print('Would you like to continue?')
            does_Continue = input()
            if does_Continue == 'yes'.lower():
                score = 0
                total = 0
                the_ProblemD()
            if does_Continue != 'yes'.lower():
                score = 0
                total = 0
                if score <= 11:
                    print('You Failed\n')
                    the_Quiz()
                if score <= 13:
                    print('You scored a D\n')
                    the_Quiz()
                if score <= 15:
                    print('You scored a C\n')
                    the_Quiz()
                if score <= 17:
                    print('You scored a B\n')
                    the_Quiz()
                if score >= 18:
                    print('Nice, you scored an A\n')
                    the_Quiz()


# This is a function for randomly displaying sentences

def the_ProblemS():
    global score
    global total
    global attempts
    while attempts <= 1:
        print(random.choice(my_ListS)())
        time.sleep(.5)
        print('Score=', score)
        print('Total=', total, '\n')
        time.sleep(1)
        while total == 20:
            print('Would you like to continue?')
            does_Continue = input()
            if does_Continue == 'yes'.lower():
                score = 0
                total = 0
                the_ProblemS()
            if does_Continue != 'yes'.lower():
                score = 0
                total = 0
            if score <= 11:
                print('You Failed\n')
                the_Quiz()
            if score <= 13:
                print('You scored a D\n')
                the_Quiz()
            if score <= 15:
                print('You scored a C\n')
                the_Quiz()
            if score <= 17:
                print('You scored a B\n')
                the_Quiz()
            if score >= 18:
                print('Nice, you scored an A\n')
                the_Quiz()


# This is the function for the quiz itself

def the_Quiz():
    global score
    global total
    global attempts
    print('Would you like to practice single character, double characters, or sentences?\n')
    the_Decider = input()
    print('\n')
    while the_Decider == 'single'.lower():
        the_ProblemI()
    while the_Decider == 'double'.lower():
        the_ProblemD()
    while the_Decider == 'sentences'.lower():
        the_ProblemS()

# Time to level up ಠ_ಠ

the_Quiz()




