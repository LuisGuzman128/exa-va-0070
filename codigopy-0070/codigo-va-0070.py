
# Luis Axel Guzman Martinez NC=0070
# Examen de Vision Artificial
# Objeto: Aspiradora - Numero de lista 27

import cv2
from pathlib import Path

# 1. Definir las rutas de trabajo
carpeta_proyecto = Path(__file__).resolve().parent.parent

ruta_original = (
    carpeta_proyecto
    / "img-original-0070"
    / "aspiradora-27.jpg"
)

carpeta_resultados = (
    carpeta_proyecto / "resultados-img-0070"
)

# 2. Crear la carpeta de resultados
carpeta_resultados.mkdir(parents=True, exist_ok=True)

# 3. Leer la imagen original
img27 = cv2.imread(str(ruta_original))

# 4. Comprobar que la imagen se haya cargado
if img27 is None:
    raise FileNotFoundError(
        f"No se pudo leer la imagen: {ruta_original}"
    )

# 5. Rotar la imagen 90 grados en sentido horario
img90_27 = cv2.rotate(
    img27,
    cv2.ROTATE_90_CLOCKWISE
)

# 6. Rotar la imagen 45 grados
alto, ancho = img27.shape[:2]
centro = (ancho // 2, alto // 2)

matriz_rotacion = cv2.getRotationMatrix2D(
    centro,
    45,
    1.0
)

img45_27 = cv2.warpAffine(
    img27,
    matriz_rotacion,
    (ancho, alto)
)

# 7. Redimensionar a 600 x 500 pixeles
img600x500_27 = cv2.resize(
    img27,
    (600, 500)
)

# 8. Dibujar un rectangulo rojo sobre una copia
img_rojo_27 = img27.copy()

cv2.rectangle(
    img_rojo_27,
    (50, 50),
    (150, 250),
    (0, 0, 255),
    3
)

# 9. Mostrar las cinco imagenes
cv2.imshow("Aspiradora original 27", img27)

cv2.imshow(
    "Aspiradora 90 grados 0070",
    img90_27
)

cv2.imshow(
    "Aspiradora 45 grados 0070",
    img45_27
)

cv2.imshow(
    "Aspiradora 600x500 0070",
    img600x500_27
)

cv2.imshow(
    "Aspiradora rectangulo rojo 0070",
    img_rojo_27
)

# 10. Guardar las cuatro imagenes procesadas
cv2.imwrite(
    str(carpeta_resultados / "aspiradora1-27.jpg"),
    img90_27
)

cv2.imwrite(
    str(carpeta_resultados / "aspiradora2-27.jpg"),
    img45_27
)

cv2.imwrite(
    str(carpeta_resultados / "aspiradora3-27.jpg"),
    img600x500_27
)

cv2.imwrite(
    str(carpeta_resultados / "aspiradora4-27.jpg"),
    img_rojo_27
)

# 11. Finalizar el programa
print("Imagenes procesadas y guardadas.")
print("Presiona una tecla en una ventana para finalizar.")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Programa realizado por Axel Guzman 0070")
