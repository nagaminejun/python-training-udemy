import os
import string

def get_template_dir_path():
    """
    templatesフォルダのパスを取得する
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, 'templates')

def get_template(tamplate_file):
    """
    指定されたテンプレートファイルを読み込み、
    string.Template として返す
    """
    template_dir_path = get_template_dir_path()
    template_fiile_path = os.path.join(template_dir_path, tamplate_file)

    with open(template_fiile_path, 'r', encoding='utf-8') as file:
        contents = file.read()

    return string.Template(contents)
