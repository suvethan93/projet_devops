from fastapi import FastAPI

app = FastAPI(
    title="API DevOps",
    description="Projet - Conteneurisation et Réseau",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {
        "Status": "Succès",
        "Projet": "SDN DevOps",
        "Binôme": "Suvethan & Mattéo",
        "Infrastructure": "Docker sur VM Ubuntu (UTM)",
        "Message": "L'API est parfaitement opérationnelle !"
    }

@app.get("/info")
def get_info():
    return {
        "Python_Version": "3.13",
        "Framework": "FastAPI",
        "Container_User": "app (non-root)",
        "Documentation": "Disponible sur /docs"
    }
