from gnutools.www import Youtube
from gnutools.utils import read_csv
from concurrent.futures import ProcessPoolExecutor, as_completed
from tqdm import tqdm
import os
import time
import argparse
import numpy as np
import random


class YoutubeMaster:
    def __init__(self, root_convert, world_size=1, rank=0, csv_file=None, id_list=None):
        self.root_convert = root_convert
        self.ids_completed = self.get_completed(self.root_convert)
        if id_list is None:
            lines = read_csv(csv_file)
            annotations = set([line[0] for line in lines])
            N = len(list(annotations))
            step = N // world_size
            start = np.arange(0, N, step + 1)[rank]
            id_list = [annotation for annotation in list(annotations)[start:start + step + 1]]
        random.shuffle(id_list)
        self.id_list = self.filter_completed(set(id_list))
        self.fs=[]

    def launch(self):
        with ProcessPoolExecutor() as e:
            self.fs = [e.submit(self.prepare, id=id, root_convert=self.root_convert) for id in tqdm(self.id_list)]
            for f in tqdm(as_completed(self.fs)):
                pass

    @staticmethod
    def prepare(id, root_convert):
        yt = Youtube(id=id)
        yt.download(root=root_convert)
        yt.post_process(fq=16000,
                        split_audio=True,
                        split_captions=True)

    def get_completed(self, root_convert):
        def is_completed(dir):
            try:
                dirs = os.listdir(dir)
                assert dirs.__contains__("audio")
                assert dirs.__contains__("text")
                files_audio = os.listdir("{dir}/audio".format(dir=dir))
                files_text = os.listdir("{dir}/text".format(dir=dir))
                assert len(files_audio) == len(files_text)
            except:
                return False
            return True

        ids=set()
        for id in os.listdir("{root}".format(root=root_convert)):
            if is_completed("{root}/{id}".format(root=root_convert, id=id)):
                ids.add(id)
        return ids

    def filter_completed(self, ids):
        return ids.difference(self.ids_completed)


if __name__=="__main__":
    yt = Youtube(id="e3Odkr4yhD0")
    yt.download(root="/mnt/IYONas3/ASR/ja/audio_text/YOUTUBE/all")
    yt.post_process(fq=16000,
                    split_audio=True,
                    split_captions=True)