#%%
from vision_tools.opencv_utils import *

video_path = 'D:\\TestingData\\test_1\\source\\videos\\RRMC_SS.mp4'
save_path = 'D:\\TestingData\\test_1\\testing\\images\\RRMC_SS\\'
save_name = 'RRMC_SS'
save_ext = '.jpg'
frameWriter(video_path=video_path, save_path=save_path, save_name=save_name, save_ext=save_ext)