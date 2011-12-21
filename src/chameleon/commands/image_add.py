# -*- coding: utf-8 -*-

from chameleon import api
import os
import mimetypes
import shutil


@api.register
def image_add(db, filename, userid=None, root_path=None, shopid=None):
    """
    Add image to gekosale

    :param str filename:
    :param int languageid:
    :param int userid:
    :return: Image id
    """
    cur = db.cursor()

    import Image

    db.validate('root_path', root_path, 'required')
    db.validate('shopid', shopid, 'required')

    gallery_dir = os.path.join(root_path, "design/_gallery")

    # image

    img = Image.open(filename)
    basename, ext = os.path.splitext(filename)
    basename = os.path.basename(basename)

    # extension id

    cur.execute(
        """
        SELECT
            idfileextension
        FROM
            fileextension
        WHERE
            name = %s
        """, (ext[1:]))
    extid = cur.fetchone()[0]

    if extid is None:
        raise IOError('Unsupported extension "{}"'.format(ext))

    # mimetype id

    try:
        mimetype = mimetypes.types_map[ext]
    except KeyError:
        raise Exception('unknown mimetype for extension "{}"'.format(ext))

    cur.execute(
        """
        SELECT
            idfiletype
        FROM
            filetype
        WHERE
            name = %s
        """, (mimetype,))

    mimeid = cur.fetchone()[0]

    sql = """
        INSERT INTO file (
            idfile,
            name,
            filetypeid,
            fileextensionid,
            addid,
            visible
        )
        VALUES
        (
            NULL,
            %(name)s,
            %(filetypeid)s,
            %(fileextensionid)s,
            %(userid)s,
            1
        )
        """
    data = {}
    data['name'] = basename
    data['filetypeid'] = mimeid
    data['fileextensionid'] = extid
    data['userid'] = userid

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()

    imageid = cur.lastrowid

    # Generate thumbnails
    sizes = (50, 100, 200, 300)

    filename = "{0}{1}".format(imageid, ext)
    for dim in sizes:
        path = os.path.join(gallery_dir, "_{}_{}".format(dim, dim))
        try:
            os.mkdir(path)
        except OSError:
            pass

        thumb = img.copy()
        thumb.thumbnail([dim] * 2, Image.ANTIALIAS)
        thumb.save(os.path.join(path, filename))

        path = os.path.join(gallery_dir, "_{}_{}_{}".format(dim, dim, shopid))
        try:
            os.mkdir(path)
        except OSError:
            pass

        thumb.save(os.path.join(path, filename))

    img.save(os.path.join(gallery_dir, "_orginal", filename))

    return imageid
