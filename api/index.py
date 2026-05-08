from app import app

# Vercel entry point
def handler(event, context):
    return app