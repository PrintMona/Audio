import whisper
import sounddevice as sd
import soundfile as sf

# تحميل نموذج Whisper
print("Loading Whisper model...")
model = whisper.load_model("base")
print("Model loaded successfully!")

# إعدادات التسجيل
duration = 10          # مدة التسجيل بالثواني
sample_rate = 16000

# اختيار الميكروفون رقم 1
sd.default.device = 1

print("Speak now...")

# تسجيل الصوت
audio = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1,
    dtype="float32"
)

# الانتظار حتى ينتهي التسجيل
sd.wait()

# حفظ التسجيل
sf.write("input.wav", audio, sample_rate)

print("Recording finished!")

# تحويل الصوت إلى نص
result = model.transcribe("input.wav")

print("\nYou said:")
print(result["text"])