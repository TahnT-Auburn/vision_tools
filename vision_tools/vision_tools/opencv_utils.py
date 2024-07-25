########################################################
'''
OpenCV Python Utility Functions

Author: Tahn Thawainin, AU GAVLAB
        pzt0029@auburn.edu

Description: Basic functions for OpenCV applications
'''
########################################################

import cv2 as cv

def frameWriter(video_path:str, save_path:str, save_name:str, save_ext:str):

        print('\nframeWriter initialized, writing frames ...')
        cap = cv.VideoCapture(video_path)

        frame_count = 0
        while cap.isOpened():
                ret, frame = cap.read()

                if not ret:
                        print('No frame recieved, writing complete\n')
                        break
                
                frame_count += 1
                save_dir = save_path + save_name + str(frame_count) + save_ext
                cv.imwrite(save_dir,frame)

                # cv.imshow('frame',frame)
                # cv.waitKey(1)

        cap.release()
        cv.destroyAllWindows()