HAI DUONG MARITIME - OPEN TONNAGE
=================================
index.html        V1.3.0   (khong doi so voi lan truoc)
open-tonnage.html V1.2.1

THAY DOI LAN NAY
----------------
Bo hoan toan 3 the tau in cung trong HTML. Trang gio hien
skeleton loading roi thay bang du lieu that tu open-tonnage.json.

CAU TRUC - dat tat ca vao GOC repo
----------------------------------
  index.html
  open-tonnage.html
  open-tonnage.json                       <- Action tu ghi de, dung sua tay
  robots.txt
  sitemap.xml
  scripts/build_open_tonnage.py
  .github/workflows/sync-open-tonnage.yml

LUU Y: thu muc ".github" bat dau bang dau cham nen Windows an no.
Bat "Hidden items" trong tab View cua File Explorer neu khong thay.

QUY TRINH HANG NGAY
-------------------
Chi sua Google Sheet. Toi da 20 phut sau web tu doi.
Can gap: tab Actions -> Sync open tonnage -> Run workflow.

LUON BAM "Pull origin" TRONG GITHUB DESKTOP TRUOC KHI COMMIT.
Action tu commit len GitHub nen may ban se bi cham lai neu khong pull.
Khong bao gio sua open-tonnage.json tren may - Google Sheet la nguon duy nhat.

COT TRONG SHEET
---------------
vessel | open_port | open_date | last_cargoes | note | status | updated
open_date: 2026-08-14 -> hien "14 Aug 2026". Gia tri khac hien nguyen van.
status:    OPEN / ON SUB / FIXED / HIDDEN (HIDDEN an tau khoi trang).

SUA THONG SO TAU (particulars)
------------------------------
Nam trong open-tonnage.html. Sua truc tiep tren github.com:
mo file -> bieu tuong but chi -> Ctrl+F tim gia tri -> Commit.

CHINH KHOANG CACH GIAO DIEN
---------------------------
Trong <style> cua ca hai file:
  --sec-top / --sec-bot / --sec-gap
Sua cung gia tri o CA HAI file de hai trang khong lech nhip.

Developed by Pavel Hai
