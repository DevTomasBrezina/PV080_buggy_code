import os
import json

SECRET_KEY = os.urandom(32)


class Profile:
    def __init__(self):
        self.secret_key = None
        self.name = "Default name"
        self.address = "Default address"
        self.age = -1
        self.extra = {
            "hobbies": ["Default hobby"],
        }

    def __str__(self):
        return json.dumps(
            {
                "name": self.name,
                "address": self.address,
                "age": self.age,
                "extra": self.extra,
            },
            indent=4,
        )


def merge(src, dst):
    # Recursive merge function
    for key, value in src.items():
        if hasattr(dst, "__getitem__"):
            if dst.get(key) and type(value) == dict:
                merge(value, dst.get(key))
            else:
                dst[key] = value
        elif hasattr(dst, key) and type(value) == dict:
            merge(value, getattr(dst, key))
        else:
            setattr(dst, key, value)


profile = Profile()

for _ in range(100):
    try:
        merge(json.loads(input("input json info to update profile>>>")), profile)
    except Exception as e:
        print("Error: ", e)
        continue
    if profile.secret_key == SECRET_KEY:
        print("You found the secret key! Now show your exploit to the tutor.")
        break

    print("Profile updated: ", profile)

