import utils.logo as logo
import utils.screen as screen
def main():
    logo.run()
    game = screen.Screen()
    game.check_file()
    game.start()
if __name__ == "__main__":
    main()
