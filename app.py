import os
from PIL import Image

def batch_resize_images(input_path, output_path, size, file_format):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    try:
        files = os.listdir(input_path)
    except FileNotFoundError:
        print(f"Error: The folder '{input_path}' was not found. Please check the path and try again.")
        return
    except NotADirectoryError:
        print(f"Error: The path '{input_path}' is a file, not a folder. Please enter a folder path.")
        return

    image_files = [f for f in files if os.path.isfile(os.path.join(input_path, f))]

    if not image_files:
        print(f"No image files found in '{input_path}'.")
        return

    for i, filename in enumerate(image_files):
        input_filepath = os.path.join(input_path, filename)
        file_basename, _ = os.path.splitext(filename)
        output_filepath = os.path.join(output_path, f"{file_basename}_resized.{file_format.lower()}")

        try:
            with Image.open(input_filepath) as img:
                resized_img = img.resize(size)
                
                if file_format.upper() == 'JPEG':
                    resized_img = resized_img.convert('RGB')
                
                resized_img.save(output_filepath, format=file_format)
                print(f"({i+1}/{len(image_files)}) Resized {filename} -> {os.path.basename(output_filepath)}")

        except (IOError, SyntaxError, Image.UnidentifiedImageError):
            print(f"Skipping {filename}: Not a valid image file.")

if __name__ == "__main__":
    new_size = (800, 600)
    output_format = 'JPEG'
    output_folder_name = 'resized'
    
    input_folder = input("Enter the path to the folder containing your images: ").strip()

    if input_folder:
        output_folder = os.path.join(input_folder, output_folder_name)
    
        batch_resize_images(
            input_path=input_folder,
            output_path=output_folder,
            size=new_size,
            file_format=output_format
        )
        print(f"\n✅ Batch resizing complete! Resized images are in: {output_folder}")
    else:
        print("No input folder provided. Exiting.")