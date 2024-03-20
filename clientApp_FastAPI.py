from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
import shutil
from predict import DogCatClassifier

app = FastAPI()

# Set up CORS (similar to Flask-CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Instantiate your classifier outside of your route to avoid reloading for each request
classifier = DogCatClassifier("inputImage.jpg")

@app.get("/")
async def home():
    return FileResponse('templates/index.html')

@app.post("/predict/")
async def predict_route(file: UploadFile = File(...)):
    try:
        # Save the received image to a file
        with open(classifier.filename, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Make a prediction
        result = classifier.prediction_dog_cat()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
