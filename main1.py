from Final_Project_1 import *


def main():
    application = QApplication([])
    window = Students()
    window.setFixedSize(500, 350)
    window.show()
    application.exec()

if __name__ == '__main__':
    main()