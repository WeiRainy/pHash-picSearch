import os
import re
import docx


def get_pictures(word_path, result_path):
    """
    图片提取
    :param word_path: word路径
    :param result_path：结果存放路径
    """
    try:
        doc = docx.Document(word_path)
        dict_rel = doc.part._rels
        for rel in dict_rel:
            rel = dict_rel[rel]
            if "image" in rel.target_ref:
                if not os.path.exists(result_path):
                    os.makedirs(result_path)
                img_name = re.findall("/(.*)", rel.target_ref)[0]
                # word_name = word_path.split('/')[-1]
                # if os.sep in word_name:
                #     new_name = word_name.split('\\')[-1]
                # else:
                #     new_name = word_name.split('/')[-1]
                # img_name = f'{img_name}'
                with open(f'{result_path}/{img_name}', "wb") as f:
                    f.write(rel.target_part.blob)
    except:
        print("找不到文件")
        pass
