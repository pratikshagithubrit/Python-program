import multiprocessing
def main():
    print("number of cores are",multiprocessing.cpu_count())
if __name__ == "__main__":
    main()
