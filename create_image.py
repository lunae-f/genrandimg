import sys
import os
from PIL import Image
import numpy as np

# デフォルトの画像サイズ
DEFAULT_WIDTH = 8
DEFAULT_HEIGHT = 8
width, height = DEFAULT_WIDTH, DEFAULT_HEIGHT
file_name = None

try:
    num_args = len(sys.argv)

    if num_args == 1:
        # 引数なし -> デフォルト設定
        print(f"ℹ️ No arguments provided; generating with default size: {width}x{height}.")

    elif num_args == 2:
        # 幅のみ指定 -> 高さは幅と同じ、ファイル名は自動生成
        width = int(sys.argv[1])
        height = width
        print(f"ℹ️ Generating with specified size: {width}x{height}.")

    elif num_args == 4:
        # 幅、高さ、ファイル名を指定
        width = int(sys.argv[1])
        height = int(sys.argv[2])
        # ファイル名からディレクトリ部分を取り除く
        file_name = os.path.basename(sys.argv[3])
        print(f"ℹ️ Generating with specified size: {width}x{height}, filename: '{file_name}'.")

    else:
        # それ以外の引数の数はエラー
        print("⚠️ Error: Incorrect number of arguments.")
        sys.exit(1)

except ValueError:
    print("⚠️ Error: Please provide width and height as integers.")
    sys.exit(1)

# ファイル名が指定されていない場合は、サイズから自動生成
if file_name is None:
    file_name = f'random_color_image_{width}x{height}.png'

# ファイル名に .png がなければ追加
if not file_name.lower().endswith('.png'):
    file_name += '.png'

# NumPyを使ってランダムな色の配列を生成
random_pixels = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

# NumPy配列からPillowの画像オブジェクトを生成
image = Image.fromarray(random_pixels, 'RGB')

# 画像を保存
image.save(file_name)

print(f"✅ Image saved as '{file_name}'.")