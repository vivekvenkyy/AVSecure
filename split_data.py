import os
import shutil
import random

def split_data(source_dir, base_dir, split_ratios=(0.7, 0.15, 0.15)):
    """
    Splits the data from source_dir into train, validation, and test sets
    and saves them in base_dir.
    """
    if os.path.exists(base_dir):
        shutil.rmtree(base_dir)
        print(f"Removed existing directory: {base_dir}")

    # Create directories
    train_dir = os.path.join(base_dir, 'train')
    validation_dir = os.path.join(base_dir, 'validation')
    test_dir = os.path.join(base_dir, 'test')

    os.makedirs(train_dir)
    os.makedirs(validation_dir)
    os.makedirs(test_dir)

    print(f"Created new directory structure at: {base_dir}")

    # Iterate over each class in the source directory
    for class_name in os.listdir(source_dir):
        class_path = os.path.join(source_dir, class_name)
        if not os.path.isdir(class_path):
            continue

        # Create class subdirectories in train, validation, and test
        os.makedirs(os.path.join(train_dir, class_name))
        os.makedirs(os.path.join(validation_dir, class_name))
        os.makedirs(os.path.join(test_dir, class_name))

        # Get all image filenames and shuffle them
        images = os.listdir(class_path)
        random.shuffle(images)

        # Calculate split points
        train_split = int(len(images) * split_ratios[0])
        validation_split = int(len(images) * (split_ratios[0] + split_ratios[1]))

        # Slice the list of images for each set
        train_images = images[:train_split]
        validation_images = images[train_split:validation_split]
        test_images = images[validation_split:]

        # Copy files to new directories
        for img in train_images:
            shutil.copy(os.path.join(class_path, img), os.path.join(train_dir, class_name))
        for img in validation_images:
            shutil.copy(os.path.join(class_path, img), os.path.join(validation_dir, class_name))
        for img in test_images:
            shutil.copy(os.path.join(class_path, img), os.path.join(test_dir, class_name))
        
        print(f"Class '{class_name}': {len(train_images)} train, {len(validation_images)} val, {len(test_images)} test")

    print("\nDataset splitting complete!")

# --- CONFIGURATION ---
# IMPORTANT: Update these paths
SOURCE_DIR = "ITS Dataset"
BASE_DIR = "split_dataset" # Where the train/val/test folders will be created
# ---------------------

if __name__ == '__main__':
    split_data(SOURCE_DIR, BASE_DIR)