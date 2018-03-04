PASCAL VOC Writer
=================

This library can be used to create image annotation XML files in the PASCAL VOC
file format.

Install
-------

``pip install -e git+git@github.com:Labelbox/pascal-voc-writer.git@master``

Use
---

    # Writer(path, width, height)

    writer = Writer('path/to/img.jpg', 800, 400)


    # ::addObject(name, xy_coords)

    writer.addObject('cat', [100, 100, 200, 200])


    # ::save(path)

    writer.save('path/to/img.xml')
