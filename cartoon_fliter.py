import cv2
import numpy as np

def render_cartoon(image_path):
    # 1. 이미지 읽기
    img = cv2.imread(image_path)
    if img is None:
        print("이미지 파일을 찾을 수 없습니다. 경로를 확인하세요.")
        return

    # 2. 외곽선 추출 (Edge Mask)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray_blur, 255, 
                                  cv2.ADAPTIVE_THRESH_MEAN_C, 
                                  cv2.THRESH_BINARY, 9, 9)

    # 3. 색상 단순화 (Bilateral Filter)
    color = cv2.bilateralFilter(img, 9, 300, 300)

    # 4. 합성
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # 5. [수정됨] 결과 출력 및 창 크기 조절
    # WINDOW_NORMAL을 설정해야 창 크기를 마우스로 조절하거나 resizeWindow가 먹힙니다.
    cv2.namedWindow("Cartoon Result", cv2.WINDOW_NORMAL) 
    cv2.resizeWindow("Cartoon Result", 800, 800) # 가로세로 800px 정도로 보기 좋게 조절
    
    cv2.imshow("Cartoon Result", cartoon)
    
    # [수정됨] 자동으로 결과 파일 저장 (이 사진을 GitHub에 올리시면 됩니다)
    cv2.imwrite('output_demo.jpg', cartoon)
    print("결과가 'output_demo.jpg'로 저장되었습니다.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 파일 확장자가 .png인지 .jpg인지 꼭 확인하세요!
render_cartoon('input.jpg.jpg')