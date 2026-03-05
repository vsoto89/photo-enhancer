from src.models import ImageEhancer
from src.utils import pil_to_bgr, bgr_to_pil, load_image

def main():
    with open("E:\\OneDrive - Corporación Santo Tomas\\Mio\\Cursos Udemy\\Python\\curso_python\\Tema_6\\photo-enhancer\\imagen1.jpg", "rb") as f:
        image_pil = load_image(f)
    
    image_bgr = pil_to_bgr(image_pil)

    enhancer = ImageEhancer()
    restored_bgr = enhancer.enhance(image_bgr)

    restored_pil = bgr_to_pil(restored_bgr)

    restored_pil.save("E:\\OneDrive - Corporación Santo Tomas\\Mio\\Cursos Udemy\\Python\\curso_python\\Tema_6\\photo-enhancer\\imagen_restaurada.jpg")

if __name__ == "__main__":
    main()