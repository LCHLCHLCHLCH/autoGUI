import pyautogui
import PIL
import pyscreeze
import time


# 读取屏幕分辨率大小
screenWidth, screenHeight = pyautogui.size()


# 定位函数，屏幕中含匹配项时返回中心x，y坐标，无匹配项则返回None
def location(png, confidence):
	icon = pyautogui.locateOnScreen(png, confidence=confidence)  # 新增参数confidence，须配置opencv环境
	if icon is not None:
		center = pyautogui.center(icon)
		return center
	else:
		time.sleep(3)  # 考虑网页的加载时间，无法识别时延时3秒
		icon = pyautogui.locateOnScreen(png, confidence=confidence)
		if icon is None:
			return None
		else:
			center = pyautogui.center(icon)
			return center

		
def main():
	print("程序将于3秒后开始运行")
	time.sleep(3)
	while(True):
		log = open("D:\\xuexitong_auto_play\\log.txt", "a")
		# 点击播放按钮
		while True:
			try:
				playButton = location('playbutton.png',0.9)
				log.write("找到播放按钮,执行点击操作")
				pyautogui.moveTo(playButton[0], playButton[1], duration=0.8)
				pyautogui.click()
				break
			except:
				log.write("播放按钮未找到,等待3秒")
				time.sleep(3)


		# 等待视频播放结束,这时屏幕上会出现重播标志
		while True:
			try:
				location('replay.png',0.9)
				log.write("匹配到重播按钮,即将进入下一节")
				break
			except:
				time.sleep(10)

		# 寻找下一节的标志并点击
		while True:
			try:
				next = location('next.png',0.9)
				pyautogui.moveTo(next[0],next[1],duration=0.9)
				pyautogui.click()
				break
			except:
				log.write("未找到下一节按钮,向下滚动")
				pyautogui.scroll(-750)

		# 寻找下一节的标志并点击(这时处在答题界面)
		while True:
			try:
				next = location('next.png',0.9)
				pyautogui.moveTo(next[0],next[1],duration=0.9)
				pyautogui.click()
				break
			except:
				pyautogui.scroll(-750)

		log.close()


if __name__ == '__main__':
	main()
