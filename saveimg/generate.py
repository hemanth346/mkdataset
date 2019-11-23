import os
import time
import numpy as np
import cv2
from collections import Counter

class GenerateData:
    def __init__(self,cls:'str',path:'str'='.',reverse=False, continuous=False, distribution:'list'=[0.6,0.2,0.2])->'None':
        self.name = cls
        self.path = path
        self.distribution = distribution    # train, test and validation distribution
        self.train = os.path.join(self.path, 'train', self.name)
        self.test = os.path.join(self.path, 'test', self.name)
        self.val = os.path.join(self.path, 'validation', self.name)
        self.continuous = continuous
        if reverse:
            self.train = os.path.join(self.path, self.name, 'train')
            self.test = os.path.join(self.path, self.name, 'test')
            self.val = os.path.join(self.path, self.name, 'validation')
        self.__total_counter = Counter('total')
        self.__counter = Counter(['train', 'test', 'val'])

    def _ensure_dir(self):
        if not os.path.exists(self.train):
            os.makedirs(self.train)
        if not os.path.exists(self.test):
            os.makedirs(self.test)
        if not os.path.exists(self.val):
            os.makedirs(self.val)

    def capture(self, file='', fps=0.5):
        if not file:
            file = 0    # webcam feed
        vid = cv2.VideoCapture(file)  

        if not (vid.isOpened()):
            raise ValueError('Error reading video feed')

        self._ensure_dir()      # create necessary directories

        while (vid.isOpened()):
            check, image = vid.read()
            if check is False:
                break
            self.save_image(image)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            time.sleep(fps)
            print('---------')
        vid.release()
        cv2.destroyAllWindows()

    def save_image(self, image):
        choice = np.random.choice(np.arange(1, 4), p=self.distribution)         # https://stackoverflow.com/a/4266645/7445772
        # print('Count is ',self.__counter, 'choice : ', choice)
        if choice == 1:
            img_path = os.path.join(self.train, "{0}_{1}.jpg".format(self.name, str(self.__counter['train'])))
            if self.continuous:
                img_path = os.path.join(self.train, "{0}_{1}.jpg".format(self.name, str(self.__total_counter['total'])))
            cv2.imwrite(img_path, image)
            print('Saved', img_path)
            self.__counter['train'] += 1
            self.__total_counter['total'] += 1
        if choice == 2:
            img_path = os.path.join(self.test, "{0}_{1}.jpg".format(self.name, str(self.__counter['test'])))
            if self.continuous:
                img_path = os.path.join(self.test, "{0}_{1}.jpg".format(self.name, str(self.__total_counter['total'])))
            cv2.imwrite(img_path, image)
            print('Saved', img_path)
            self.__counter['test'] += 1
            self.__total_counter['total'] += 1
        if choice == 3:
            img_path = os.path.join(self.val, "{0}_{1}.jpg".format(self.name, str(self.__counter['val'])))
            if self.continuous:
                img_path = os.path.join(self.val, "{0}_{1}.jpg".format(self.name, str(self.__total_counter['total'])))
            cv2.imwrite(img_path, image)
            print('Saved', img_path)
            self.__counter['val'] += 1
            self.__total_counter['total'] += 1

