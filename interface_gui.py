import tkinter as tk
from tkinter import filedialog, messagebox
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.fft import fft2, ifft2, fftshift
from scipy.ndimage import maximum_filter, minimum_filter


class ImageProcessingApp:
    def __init__(self,root):
        self.root = root
        self.root.title("SIN 392 - Processamento Digital de Imagens")
        self.root.geometry("900x700")
        self.style = ttkb.Style(theme="vapor")

        # Armazena a imagem original e processada
        self.image = None
        self.processed_image = None
        self.photo = None
        self.image_array = None

        # Criar menu
        self.menu_bar = ttkb.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Menu do arquivo
        self.file_menu = ttkb.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Arquivo", menu=self.file_menu)
        self.file_menu.add_command(label="Carregar Imagem", command=self.load_image)
        self.file_menu.add_command(label="Salvar Imagem", command=self.save_image)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Sair", command=self.root.quit)

        self.main_frame = ttkb.Frame(self.root, padding=10)
        self.main_frame.pack(fill=BOTH, expand=True)

        # Painel para botões de funcionalidade
        self.button_frame = ttkb.LabelFrame(self.main_frame, text="Funcionalidades", padding=10)
        self.button_frame.pack(side=TOP, fill=X, padx=5, pady=5)

        # Botões de cada funcionalidade
        self.create_function_buttons()

        # Label para Status
        self.status_label = ttkb.Label(self.main_frame, text="Nenhuma imagem carregada", bootstyle = INFO)
        self.status_label.pack(side=TOP, pady=5)

        # Área para exibir a imagem
        self.image_frame = ttkb.LabelFrame(self.main_frame, text="Imagem", padding=5)
        self.image_frame.pack(fill=BOTH, expand=True, padx=5, pady=5)
        self.image_label = ttkb.Label(self.image_frame)
        self.image_label.pack(expand=True)

    # Botões para as funções
    def create_function_buttons(self):
        buttons = [
            ("Histograma", self.show_histogram),
            ("Alargamento de Contraste", self.contrast_stretching),
            ("Equalização de Histograma", self.histogram_equalization),
            ("Filtro Média", self.mean_filter),
            ("Filtro Mediana", self.median_filter),
            ("Filtro Gaussiano", self.gaussian_filter),
            ("Filtro Máximo", self.max_filter),
            ("Filtro Mínimo", self.min_filter),
            ("Filtro Laplaciano", self.laplacian_filter),
            ("Filtro Roberts", self.roberts_filter),
            ("Filtro Prewitt", self.prewitt_filter),
            ("Filtro Sobel", self.sobel_filter),
            ("Convolução Passa-Baixa", self.low_pass_convolution),
            ("Convolução Passa-Alta", self.high_pass_convolution),
            ("Espectro de Fourier", self.fourier_spectrum),
            ("Erosão", self.erosion),
            ("Dilatação", self.dilation),
            ("Segmentação Otsu", self.otsu_segmentation)
        ]

        for idx, (text, command) in enumerate (buttons):
            btn = ttkb.Button(self.button_frame, text=text, command=command, bootstyle=PRIMARY)
            btn.grid(row=idx // 4, column=idx % 4, padx=5, pady= 5, sticky="ew")
        for i in range(4):
            self.button_frame.grid_columnconfigure(i, weight=1)
    
    # Carrega a imagem, converte para níveis de cinza e redimensiona
    def load_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files","*.png *.jpg *.jpeg *.bmp")]
        )
        if file_path:
            try:
                self.image = Image.open(file_path)
                if self.image.mode == "RGB":
                    self. image = self.image.convert("L")
                self.processed_image = self.image.copy()
                self.image_array = np.array(self.image)
                self.display_image(self.image)
                self.status_label.config(text="Imagem carregada com sucesso", bootstyle=SUCCESS)
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao carregar a imagem: {e}")
                self.status_label.config(text="Erro ao carregar imagem", bootstyle=DANGER)
    
    # Redimensiona a imagem para exibição
    def display_image(self,image):
        max_size = (600,400)
        image.thumbnail(max_size, Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=self.photo)
        self.image_label.image = self.photo

    # Salvar imagem
    def save_image(self):
        if self.processed_image is None:
            messagebox.showwarning("Aviso", "Nenhuma imagem pra salvar")
            self.status_label.config(text="Nenhuma imagem para salvar", bootstyle=WARNING)
            return
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG","*.png"),("JPEG","*.jpg")]
        )
        if file_path:
            try:
                self.processed_image.save(file_path)
                messagebox.showinfo("Sucesso", "Imagem salva com sucesso!")
                self.status_label.config(text="Imagem salva com sucesso", bootstyle=SUCCESS)
            except Exception as e:
                messagebox.showerror("Erro",f"Erro ao salvar a imagem: {e}")
                self.status_label.config(text="Erro ao salvar imagem", bootstyle=DANGER)

    # Métodos placeholders para as funcionalidades
    def show_histogram(self):
        if self.image_array is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        plt.figure(figsize=(9,5))
        plt.hist(self.image_array.ravel(), bins=256, range=(0,255), color='gray', alpha=0.7)
        plt.title("Histograma de Imagem")
        plt.xlabel("Intensidade")
        plt.ylabel("Frequência")
        plt.grid(True, alpha=0.3)
        plt.show()
        self.status_label.config(text="Histograma Exibido", bootstyle=INFO)
    
    def contrast_stretching(self):
        if self.image_array is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        min_val = np.min(self.image_array)
        max_val = np.max(self.image_array)
        stretched = 255 * (self.image_array - min_val) / (max_val - min_val + 1e-6)
        self.processed_image = Image.fromarray(stretched.astype(np.uint8))
        self.display_image(self.processed_image)
        self.status_label.config(text="Alargamento de Contraste aplicado", bootstyle=SUCCESS)
    
    def histogram_equalization(self):
        if self.image_array is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        equalized = cv2.equalizeHist(self.image_array)
        self.processed_image = Image.fromarray(equalized)
        self.display_image(self.processed_image)
        self.status_label.config(text="Equalização de Histograma aplicada", bootstyle=SUCCESS)
        
    def mean_filter(self):
        if self.image_array is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        blurred = cv2.blur(self.image_array, (5,5))
        self.processed_image = Image.fromarray(blurred)
        self.display_image(self.processed_image)
        self.status_label.config(text="Filtro Média aplicado", bootstyle=SUCCESS)
        
    def median_filter(self):
        if self.image_array is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        blurred = cv2.medianBlur(self.image_array, 5)
        self.processed_image = Image.fromarray(blurred)
        self.display_image(self.processed_image)
        self.status_label.config(text="Filtro Mediana aplicado", bootstyle=SUCCESS)

    def gaussian_filter(self):
        if self.image_array is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        blurred = cv2.GaussianBlur(self.image_array, (5,5), 0)
        self.processed_image = Image.fromarray(blurred)
        self.display_image(self.processed_image)
        self.status_label.config(text="Filtro Gaussiano aplicado", bootstyle=SUCCESS)
     
    def max_filter(self):
        if self.image_array is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        filtered = maximum_filter(self.image_array, size=3)
        self.processed_image = Image.fromarray(filtered)
        self.display_image(self.processed_image)
        self.status_label.config(text="Filtro Máximo aplicado", bootstyle=SUCCESS)

    def min_filter(self):
        if self.image_array is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        filtered = minimum_filter(self.image_array,size=3)
        self.processed_image = Image.fromarray(filtered)
        self.display_image(self.processed_image)
        self.status_label.config(text="Filto Mínimo aplicado", bootstyle=SUCCESS)
      
    def laplacian_filter(self):
        if self.image_array is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        laplacian = cv2.Laplacian(self.image_array, cv2.CV_64F)
        laplacian = np.uint8(np.absolute(laplacian))
        self.processed_image = Image.fromarray(laplacian)
        self.display_image(self.processed_image)
        self.status_label.config(text="Filtro Laplaciano aplicado", bootstyle=SUCCESS)      

    def roberts_filter(self):
        if self.image_array is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        kernel_x = np.array([[1, 0], [0, -1]])
        kernel_y = np.array([[0, 1], [-1, 0]])
        grad_x = cv2.filter2D(self.image_array, -1, kernel_x)
        grad_y = cv2.filter2D(self.image_array, -1, kernel_y)
        roberts = np.sqrt(grad_x**2 + grad_y**2)
        roberts = np.uint8(roberts)
        self.processed_image = Image.fromarray(roberts)
        self.display_image(self.processed_image)
        self.status_label.config(text="Filtro Roberts aplicado", bootstyle=SUCCESS)
           
    def prewitt_filter(self):
        if self.image_array is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
        kernel_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
        grad_x = cv2.filter2D(self.image_array, -1, kernel_x)
        grad_y = cv2.filter2D(self.image_array, -1, kernel_y)
        prewitt = np.sqrt(grad_x**2 + grad_y**2)
        prewitt = np.uint8(prewitt)
        self.processed_image = Image.fromarray(prewitt)
        self.display_image(self.processed_image)
        self.status_label.config(text="Filtro Prewitt aplicado", bootstyle=SUCCESS)    

    def sobel_filter(self):
        if self.image_array is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        grad_x = cv2.Sobel(self.image_array, cv2.CV_64F, 1, 0, ksize=3)
        grad_y = cv2.Sobel(self.image_array, cv2.CV_64F, 0, 1, ksize=3)
        sobel = np.sqrt(grad_x**2 + grad_y**2)
        sobel = np.uint8(sobel)
        self.processed_image = Image.fromarray(sobel)
        self.display_image(self.processed_image)
        self.status_label.config(text="Filtro Sobel aplicado", bootstyle=SUCCESS)

    def low_pass_convolution(self):
        if self.image_array is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        f = fft2(self.image_array)
        fshift = fftshift(f)
        rows, cols = self.image_array.shape
        crow, ccol = rows // 2, cols // 2
        d = 30
        mask = np.zeros((rows,cols), np.uint8)
        for i in range(rows):
            for j in range(cols):
                if np.sqrt((i - crow)**2 + (j- ccol)**2) < d:
                    mask[i, j] = 1
        fshift = fshift * mask
        f_ishift = np.fft.ifftshift(fshift)
        img_back = ifft2(f_ishift)
        img_back = np.abs(img_back)
        img_back = np.uint8(img_back)
        self.processed_image = Image.fromarray(img_back)
        self.display_image(self.processed_image)
        self.status_label.config(text="Convolução Passa-Baixa aplicada", bootstyle=SUCCESS)


    def high_pass_convolution(self):
        if self.image_array is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        f = fft2(self.image_array)
        fshift = fftshift(f)
        rows, cols = self.image_array.shape
        crow, ccol = rows // 2, cols // 2
        d = 30
        mask = np.ones((rows, cols), np.uint8)
        for i in range(rows):
            for j in range(cols):
                if np.sqrt((i - crow)**2 + (j - ccol)**2) < d:
                    mask[i, j] = 0
        fshift = fshift * mask
        f_ishift = np.fft.ifftshift(fshift)
        img_back = ifft2(f_ishift)
        img_back = np.abs(img_back)
        img_back = np.uint8(img_back)
        self.processed_image = Image.fromarray(img_back)
        self.display_image(self.processed_image)
        self.status_label.config(text="Convolução Passa-Alta aplicado", bootstyle=SUCCESS)

    def fourier_spectrum(self):
        if self.image_array is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        f = fft2(self.image_array)
        fshift = fftshift(f)
        magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1e-6)
        plt.figure(figsize=(8,6))
        plt.imshow(magnitude_spectrum, cmap='gray')
        plt.title("Espectro de Fourier")
        plt.colorbar()
        plt.show()
        self.status_label.config(text="Espectro de Fourier exibido", bootstyle=INFO)
        
    def erosion(self):
        if self.image_array is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        kernel = np.ones((3, 3), np.uint8)
        eroded = cv2.erode(self.image_array, kernel, iterations=5)
        self.processed_image = Image.fromarray(eroded)
        self.display_image(self.processed_image)
        self.status_label.config(text="Erosão aplicada", bootstyle=SUCCESS)

    def dilation(self):
        if self.image_array is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        kernel = np.ones((3,3), np.uint8)
        dilated = cv2.dilate(self.image_array, kernel, iterations=5)
        self.processed_image = Image.fromarray(dilated)
        self.display_image(self.processed_image)
        self.status_label.config(text="Dilatação aplicada", bootstyle=SUCCESS)    

    def otsu_segmentation(self):
        if self.image_array is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        _, segmented = cv2.threshold(self.image_array, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        self.processed_image = Image.fromarray(segmented)
        self.display_image(self.processed_image)
        self.status_label.config(text="Segmentação Otsu aplicada", bootstyle=SUCCESS)

if __name__ == "__main__":
    root = ttkb.Window()
    app = ImageProcessingApp(root)
    root.mainloop()

    








