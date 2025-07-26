import sys

from gui_handler import App


def main():
    try:
        # Create the main application window
        App.create_window(500, 200, "Hash Application")

        # Start the GUI event loop
        App.open_window()

    except KeyboardInterrupt:
        print("\nApplication interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
