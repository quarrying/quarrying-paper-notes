import os
import khandy


def _get_all_filenames(dirname):
    dirname = os.path.expanduser(dirname)
    dirname = os.path.abspath(dirname)

    all_filenames = []
    for item in os.listdir(dirname):
        fullname = os.path.join(dirname, item)
        if os.path.isdir(fullname) and not item.startswith('_'):
            all_filenames += khandy.get_all_filenames(fullname)
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

    now = khandy.get_utc8now()
    filename = os.path.join(dst_str, f"{now.strftime('%Y%m')}.txt")
    
    root_dir = 'G:/_baidu'
    filenames = _get_all_filenames(os.path.join(root_dir, '1数学'))
    filenames += _get_all_filenames(os.path.join(root_dir, '2视觉'))
    filenames = _normalize_filenames(filenames, root_dir)
    khandy.save_list(filename, filenames)
    