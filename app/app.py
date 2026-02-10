import time
import os

APP_NAME = os.getenv("APP_NAME", "OMNIOPS")
ENV = os.getenv("ENV", "dev")

print(f"🚀 {APP_NAME} started")
print(f"🌍 Environment: {ENV}")

while True:
    print(f"🙏 Ganpati Bappa Morya | {APP_NAME} alive in {ENV}")
    time.sleep(10)

