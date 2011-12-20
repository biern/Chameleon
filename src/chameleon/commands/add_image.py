# -*- coding: utf-8 -*-

from chameleon import api
import os


@api.register
def add_image(db, filename, userid=None):
    """
    Add image to gekosale
    :param str filename:
    :param int languageid:
    :param int userid:
    :return: Image id
    """

    # @todo stworzyć miniaturki i umieścic je w katalogach: design/_gallery/*

    # @todo odczytać mime type pliku i odczytać jego id z tabeli filetype
    fileTypeId = 12

    # Read file extension
    fileNameWithoutExt, fileExtension = os.path.splitext(filename)

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
    data['name'] = fileNameWithoutExt
    data['filetypeid'] = fileTypeId
    data['fileextensionid'] = fileExtensionId
    data['userid'] = userid

    cur = db.cursor()
    cur.execute(sql, data)
    db.commit()

    imageid = cur.lastrowid

    return imageid
