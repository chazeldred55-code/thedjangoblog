import os

# Local Django secret key
os.environ.setdefault('SECRET_KEY', 'your-production-secret-key')

# Debug mode (True for local dev)
os.environ.setdefault('DEBUG', 'False')

# Optional: local PostgreSQL database URL
os.environ.setdefault(
    'DATABASE_URL',
    'postgresql://neondb_owner:npg_dl0CytY9Mpna@ep-delicate-unit-ag1rq77b.c-2.eu-central-1.aws.neon.tech/god_music_scare_662035'
)
os.environ.setdefault(
    "CLOUDINARY_URL", "cloudinary://7TwQOb_P6j7JspFUvHSiQh8eckk@dtkzkxpsk")