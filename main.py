# 1. นำเข้าเครื่องมือ (Library) ที่ต้องใช้
import numpy as np
from sklearn.linear_model import LinearRegression

# 2. เตรียมข้อมูล (Data)
# X (ตัวใหญ่) คือ "ข้อมูลที่เรามี" (ส่วนสูงหน่วยเป็น ซม.) 
# บังคับว่าต้องใส่เป็น List ซ้อน List แบบนี้ [[ค่าที่ 1], [ค่าที่ 2]]
X_height = np.array([
    [150], 
    [160], 
    [170], 
    [180], 
    [190]
])

# y (ตัวเล็ก) คือ "คำตอบที่เราอยากให้โมเดลทาย" (น้ำหนักหน่วยเป็น กก.)
y_weight = np.array([50, 60, 70, 80, 90])

# 3. สร้างและสอนโมเดล (Train Model)
model = LinearRegression() # เลือกโมเดลหาความสัมพันธ์แบบเส้นตรง
model.fit(X_height, y_weight) # สั่งให้โมเดล "เรียนรู้" ความสัมพันธ์ระหว่าง X และ y

# 4. รับค่าส่วนสูงจากผู้ใช้
user_hight = float(input("กรุณากรอกส่วนสูงของคุณ (ซม.): "))

# 5. จัดรูปแบบข้อมูลให้เป็น 2 มิติ [[ค่า]] ตามที่โมเดลต้องการ
new_person = np.array([[user_hight]])

# 6. ให้โมเดลทำนายผลและแสดงคำตอบ
predicted_weight = model.predict(new_person)

# แสดงผลลัพธ์
print(f"คนที่มีส่วนสูง {new_person[0][0]} ซม.")
print(f"โมเดลทายว่าจะมีน้ำหนักประมาณ: {predicted_weight[0]:.2f} กิโลกรัม")