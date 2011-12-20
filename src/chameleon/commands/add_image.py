# -*- coding: utf-8 -*-

from chameleon import api
import os


# TODO: image_add

@api.register
def add_image(db, filename, userid=None, root_path=None):
    """
    Add image to gekosale
    :param str filename:
    :param int languageid:
    :param int userid:
    :return: Image id
    """
    import Image

    db.validate('root_path', root_path, 'required')

    gallery_dir = os.path.join(root_path, "design/_gallery")

    img = Image.open(filename)
    # @todo odczytać mime type pliku i odczytać jego id z tabeli filetype
    fileTypeId = 12

    basename, ext = os.path.splitext(filename)
    # @todo odczytać id rozszerzenia pliku z tabeli fileextension
    fileExtensionId = 3

    cur = db.cursor()
    sql = """
        INSERT INTO file (
            idfile,
            name,
            filetypeid,
            fileextensionid,
            addid
        )
        VALUES
        (
            NULL,
            %(name)s,
            %(filetypeid)s,
            %(fileextensionid)s,
            %(userid)s
        )
        """
    data = {}
    data['name'] = basename
    data['filetypeid'] = fileTypeId
    data['fileextensionid'] = fileExtensionId
    data['userid'] = userid

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()

    imageid = cur.lastrowid

    # Generate thumbnails
    sizes = (50, 100, 200, 300)

    filename = "{0}{1}".format(imageid, ext)
    for dim in sizes:
        path = os.path.join(gallery_dir, "_{1}_{1}".format(dim, dim), filename)
        print path
        thumb = img.copy()
        thumb.thumbnail([dim] * 2, Image.ANTIALIAS)
        thumb.save(path)

    return imageid
