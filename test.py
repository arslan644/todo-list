import msvcrt
import sys

def move_cursor(x, y):
    sys.stdout.write(f"\x1b[{y};{x}H")
    sys.stdout.flush()

def main():
    x, y = 1, 1

    while True:
        move_cursor(x, y)
        key = msvcrt.getch()

        if key == b'\xe0':  # Arrow key prefix
            key = msvcrt.getch()
            if key == b'H':  # Up arrow
                y -= 1
            elif key == b'P':  # Down arrow
                y += 1
            elif key == b'K':  # Left arrow
                x -= 1
            elif key == b'M':  # Right arrow
                x += 1
        elif key == b'\r':  # Enter key
            break

    move_cursor(1, y + 1)  # Move one line beneath input
    print("Text below input")

if __name__ == "__main__":
    main()
