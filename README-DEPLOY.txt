HAI DUONG MARITIME - OPEN TONNAGE
=================================
index.html        V1.3.0
open-tonnage.html V1.2.0

CAU TRUC - dat tat ca vao GOC repo (cung cap voi index.html cu)
---------------------------------------------------------------
  index.html                              ghi de file cu
  open-tonnage.html                       file moi
  open-tonnage.json                       du lieu vi tri tau
  robots.txt                              file moi
  sitemap.xml                             file moi
  scripts/build_open_tonnage.py           thu muc moi
  .github/workflows/sync-open-tonnage.yml thu muc moi

LUU Y: thu muc ".github" bat dau bang dau cham. Tren Windows,
File Explorer van tao duoc binh thuong. Neu khong thay thu muc
sau khi giai nen, bat "Hidden items" trong tab View.

SAU KHI PUSH
------------
1. Vao tab Actions cua repo -> chon "Sync open tonnage"
   -> bam "Run workflow" de chay ngay lan dau (khong cho 15 phut).

2. Neu Actions bao loi quyen ghi:
   Settings -> Actions -> General -> Workflow permissions
   -> chon "Read and write permissions" -> Save -> chay lai.

3. Mo https://hdmaritime.com.vn/open-tonnage.json
   -> phai thay du lieu tu Google Sheet (khong phai du lieu mau).

4. Mo https://hdmaritime.com.vn/open-tonnage.html
   -> kiem tra 3 the tau khop voi sheet.

5. Google Search Console -> nop lai sitemap.xml

CAP NHAT HANG NGAY
------------------
Chi sua Google Sheet. Toi da 20 phut sau web tu doi.
Can gap: vao tab Actions bam "Run workflow".

Cot open_date: de dang 2026-08-14 se hien "14 Aug 2026".
Gia tri khac (PROMPT, END AUG...) hien nguyen van.
Cot status: OPEN / ON SUB / FIXED / HIDDEN.

SUA THONG SO TAU (particulars)
------------------------------
Nam trong open-tonnage.html. Sua truc tiep tren github.com:
mo file -> bam bieu tuong but chi -> Ctrl+F tim gia tri -> Commit.

CHINH KHOANG CACH GIAO DIEN
---------------------------
Trong <style> cua ca hai file:
  --sec-top   khoang tren tieu de moi muc
  --sec-bot   khoang duoi noi dung
  --sec-gap   khoang duoi khoi tieu de
Sua cung gia tri o CA HAI file de hai trang khong lech nhip.

Developed by Pavel Hai
