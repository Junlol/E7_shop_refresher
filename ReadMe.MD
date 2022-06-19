## Epic7 Shop Refresher
A rewrite of the script done originally by [EmaOlay](https://github.com/EmaOlay/E7-Auto-Shop-Refresh) that automatically refreshes the shop and buys covenant bookmarks and mystics.

### Requirements
- requires python 3
- pip install -r requirements.txt
- run main.py


Works fine on my screen (1080p) with the emulator maximized but may need some tinkering to get it to work on others.
Taking new screenshots of the buttons on whatever screen resolutions you're using and setting the x & y offset of the item buy button should fix any problems.


- I might try in the future (whenever I'm free) to connect directly to adb to prevent any problems.

---

此為利用影像辨識來判斷刷到書籤後，執行購買動作。

使用方法
===
用模擬器跑 E7，並且全螢幕，原作者是用 1080p 下去做的，所以如果解析度不一樣就會沒辦法 work（需要調整圖片跟座標）

以下以 windows 為例：
1. 安裝 python 3（有裝配裝器的話應該都有了）
2. 整包下載到電腦
3. 打開 cmd，將目錄位置移到下載包位置，例如輸入 cd C:\Users\XXX\Downloads\E7_shop_refresher-main
4. cmd 中執行 pip install -r requirements.txt（會安裝必要一些工具）
5. cmd 中執行 python main.py

接著會倒數 5 秒，5 秒後就會開始刷商店，所以你需要在這 5 秒內進入商店，並開啟全螢幕模式（BlueStacks 是 F11）
如果要結束刷商店，只要離開商店或結束全螢幕就可以了（程式判斷不到在商店中就會停止）

祝大家神祕聖約刷到沒錢。

by 半分青
