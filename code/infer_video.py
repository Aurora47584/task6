from ultralytics import YOLO
import cv2
import os
model = YOLO("runs/detect/train3/weights/best.pt")
video_path = "/home/aurora/task6/assets/origin.avi"
output_video_path = "/home/aurora/task6/assets/result_video.avi"
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print(f"❌ 无法打开视频{video_path}")
    exit()
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))
frame_count = 0
print("🚀 开始推理视频...")
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    results = model(frame)
    annotated_frame = results[0].plot()
    out.write(annotated_frame)
    frame_count += 1
    if frame_count % 30 == 0:
        print(f"已处理{frame_count}帧")
cap.release()
out.release()
print(f"✅ 视频推理完成！结果视频保存在{output_video_path}")

