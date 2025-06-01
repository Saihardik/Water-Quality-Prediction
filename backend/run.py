from app import create_app


app = create_app()


if __name__ == "__main__":
    print("🚀 Launching Flask server...")
    app.run(debug=True)
