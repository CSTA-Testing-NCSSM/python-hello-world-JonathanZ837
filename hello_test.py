import hello;
    
def test():
    assert hello.hello_world() == "Hello World!", "This should be 'Hello World!'"

if __name__ == "__main__":
    try:
        test()
        print("All tests passed")  # Print success message after tests have run
    except AssertionError as e:
        print("Test failed:", e)
