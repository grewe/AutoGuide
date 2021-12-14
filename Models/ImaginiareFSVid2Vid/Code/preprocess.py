#code to preprocess val dataset
import os

Basepath = r"/content/drive/MyDrive/imaginaire/dataset/val/images/"
human_instance_maps  = r"/content/drive/My Drive/human_instance_maps/"
poses = r"/content/drive/My Drive/poses"
openpose_root=r"/content/openpose"

for i in os.listdir(Basepath):
  img_dir = os.path.join(Basepath, i)
  newinstance = os.path.join(human_instance_maps, i)
  cmd = r'cd /content/openpose/'
  os.system(cmd)
  command = r"./build/examples/openpose/openpose.bin --display 0 --disable_blending --image_dir %s --write_images %s --face --hand --face_render_threshold 0.1 --hand_render_threshold 0.02 --write_json %s" % (img_dir, img_dir, img_dir)
  var = os.system(command)
  print(var)