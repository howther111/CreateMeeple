# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import CreateMeeple

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('CreateMeeple')
    CreateMeeple.createMeeple(255, 0, 0)
    CreateMeeple.createMeeple(0, 255, 0)
    CreateMeeple.createMeeple(0, 0, 255)
    CreateMeeple.createMeeple(63, 63, 63)
    CreateMeeple.createMeeple(191, 191, 191)
    CreateMeeple.createMeeple(0, 255, 255)
    CreateMeeple.createMeeple(255, 255, 0)
    CreateMeeple.createMeeple(255, 0, 255)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
