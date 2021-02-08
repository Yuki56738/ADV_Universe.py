#!/usr/bin/python3
import sys
print("Universe ADVへようこそ。")

print("あなたは暗い場所にいる。どうする？")

print("選択肢1: ポケットを探る。")
print("選択肢2: 立ち尽くす。")
select=0
print(">>", end="")
select=input()
#print(f"debug: select: {select}")
if not select == 0:
    if select == "2":
        print("GAME OVER")
        sys.exit(0)
    if select == "1":
        print("ポケットからマッチを見つけた。どうする？")
        print("選択肢1: マッチを点ける。")
        print("選択肢2: 無視する。")
        select=0
        print(">>", end="")
        select=input()
        if not select == 0:
            if select == "2":
                print("GAME OVER")
                sys.exit(0)
            if select == "1":
                print("マッチの灯りで松明が見えた。どうする？")
                print("選択肢1: マッチで松明を点ける。")
                print("選択肢2: 立ち尽くす。")
                select = 0
                print(">>", end="")
                select = input()
                if not select == 0:
                    if select == "2":
                        print("GAME OVER")
                        sys.exit(0)
                    if select == "1":
                        print("松明の灯りで親友が見えた。どうする？")
                        print("選択肢1: 寄り添う。")
                        print("選択肢2: 無視する。")
                        select = 0
                        print(">>", end="")
                        select = input()
                        if not select == 0:
                            if select == "2":
                                print("親友に殺された。")
                                print("GAME OVER")
                                sys.exit(0)
                            if select == "1":
                                print("親友に手紙を渡された。どうする？")
                                print("選択肢1: 読む。")
                                print("選択肢2: 手紙を捨てる。")
                                print(">>", end="")
                                select = 0
                                select = input()
                                if not select == 0:
                                    if select == "2":
                                        print("親友に殺された。")
                                        print("GAME OVER")
                                        sys.exit(0)
                                    if select == "1":
                                        print("「この部屋の左側に隠し扉がある。選択はあなた次第。」")
                                        print("選択肢1: 扉を開ける。")
                                        print("選択肢2: 扉を開けない。")
                                        print(">>", end="")
                                        select = 0
                                        select = input()
                                        if not select == 0:
                                            if select == "2":
                                                print("GAME OVER")
                                                sys.exit(0)
                                            if select == "1":
                                                print("洞窟が見えた。どうする？")
                                                print("選択肢1: 洞窟を抜ける。")
                                                print(">>", end="")
                                                select = 0
                                                select = input()
                                                if not select == 0:
                                                    if select == "1":
                                                        print("新世界に到達。\nゲームクリア。")
