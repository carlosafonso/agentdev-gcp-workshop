import os
import random  # <-- Import the random module
from flask import Flask, request, jsonify

app = Flask(__name__)

# --- Add a list of mock data ---
MOCK_PET_NAMES = ["Fido", "Whiskers", "Buddy", "Lucy", "Max", "Daisy", "Charlie", "Sadie"]
MOCK_STATUSES = ["available", "pending", "sold"]


@app.route("/")
def index():
    """Provides a helpful index page."""
    return jsonify({
        "message": "Mock Pet Store API (Random Data)",
        "endpoints": {
            "/get": "GET: Returns a random mock pet object.",
            "/post": "POST: Echoes JSON request body."
        }
    })

@app.route("/get", methods=["GET"])
def handle_get():
    """
    Simulates returning pet data.
    
    This now returns a single mock pet object with a random name
    and status, regardless of the query parameters.
    This fulfills the spirit of both 'listPets' and 'showPetById'
    by returning sample pet data.
    """
    
    # Select random data
    random_name = random.choice(MOCK_PET_NAMES)
    random_status = random.choice(MOCK_STATUSES)
    
    # Try to get petId from query params, or assign a random one
    pet_id = request.args.get('petId', default=random.randint(1, 1000), type=int)

    # Create our mock pet response object
    mock_pet = {
        "id": pet_id,
        "name": random_name,
        "status": random_status
    }
    
    # Return the mock pet as JSON
    return jsonify(mock_pet)

@app.route("/post", methods=["POST"])
def handle_post():
    """
    Simulates the httpbin /post endpoint.
    Echoes the JSON body received.
    
    This fulfills the 'createPet' operation.
    (This function is unchanged)
    """
    data = None
    try:
        # request.json automatically parses the body as JSON
        data = request.json
        if data is None:
            # Handle cases where content-type is json but body is empty
            data = {}
    except Exception:
        # Handle cases where body is not valid JSON
        return jsonify({"error": "Failed to parse JSON body."}), 400

    # Return a 201 Created status, as per your spec
    return jsonify({
        "json": data,
        "headers": dict(request.headers),
        "url": request.url,
        "origin": request.remote_addr
    }), 201

if __name__ == "__main__":
    # Cloud Run provides the PORT environment variable
    port = int(os.environ.get("PORT", 8080))
    # Run the app, binding to all interfaces
    app.run(debug=True, host="0.0.0.0", port=port)