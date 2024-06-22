import os

def get_base_url():
    env = os.environ.get("ENV", "prod")

    if env.lower() == "test":
        return "http://localhost:7888/Belgrade-with-children"
    elif env.lower() == "prod":
        return "https://belgrade-with-kids.onrender.com"
    else:
        raise Exception(f"Unknown envirnment: {env}")