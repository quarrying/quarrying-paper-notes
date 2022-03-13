import os
from datetime import datetime
from datetime import timezone
from datetime import timedelta


def get_utc8now():
    utcnow = datetime.now(timezone.utc)
    utc8now = utcnow.astimezone(timezone(timedelta(hours=8)))
    return utc8now


def walk_dirs(dirname):
    filenames = []
    for root, _, files in os.walk(dirname):
        for item in files:
            filenames.append(os.path.join(root, item))
    return filenames


def save_list(filename, list_obj, encoding='utf-8', append_break=True):
    with open(filename, 'w', encoding=encoding) as f:
        if append_break:
            for item in list_obj:
                f.write(str(item) + '\n')
        else:
            for item in list_obj:
                f.write(str(item))


def _get_all_filenames(dirname):
    dirname = os.path.expanduser(dirname)
    dirname = os.path.abspath(dirname)

    all_filenames = []
    for item in os.listdir(dirname):
        fullname = os.path.join(dirname, item)
        if os.path.isdir(fullname) and not item.startswith('_'):
            all_filenames += walk_dirs(fullname)
    return all_filenames


def _normalize_filenames(filenames, prefix=None):
    if prefix is None:
        prefix = ''
    else:
        prefix = prefix.replace('\\', '/')

    dst_filenames = []
    for filename in filenames:
        dst_filename = filename.replace('\\', '/')
        dst_filename = dst_filename[len(prefix):]
        dst_filename = dst_filename.lstrip('/')
        dst_filenames.append(dst_filename)
    dst_filenames.sort()
    return dst_filenames


if __name__ == '__main__':
    dst_str = 'archives'
    os.makedirs(dst_str, exist_ok=True)

    now = get_utc8now()
    filename = os.path.join(dst_str, '{}.txt'.format(now.strftime('%Y%m')))
    
    root_dir = 'G:/_baidu'
    filenames = _get_all_filenames(os.path.join(root_dir, '1数学'))
    filenames += _get_all_filenames(os.path.join(root_dir, '2视觉'))
    filenames = _normalize_filenames(filenames, root_dir)
    save_list(filename, filenames)
    