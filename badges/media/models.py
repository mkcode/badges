from media import db

def upload_image(image_file, uploader_uri):
    image_db = db.Image(image_file=image_file, uploader_uri=uploader_uri)
    image_db.save()
    return get_image("/uri/media/image/{0}".format(image_db.id))


def get_image(image_uri):
    image_id = image_uri.strip('/').split('/')[-1]
    image_db = None
    try:
        image_db = db.Image.objects.get(id=image_id)
    except:
        raise
    image = {
        "uri": "/uri/media/image/{0}".format(image_db.id),
        "url": image_db.image_file.url,
    }
    return image
