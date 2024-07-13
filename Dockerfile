# استخدام صورة Python الرسمية
FROM python:3.9-slim

# تعيين مجلد العمل في الحاوية
WORKDIR /app

# نسخ ملفات المتطلبات وتثبيت المكتبات
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# نسخ باقي الملفات
COPY . .

# تشغيل الكود الرئيسي
CMD ["python", "main.py"]
