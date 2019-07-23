from youtube_master import YoutubeMaster


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--root_convert', default="/mnt/IYONas/ASR/ja/YOUTUBE/all")
    parser.add_argument('--csv_annotation', default="/mnt/IYONas/ASR/csv/YOUTUBE/yt_all.csv")
    parser.add_argument('--world_size', default=1, type=int)
    parser.add_argument('--rank', default=0, type=int)
    args = parser.parse_args()

    master = YoutubeMaster(world_size=args.world_size,
                           rank=args.rank,
                           csv_file=args.csv_annotation,
                           root_convert=args.root_convert)
    master.launch()