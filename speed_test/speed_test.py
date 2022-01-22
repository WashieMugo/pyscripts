import speedtest  # pip install speedtest-cli

speed = speedtest.Speedtest()


def main():
    while True:
        print('\a')
        choice = int(input("""Check Your Connection Speed
        1: Download Speed
        2: Upload Speed
        3: Exit
        Choice(1/2/3): """))
        print('\a')

        if choice == 1:
            print('counting...')
            print(
                f"Download Speed: {'{:.2f}'.format(speed.download()/1024/1024)} Mb/s")
        elif choice == 2:
            print("Counting...")
            print(
                f"Upload Speed: {'{:.2f}'.format(speed.upload()/1024/1024)} Mb/s")
        elif choice == 3:
            print("Exciting the Program ...")
            quit()
        else:
            print("Invalid Option !")


if __name__ == '__main__':
    main()
