import qrcode as qr
from PIL import Image
q_code=qr.QRCode(version=1,error_correction=qr.constants.ERROR_CORRECT_H,
                     box_size=20,border=3,)
q_code.add_data("https://github.com/8844sachin ")
q_code.make(fit=True)
img=q_code.make_image(fill_color="red",back_color="black")
img.save("My_qrcode.png")
