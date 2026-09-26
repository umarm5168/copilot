import sys

# Ensure stdout uses UTF-8 to support emojis on Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("Hello, World! 👋 Your uv backend is running.")
