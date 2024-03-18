from utils.test_runner import run_behave_tests

def main():
    features = [
        "./features/login.feature",
        "./features/transfer.feature",
    ]
    run_behave_tests(features)

if __name__ == "__main__":
    main()