# test_unused.py
def unused_helper():
    # intentionally unused helper
    return "I am never called"

def main():
    print("Hello from main function")

if __name__ == "__main__":
    main()
