from gfpgan import GFPGANer
from config import CONFIG

class ImageEhancer:

    def __init__(self):
        self.model = None

    def load_model_simple(self):
        model = GFPGANer(
            model_path=CONFIG["model_url"],
            upscale=CONFIG["upscale"],
            arch=CONFIG["arch"],
            channel_multiplier=CONFIG["chanel_multiplier"],
            bg_upsampler=None
        )
        return model
    
    def enhance(self, image_bgr):
        """
        Mejora una imagen con opciones configurables.
        
        Args:
            image_bgr: Imagen en formato BGR
        """

        if not self.model:
            self.model = self.load_model_simple()

        _, _, restored_img = self.model.enhance(
            image_bgr,
            has_aligned=False,
            only_center_face=False,
            paste_back=True,
            weight=CONFIG["enhancement_weight"]
        )

        return restored_img