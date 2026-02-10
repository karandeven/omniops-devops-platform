import os

def main():
    app_name = os.getenv("APP_NAME", "OMNIOPS")

    print("Ganpati Bappa Morya 🙏")
    print(f"{app_name} is running.")
    print("This app is a base for Docker, CI/CD and Kubernetes learning.")

if __name__ == "__main__":
    main()

