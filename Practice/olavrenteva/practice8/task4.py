import argparse
import os
import cv2
import numpy
from PIL import Image, ImageDraw


def image_match_template(current_img_path, pattern_img_path):
    current_img = Image.open(current_img_path)
    pattern_img = Image.open(pattern_img_path)
    current_img_arr = cv2.cvtColor(numpy.array(current_img), cv2.COLOR_RGB2BGR555)
    pattern_img_arr = cv2.cvtColor(numpy.array(pattern_img), cv2.COLOR_RGB2BGR555)
    res = cv2.matchTemplate(current_img_arr, pattern_img_arr, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    pattern_size = pattern_img_arr.shape
    closest_area = [max_loc[0], max_loc[1], max_loc[0] + pattern_size[1], max_loc[1] + pattern_size[0]]
    source_size = current_img_arr.shape
    source_rad = source_size[0]/2
    return max_val, closest_area, source_rad


def screen_graphical_result(current_img_file, bbox):
    current_img = Image.open(current_img_file)
    ImageDraw.Draw(current_img).rectangle(xy=bbox, outline=(255, 0, 0), width=10)
    result_file_name = f'result_{os.path.basename(current_img_file)}'
    current_img.save(result_file_name)
    return result_file_name


def calc_score(current_img_path, bbox, source_rad):
    point_from_center = (bbox[0] + (bbox[2] - bbox[0]) / 2 - source_rad,
                         bbox[1] + (bbox[3] - bbox[1]) / 2 - source_rad)
    center_to_point = (point_from_center[0]**2 + point_from_center[1]**2)**0.5
    score = 10 - center_to_point // (source_rad / 10)
    return int(score)


def parse_args():
    parser = argparse.ArgumentParser(description='Searches for pattern in image')
    parser.add_argument('-s', '--source', help='Path to source file')
    parser.add_argument('-p', '--pattern', help='Path to pattern file')
    parser.add_argument('-i', '--ignore-color', type=bool, default=False, help='Ignore color')
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    max_val, closest_area, source_rad = image_match_template(args.source, args.pattern)
    res_file_name = screen_graphical_result(args.source, closest_area)
    score = calc_score(args.source, closest_area, source_rad)
    print(f"Pattern found with confidence {max_val}, {score=}. Open {res_file_name} for details")
