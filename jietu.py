import os
import time

def getImage(driver):
    '''
    截取图片,并保存在images文件夹
    :return: 无
    '''
    timestrmap = time.strftime('%Y%m%d_%H.%M.%S')
    imgPath = os.path.join('E:/Study/GHWH/images', '%s.png' % str(timestrmap))

    #driver.save_screenshot(imgPath)
    imgs=driver.get_screenshot_as_base64()
    print(imgs)
    print('screenshot:', timestrmap, '.png' )