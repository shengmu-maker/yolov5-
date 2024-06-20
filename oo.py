from PIL import Image
import random

# 定义一个函数，用来检查一个位置是否已经有形状图片
def is_occupied(position, old_list):
    for pos in old_list:
        if abs(pos[0] - position[0]) < overlay.size[0] and abs(pos[1] - position[1]) < overlay.size[1]:
            return True
    return False

for i in range(1000):
    old_list = []
    j=0
    z = random.randint(1, 12)
    # 打开背景图片
    bg = Image.open(r"C:\Users\29745\Desktop\blackground\blackgroud ({}).png".format(z))
    bg=bg.resize((4000,4000))

    while j<15:
        # 打开需要合成的透明背景图片
        x, y = random.randint(0, 3600), random.randint(0, 3600)
        z1 = random.randint(1, 36)
        overlay = Image.open(r"C:\Users\29745\Desktop\data\Drawing ({}).png".format(z1))
        angle = random.randint(1, 360)
        overlay = overlay.rotate(angle)

        # 检查这个位置是否已经有形状图片
        if not is_occupied((x, y), old_list):
            bg.paste(overlay, (x, y), overlay)
            old_list.append((x, y))
            j += 1
            print("sdfhhfdas")

    # 保存合成后的图片
    bg.save("D:\pythhon_Test\pythonProject4\pg\combined{}.png".format(i), 'PNG')




