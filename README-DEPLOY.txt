HAI DUONG MARITIME - TOI UU TOC DO TAI TRANG
============================================
index.html        V1.4.1
open-tonnage.html V1.3.1

THAY DOI
--------
- Go toan bo anh base64 khoi HTML: index.html tu 583 KB xuong 46 KB
- Anh chuyen sang thu muc images/ (nen lai tu file goc)
- Logo va icon roi Cloudinary, ve GitHub -> khong con phu thuoc dich vu
  ngoai, an toan cho khach o Trung Quoc
- Them width/height cho moi <img> -> khong con nhay layout khi tai
- Manifest PWA dung URL tuyet doi cho icon (Blob URL khong resolve
  duoc duong dan tuong doi)
- Bo user-scalable=no -> nguoi dung phong to duoc trang tren dien thoai

VE width/height TREN THE <img>
------------------------------
Hai thuoc tinh nay KHONG ep kich thuoc anh va khong lam cat anh.
CSS luon thang thuoc tinh HTML:
  .about-img-item img { width: 100%; height: auto; }
  logo: style="height:60px;width:auto"
Chung chi bao truoc TI LE KHUNG HINH de trinh duyet chua san cho,
tranh nhay layout khi anh tai xong. Gia tri dat dung bang pixel that
cua tung file.
QUAN TRONG: neu thay anh trong images/ bang anh ti le khac, phai sua
hai con so nay cho khop - hoac xoa han chung di cung duoc.

FILE CAN PUSH
-------------
  index.html                    ghi de
  open-tonnage.html             ghi de
  images/                       THU MUC MOI - push ca thu muc
    hero.jpg              139 KB   anh nen trang chu (MV Hai Duong 68)
    mv-36.jpg             117 KB   muc About
    mv-09.jpg             150 KB   muc About
    logo.png                9 KB   navbar + favicon
    icon-512.png           34 KB   PWA + og:image cho mang xa hoi
    icon-192.png            7 KB   PWA
    apple-touch-icon.png    6 KB   iOS Add to Home Screen

KHONG DUNG DEN: open-tonnage.json (Action tu quan ly - dung ghi de)

SAU KHI PUSH
------------
1. Kiem tra anh hien day du o trang chu va trang open tonnage
2. Chay lai https://pagespeed.web.dev/ - Performance nen tang dang ke
3. Neu anh khong hien: kiem tra thu muc images/ da len GitHub chua

DOI ANH SAU NAY
---------------
Thay file trong images/ giu nguyen ten la xong, khong phai sua HTML.
Nen resize truoc: hero 1600px rong, anh About 1200px rong, chat luong 72-82.

Developed by Pavel Hai
