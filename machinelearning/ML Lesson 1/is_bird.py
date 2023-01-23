from fastai.vision.all import *
import matplotlib.pyplot as plt

# turn on interactive mode, otherwise pyplot.show blocks until the window is closed
plt.ion()

# display a bird
dest = 'bird.jpg'
im = Image.open(dest)
im.to_thumb(256,256)
# plt.imshow(im)
# plt.waitforbuttonpress()

# and a forest, this time in a single line
Image.open('forest.jpg').to_thumb(256,256)
# plt.imshow(im)
# plt.waitforbuttonpress()

# The interesting part! Training our model.  Images are in bird_or_not/bird, # and bird_or_not/forest.
path = Path('bird_or_not')

# create a DataBlock to train with
dls = DataBlock(
    blocks=(ImageBlock, CategoryBlock), 
    get_items=get_image_files, 
    splitter=RandomSplitter(valid_pct=0.2, seed=42),
    get_y=parent_label,
    item_tfms=[Resize(192, method='squish')]
).dataloaders(path, bs=32, num_workers=0)

# Here what each of the `DataBlock` parameters means:
# 
#     blocks=(ImageBlock, CategoryBlock),
# 
# The inputs to our model are images, and the outputs are categories (in this case, "bird" or "forest").
# 
#     get_items=get_image_files, 
# 
# To find all the inputs to our model, run the `get_image_files` function (which returns a list of all image files in a path).
# 
#     splitter=RandomSplitter(valid_pct=0.2, seed=42),
# 
# Split the data into training and validation sets randomly, using 20% of the data for the validation set.
# 
#     get_y=parent_label,
# 
# The labels (`y` values) is the name of the `parent` of each file (i.e. the name of the folder they're in, which will be *bird* or *forest*).
# 
#     item_tfms=[Resize(192, method='squish')]
# 
# Before training, resize each image to 192x192 pixels by "squishing" it (as opposed to cropping it).
#
#     bs=32
#
# Use a batch size of 32 images, this should be small enough even for underpowered machines.
#
#     num_workers=0
#
# Don't spawn extra worker processes, this doesn't work well on Windows.

# show a sample from the DataBlock
dls.show_batch(max_n=6)
plt.show()
plt.waitforbuttonpress()

# Now we're ready to train our model. The fastest widely used computer vision model is `resnet18`. You can train this in a few minutes, even on a CPU! (On a GPU, it generally takes under 10 seconds...)
# 
# `fastai` comes with a helpful `fine_tune()` method which automatically uses best practices for fine tuning a pre-trained model, so we'll use that.
learn = vision_learner(dls, resnet18, metrics=error_rate)
learn.fine_tune(3)

# now predict what category our example images belong to!
for fname in ['bird.jpg', 'forest.jpg']:
    category,index,probs = learn.predict(PILImage.create(fname))
    print(f"{fname} is a: {category} with confidence level: {probs[index]:.4f}")
