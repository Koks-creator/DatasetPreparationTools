import cv2
import os
from pathlib import Path

def resize_images(input_folder, output_folder, max_dimension=1280, min_dimension=1000):
    """
    Przeskalowuje obrazy, które przekraczają max_dimension na dłuższym boku.
    
    Args:
        input_folder: folder z oryginalnymi obrazami
        output_folder: folder na przeskalowane obrazy
        max_dimension: maksymalny wymiar (dłuższy bok)
        min_dimension: próg, od którego skalujemy
    """
    
    # Tworzenie folderu wyjściowego
    Path(output_folder).mkdir(parents=True, exist_ok=True)
    
    # Obsługiwane formaty
    extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp']
    
    processed = 0
    skipped = 0
    
    for filename in os.listdir(input_folder):
        file_ext = os.path.splitext(filename)[1].lower()
        
        if file_ext not in extensions:
            continue
            
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        
        # Wczytanie obrazu
        img = cv2.imread(input_path)
        
        if img is None:
            print(f"❌ Nie można wczytać: {filename}")
            continue
        
        height, width = img.shape[:2]
        max_current = max(height, width)
        
        # Sprawdzenie czy wymaga przeskalowania
        if max_current <= min_dimension:
            # Kopiowanie bez zmian
            cv2.imwrite(output_path, img)
            skipped += 1
            print(f"⏩ Pominięto (już mały): {filename} ({width}x{height})")
            continue
        
        # Obliczenie nowych wymiarów z zachowaniem proporcji
        if width > height:
            new_width = max_dimension
            new_height = int(height * (max_dimension / width))
        else:
            new_height = max_dimension
            new_width = int(width * (max_dimension / height))
        
        # Przeskalowanie (INTER_AREA najlepsze dla zmniejszania)
        resized = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)
        
        # Zapis
        cv2.imwrite(output_path, resized)
        processed += 1
        
        print(f"Przeskalowano: {filename}")
        print(f"   {width}x{height} → {new_width}x{new_height}")
    
    print(f"Podsumowanie:")
    print(f"   Przeskalowano: {processed}")
    print(f"   Pominięto: {skipped}")

# Użycie
if __name__ == "__main__":
    INPUT_FOLDER = r"C:\Users\table\PycharmProjects\MojeCos\ocr_dwa\train_data\images\train" # Twój folder z obrazami
    OUTPUT_FOLDER = r"C:\Users\table\PycharmProjects\MojeCos\ocr_dwa\train_data\images\train2"   # Folder na przeskalowane
    
    resize_images(INPUT_FOLDER, OUTPUT_FOLDER, max_dimension=1280)
