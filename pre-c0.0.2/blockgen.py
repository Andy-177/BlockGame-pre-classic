from PIL import Image

class Gen_texture():
    def __init__(self, img1, img2, img3, img4, img5, img6, img_name):
        self.generate_transparent_images('cache/test1.png')
        self.rotate_image(img1, 'cache/test2.png')
        self.rotate_image(img3, 'cache/test3.png')
        self.rotate_image(img5, 'cache/test4.png')
        self.rotate_image(img6, 'cache/test5.png')
        self.vertical_concat_images(
            'cache/test1.png',
            img2,
            'cache/test1.png',
            'cache/test1.png',
            'cache/test6.png'
        )
        self.vertical_concat_images(
            'cache/test2.png',
            'cache/test3.png',
            'cache/test4.png',
            'cache/test5.png',
            'cache/test7.png'
        )
        self.vertical_concat_images(
            'cache/test1.png',
            img4,
            'cache/test1.png',
            'cache/test1.png',
            'cache/test8.png'
        )
        self.horizontal_concat_images(
            'cache/test6.png',
            'cache/test7.png',
            'cache/test8.png',
            img_name
        )
    def generate_transparent_images(self, save_path):
        img1 = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
        img1.save(save_path)
    def rotate_image(self, path, save_path):
        img2 = Image.open(path)
        img2 = img2.transpose(Image.ROTATE_270)
        img2.save(save_path)
    def vertical_concat_images(self, path1, path2, path3, path4, save_path):
        img3_1 = Image.open(path1)
        img3_2 = Image.open(path2)
        img3_3 = Image.open(path3)
        img3_4 = Image.open(path4)
        result = Image.new('RGBA', (16,64), (255,255,225,0))
        result.paste(img3_1, (0, 0))
        result.paste(img3_2, (0, 16))
        result.paste(img3_3, (0, 32))
        result.paste(img3_4, (0, 48))
        result.save(save_path)
    def horizontal_concat_images(self, path1, path2, path3, save_path):
        img4_1 = Image.open(path1)
        img4_2 = Image.open(path2)
        img4_3 = Image.open(path3)
        img4_4 = Image.new('RGBA', (8,64), (255,255,225,0))
        result = Image.new('RGBA', (64, 64), (255, 255, 225, 0))
        result.paste(img4_4, (0, 0))
        result.paste(img4_1, (8, 0))
        result.paste(img4_2, (24, 0))
        result.paste(img4_3, (40, 0))
        result.paste(img4_4, (56, 0))
        result.save(save_path)

#img = Gen_texture(
    #'assets/block/grass_side_carried.png',
    #'assets/block/dirt.png',
    #'assets/block/grass_side_carried.png',
    #'assets/block/grass_carried.png',
    #'assets/block/grass_side_carried.png',
    #'assets/block/grass_side_carried.png',
    #'grass_block.png',
#)