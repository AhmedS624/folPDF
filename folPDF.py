import os
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tqdm import tqdm

def create_pdf(main_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through each folder in the main directory
    for secondary_folder in os.listdir(main_folder):
        secondary_folder_path = os.path.join(main_folder, secondary_folder)
        
        # Only process secondary folders, ignore files
        if os.path.isdir(secondary_folder_path):
            # Iterate through each folder in the secondary directory
            for folder_name in os.listdir(secondary_folder_path):
                folder_path = os.path.join(secondary_folder_path, folder_name)
                
                # Only process folders, ignore files
                if os.path.isdir(folder_path):
                    # Create a new PDF
                    pdf_path = os.path.join(output_folder, f"{folder_name}.pdf")
                    c = canvas.Canvas(pdf_path)
                    
                    # Get all image files in the current folder
                    image_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.PNG') or f.endswith('.JPG') or f.endswith ('.jpeg')]
                    image_files.sort()  # Sort files alphabetically
                    image_files.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))
                    
                    # Create a tqdm progress bar
                    progress_bar = tqdm(image_files, desc=f"Creating PDF for {folder_name}", unit="image")
                    
                    # Add each image to the PDF
                    for image_file in progress_bar:
                        image_path = os.path.join(folder_path, image_file)
                        img = Image.open(image_path)
                        img_width, img_height = img.size
                        
                        # Set canvas size to match image size
                        c.setPageSize((img_width, img_height))
                        
                        # Add the image to the PDF
                        c.drawImage(image_path, 0, 0)
                        c.showPage()
                    
                    # Save the PDF
                    c.save()

if __name__ == "__main__":
    # Specify the main folder containing secondary folders with image folders
    main_folder = "/home/hamada/Downloads/input/Stuff"
    
    # Specify the output folder where PDFs will be saved
    output_folder = "/home/hamada/Downloads/Documents/output"
    
    create_pdf(main_folder, output_folder)

