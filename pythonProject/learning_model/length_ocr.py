import cv2
import numpy as np
import pytesseract
import re

def length_from_image(img_url):
    imageOrgCp = cv2.imread(img_url)  # 원본 이미지 불러오기
    imageOrgCp = cv2.resize(imageOrgCp, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    height, width, channel = imageOrgCp.shape  # 원본 이미지 크기 저장
    center = (width // 2, height // 2)  # 이미지 center값 저장
    grayCp = cv2.cvtColor(imageOrgCp, cv2.COLOR_BGR2GRAY)  # 이미지 흑백으로 전환

    grayCp = cv2.bitwise_not(grayCp)  # 이미지 색반전
    threshold = 250  # 숫자영역만 원래 0에 가까울것으로 추정되기때문에 색반전후 250 이상인값만 숫자일것으로 추정
    ret, mask = cv2.threshold(grayCp, threshold, 255, cv2.THRESH_BINARY_INV)  # threshold를 사용해 숫자영역을 제외한 나머지 부분 0으로 변환
    mask = cv2.bitwise_not(mask)  # mask영역 색 반전

    img_blurred = cv2.GaussianBlur(mask, ksize=(3, 3),
                                   sigmaX=0)  # 숫자영역중 흰색과 경계인 부분은 실제 0에 가까운값이 아니었기때문에 굉장히 얇은 실선 형태로 변환되었기때문에 가우시안 블러를 사용해 모양을 다시 살림

    img_blurred = 255 - img_blurred  #
    ret, mask = cv2.threshold(img_blurred, threshold, 255, cv2.THRESH_BINARY_INV)

    # cv2_imshow(mask)

    contours, _ = cv2.findContours(
        mask,
        mode=cv2.RETR_LIST,
        method=cv2.CHAIN_APPROX_SIMPLE
    )

    temp_result = np.zeros((height, width), dtype=np.uint8)

    contours_dict = []

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(temp_result, pt1=(x, y), pt2=(x + w, y + h), color=255, thickness=-1)

        # insert to dict
        contours_dict.append({
            'x': x,
            'y': y,
            'w': w,
            'h': h,
            'cx': x + (w / 2),
            'cy': y + (h / 2)
        })
    # cv2_imshow(temp_result)

    bit_and = cv2.bitwise_and(grayCp, temp_result)

    # cv2_imshow(bit_and)
    serch_list = []
    for i in range(0, 360, 5):
        M = cv2.getRotationMatrix2D(center, i, 1.0)
        rotated = cv2.warpAffine(bit_and, M, (width, height))
        chars = pytesseract.image_to_string(255 - rotated, config='--psm 6')
        # print(chars)
        serch_list.append(re.search("\d+cm", chars))

    len_dict = {}
    for item in serch_list:
        if item != None:
            try:
                len_dict[item.group()] += 1
            except:
                len_dict[item.group()] = 1
    sorted_dict = sorted(len_dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_dict
img_url = "test_img/po1.jpg"
len_dict = length_from_image(img_url)
print(len_dict)
img_url = "test_img/po2.jpg"
len_dict = length_from_image(img_url)
print(len_dict)
img_url = "test_img/pa1.jpg"
len_dict = length_from_image(img_url)
print(len_dict)
img_url = "test_img/pa2.jpg"
len_dict = length_from_image(img_url)
print(len_dict)
img_url = "test_img/yang1.jpg"
len_dict = length_from_image(img_url)
print(len_dict)
img_url = "test_img/yang1.jpg"
len_dict = length_from_image(img_url)
print(len_dict)