# 📏 height-to-weight-predictor (โปรแกรมทำนายน้ำหนักจากส่วนสูง)

โปรเจกต์ Machine Learning เบื้องต้นด้วยภาษา Python สำหรับทำนายน้ำหนัก (กิโลกรัม) จากส่วนสูง (เซนติเมตร) โดยใช้หลักการ **Linear Regression** (การถดถอยเชิงเส้น) ผ่านไลบรารี `scikit-learn`

## ✨ ฟีเจอร์หลัก
- สอนโมเดล (Train) ด้วยชุดข้อมูลจำลองความสัมพันธ์ระหว่างส่วนสูงและน้ำหนัก
- รับค่าส่วนสูงจากผู้ใช้งานผ่านหน้าจอ Terminal (รองรับทั้งเลขจำนวนเต็มและทศนิยม)
- คำนวณและแสดงผลลัพธ์น้ำหนักที่คาดการณ์ได้ทันที

## 🛠️ เครื่องมือที่ใช้ (Tech Stack)
- **Python 3.x**
- **NumPy** (จัดการข้อมูลอาเรย์และตัวเลข)
- **Scikit-learn** (สร้างและเทรนโมเดล Linear Regression)

---

## 🚀 วิธีการติดตั้งและใช้งาน (Installation & Setup)

แนะนำให้ใช้งานผ่าน **Virtual Environment (`venv`)** เพื่อแยกไลบรารีของโปรเจกต์นี้ให้เป็นสัดส่วน ไม่ปะปนกับโปรเจกต์อื่นในเครื่อง

### 1. โคลนโปรเจกต์ลงเครื่อง (Clone Repository)
เปิด Terminal หรือ Command Prompt แล้วพิมพ์คำสั่ง:
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
*(หมายเหตุ: อย่าลืมเปลี่ยน `your-username/your-repo-name` เป็นลิงก์ GitHub ของคุณ)*

### 2. สร้าง Virtual Environment (`venv`)
พิมพ์คำสั่งด้านล่างเพื่อสร้างสภาพแวดล้อมจำลองชื่อ `venv`:
```bash
python -m venv venv
```

### 3. เปิดใช้งาน Virtual Environment (Activate)
เลือกพิมพ์คำสั่งตามระบบปฏิบัติการที่คุณใช้งาน:

* **สำหรับ Windows (Command Prompt / PowerShell):**
  ```bash
  venv\Scripts\activate
  ```
* **สำหรับ macOS / Linux:**
  ```bash
  source venv/bin/activate
  ```
*(เมื่อเปิดใช้งานสำเร็จ จะมีคำว่า `(venv)` ปรากฏขึ้นที่ด้านหน้าสุดของบรรทัดใน Terminal)*

### 4. ติดตั้งไลบรารีที่จำเป็น (Install Dependencies)
```bash
pip install numpy scikit-learn
```

---

## 💻 วิธีรันโปรแกรม (Usage)

เมื่อติดตั้งไลบรารีเรียบร้อยแล้ว สามารถสั่งรันโค้ดได้ทันที (สมมติว่าไฟล์โค้ดชื่อ `main.py`):

```bash
python main.py
```

### ตัวอย่างผลลัพธ์การทำงาน:
```text
กรุณากรอกส่วนสูงของคุณ (ซม.): 172.5
สำหรับคนส่วนสูง 172.5 ซม.
โมเดลทายว่าจะมีน้ำหนักประมาณ: 72.50 กิโลกรัม
```

### การปิดใช้งาน Virtual Environment
เมื่อใช้งานเสร็จเรียบร้อยแล้ว สามารถออกจาก `venv` ได้ด้วยคำสั่ง:
```bash
deactivate
```

---

## 📁 โครงสร้างไฟล์ในโปรเจกต์ (Project Structure)
```text
📦 your-repo-name
 ┣ 📂 venv/           # โฟลเดอร์ Virtual Environment (ไม่ควรอัปโหลดขึ้น GitHub)
 ┣ 📜 main.py         # ไฟล์โค้ดหลักสำหรับเทรนโมเดลและทำนายผล
 ┗ 📜 README.md       # ไฟล์อธิบายรายละเอียดโปรเจกต์
```