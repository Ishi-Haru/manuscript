from PIL import Image
import os

base = os.path.dirname(os.path.abspath(__file__))
files = [
    'TOC.png', 'mapping_results.png', 'mapping_colormaps.png',
    'HOPG_strong_force.png', 'schematics_of_measurement.png', 'scaling_result.png', 'DLC_bubble.png'
]

for fname in files:
    path = os.path.join(base, fname)
    img = Image.open(path).convert('RGBA')
    bg = Image.new('RGB', img.size, (255, 255, 255))
    bg.paste(img, mask=img.split()[3])  # アルファチャンネルをマスクとして白背景に合成
    bg.save(path)
    print(f'Done: {fname}')

print('All done.')
