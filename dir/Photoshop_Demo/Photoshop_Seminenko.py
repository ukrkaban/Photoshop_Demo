import os

from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QLabel, QPushButton, QListWidget, QHBoxLayout, \
    QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from PIL import Image
from PIL.ImageFilter import BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE, EMBOSS, FIND_EDGES, SMOOTH, \
    SMOOTH_MORE, SHARPEN, GaussianBlur, UnsharpMask


class ImageProcessor:
    """Class ImageProcessor represents an object used for image editing."""
    def __init__(self):
        """Constructor"""
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modified/"

    def load_image(self, filename):
        """When downloading, remember the path and name of the file """
        self.filename = filename
        fullname = os.path.join(workdir, filename)
        self.image = Image.open(fullname)

    def save_image(self):
        """Saves a copy of the file in a folder"""
        path = os.path.join(workdir, self.save_dir)
        if not (os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        fullname = os.path.join(path, self.filename)
        self.image.save(fullname)

    def __save_show_image(self):
        """Private saves a copy of the file"""
        self.save_image()
        self.show_image(os.path.join(workdir, self.save_dir, self.filename))

    def do_b_w(self):
        """Function filter"""
        self.image = self.image.convert("L")
        self.__save_show_image()

    def turn_left(self):
        """Filter for left"""
        self.image = self.image.transpose(Image.ROTATE_90)
        self.__save_show_image()

    def turn_right(self):
        """Filter for right"""
        self.image = self.image.transpose(Image.ROTATE_270)
        self.__save_show_image()

    def do_flip(self):
        """Filter for flip"""
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.__save_show_image()

    def do_blur(self):
        """Filter for blur"""
        self.image = self.image.filter(BLUR)
        self.__save_show_image()

    def do_sharpen(self):
        """Filter for sharpen"""
        self.image = self.image.filter(SHARPEN)
        self.__save_show_image()

    def do_contour(self):
        """Filter for contour"""
        self.image = self.image.filter(CONTOUR)
        self.__save_show_image()

    def do_detail(self):
        """Filter for detail"""
        self.image = self.image.filter(DETAIL)
        self.__save_show_image()

    def do_edge_enhance(self):
        """Filter for edge enhance"""
        self.image = self.image.filter(EDGE_ENHANCE)
        self.__save_show_image()

    def do_edge_enhance_more(self):
        """Filter for edge enhance more"""
        self.image = self.image.filter(EDGE_ENHANCE_MORE)
        self.__save_show_image()

    def do_emboss(self):
        """Filter for emboss"""
        self.image = self.image.filter(EMBOSS)
        self.__save_show_image()

    def do_find_edges(self):
        """Filter for find edges"""
        self.image = self.image.filter(FIND_EDGES)
        self.__save_show_image()

    def do_smooth(self):
        """Filter for smooth"""
        self.image = self.image.filter(SMOOTH)
        self.__save_show_image()

    def do_smooth_more(self):
        """Filter for smooth more"""
        self.image = self.image.filter(SMOOTH_MORE)
        self.__save_show_image()

    def do_gaussian_blur(self):
        """Filter for gaussian blur"""
        self.image = self.image.filter(GaussianBlur)
        self.__save_show_image()

    def do_unsharp_mask(self):
        """Filter for unsharp mask"""
        self.image = self.image.filter(UnsharpMask)
        self.__save_show_image()

    def show_image(self, path):
        """Function for show image"""
        lb_image.hide()
        pixmap_image = QPixmap(path)
        w, h = lb_image.width(), lb_image.height()
        pixmap_image = pixmap_image.scaled(w, h, Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmap_image)
        lb_image.show()


def choose_workdir():
    """Function to choose the directory"""
    global workdir
    workdir = QFileDialog.getExistingDirectory()


def show_filenames_list():
    """Function to show filenames list"""
    extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    choose_workdir()
    filenames = filter_image(os.listdir(workdir), extensions)
    lw_files.clear()
    for filename in filenames:
        lw_files.addItem(filename)


def show_сhosen_іmage():
    """Function to display show chosen files"""
    if lw_files.currentRow() >= 0:
        filename = lw_files.currentItem().text()
        workimage.load_image(filename)
        workimage.show_image(os.path.join(workdir, workimage.filename))


def filter_image(files, extensions):
    """Function to filter"""
    return [filename for filename in files for ext in extensions if filename.endswith(ext)]


def show_info():
    """Function to display information"""
    my_info = QMessageBox()
    my_info.setText('DemoPhotoshop!\nVer.1.0')
    my_info.exec_()


app = QApplication([])
win = QWidget()
win.resize(1200, 800)
win.setWindowTitle('Photoshop')
lb_image = QLabel("Зображення")

lb_image.setAlignment(Qt.AlignCenter)
btn_dir = QPushButton("Директорія")
lw_files = QListWidget()

btn_left = QPushButton("Left")
btn_right = QPushButton("Right")
btn_flip = QPushButton("Flip")
btn_sharpen = QPushButton("Sharp")
btn_b_w = QPushButton("B/W")
btn_blur = QPushButton("Blur")
btn_contour = QPushButton("Contour")
btn_detail = QPushButton("Detail")

btn_edge_enhance = QPushButton("Edge_enhance")
btn_edge_enhance_more = QPushButton("Edge_enhance_more")
btn_emboss = QPushButton("Emboss")
btn_find_edges = QPushButton("Find_edges")
btn_smooth = QPushButton("Smooth")
btn_smooth_more = QPushButton("Smooth_more")
btn_gaussian_blur = QPushButton("Gaussian_Blur")
btn_unsharp_mask = QPushButton("Unsharp_Mask")

btn_info = QPushButton('INFO')


row = QHBoxLayout()

col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(btn_dir)
col1.addWidget(lw_files)

col2.addWidget(lb_image, 95)
col2.addWidget(btn_info)

row_tools1 = QHBoxLayout()
row_tools1.addWidget(btn_left)
row_tools1.addWidget(btn_right)
row_tools1.addWidget(btn_flip)
row_tools1.addWidget(btn_sharpen)
row_tools1.addWidget(btn_b_w)
row_tools1.addWidget(btn_blur)
row_tools1.addWidget(btn_contour)
row_tools1.addWidget(btn_detail)

row_tools2 = QHBoxLayout()
row_tools2.addWidget(btn_edge_enhance)
row_tools2.addWidget(btn_edge_enhance_more)
row_tools2.addWidget(btn_emboss)
row_tools2.addWidget(btn_find_edges)
row_tools2.addWidget(btn_smooth)
row_tools2.addWidget(btn_smooth_more)
row_tools2.addWidget(btn_gaussian_blur)
row_tools2.addWidget(btn_unsharp_mask)

col2.addLayout(row_tools1)
col2.addLayout(row_tools2)

row.addLayout(col1, 20)
row.addLayout(col2, 80)
win.setLayout(row)

win.show()

btn_dir.clicked.connect(show_filenames_list)

workdir = ''
workimage = ImageProcessor()

lw_files.currentRowChanged.connect(show_сhosen_іmage)

btn_b_w.clicked.connect(workimage.do_b_w)
btn_left.clicked.connect(workimage.turn_left)
btn_right.clicked.connect(workimage.turn_right)
btn_sharpen.clicked.connect(workimage.do_sharpen)
btn_flip.clicked.connect(workimage.do_flip)
btn_blur.clicked.connect(workimage.do_blur)
btn_contour.clicked.connect(workimage.do_contour)
btn_detail.clicked.connect(workimage.do_detail)

btn_edge_enhance.clicked.connect(workimage.do_edge_enhance)
btn_edge_enhance_more.clicked.connect(workimage.do_edge_enhance_more)
btn_emboss.clicked.connect(workimage.do_emboss)
btn_find_edges.clicked.connect(workimage.do_find_edges)
btn_smooth.clicked.connect(workimage.do_smooth)
btn_smooth_more.clicked.connect(workimage.do_smooth_more)
btn_gaussian_blur.clicked.connect(workimage.do_gaussian_blur)
btn_unsharp_mask.clicked.connect(workimage.do_unsharp_mask)

btn_info.clicked.connect(show_info)

app.exec_()
