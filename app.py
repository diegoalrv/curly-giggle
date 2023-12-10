from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuración de CORS para permitir todos los orígenes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes reemplazar "*" con los orígenes que deseas permitir
    allow_credentials=True,
    allow_methods=["*"],  # Puedes limitar los métodos HTTP permitidos (e.g., ["GET", "POST"])
    allow_headers=["*"],  # Puedes limitar los encabezados permitidos
)

# Variable to control if there were changes in the image
changes_occurred = False

# URL of the current image on another server
current_image_url = "https://example.com/image1.png"

@app.get("/check_changes")
def check_changes():
    global changes_occurred
    return {"changes_occurred": changes_occurred}

@app.get("/get_new_image")
def get_new_image():
    global changes_occurred
    if changes_occurred:
        changes_occurred = False  # Reset the changes state
        return {"image_url": current_image_url}
    else:
        raise HTTPException(status_code=404, detail="No changes in the image")

@app.post("/simulate_changes")
def simulate_changes():
    global changes_occurred
    changes_occurred = True
    return {"message": "Changes simulated"}

# Ruta para actualizar la imagen actual
@app.post("/update_image")
async def update_image(new_image_url: dict):
    global current_image_url
    global changes_occurred
    current_image_url = new_image_url.get("new_image_url")
    changes_occurred = True
    return {"message": "Imagen actualizada correctamente"}